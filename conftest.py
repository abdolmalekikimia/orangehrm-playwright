import json
import os
from datetime import datetime, timezone
from html import escape
from pathlib import Path

import pytest
from playwright.sync_api import expect

CATALOG = Path(__file__).parent / "docs/test-plan/scenario-catalog.json"


def pytest_addoption(parser):
    parser.addoption("--scenario-map", default=None, help="Write collected scenario mappings to this JSON file")


def pytest_configure(config):
    config.addinivalue_line("markers", "scenario(id, coverage='full', variation=''): scenario catalog traceability")
    config._scenario_results = {}
    config._scenario_catalog = {c["id"]: c for c in json.loads(CATALOG.read_text(encoding="utf-8"))["cases"]}


def pytest_collection_modifyitems(config, items):
    for item in items:
        markers = list(item.iter_markers("scenario"))
        if len(markers) != 1:
            raise pytest.UsageError(f"{item.nodeid}: exactly one scenario marker is required")
        marker = markers[0]
        if len(marker.args) != 1 or marker.args[0] not in config._scenario_catalog:
            raise pytest.UsageError(f"{item.nodeid}: unknown scenario ID")
        coverage = marker.kwargs.get("coverage", "full")
        if coverage not in {"full", "partial"}:
            raise pytest.UsageError(f"{item.nodeid}: coverage must be full or partial")
        meta = {"scenario_id": marker.args[0], "coverage": coverage,
                "variation": marker.kwargs.get("variation", ""), "nodeid": item.nodeid}
        item._scenario_meta = meta
        item.user_properties.extend((key, value) for key, value in meta.items() if key != "nodeid")
        config._scenario_results[item.nodeid] = {**meta, "outcome": "not_run", "phases": {}, "duration_seconds": 0.0}


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    report = (yield).get_result()
    result = item.config._scenario_results[item.nodeid]
    result["phases"][report.when] = report.outcome
    result["duration_seconds"] += report.duration
    if report.failed:
        result["outcome"] = "failed" if report.when == "call" else "error"
    elif report.skipped and result["outcome"] not in {"failed", "error"}:
        result["outcome"] = "skipped"
    elif report.when == "call" and result["outcome"] not in {"failed", "error", "skipped"}:
        result["outcome"] = "passed"


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    cells.insert(1, "<th>Scenario / scope</th>")


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    properties = dict(report.user_properties)
    value = properties.get("scenario_id", "")
    scope = properties.get("coverage", "")
    variation = properties.get("variation", "")
    cells.insert(1, f"<td>{escape(value)}<br>{escape(scope)}<br>{escape(variation)}</td>")


def pytest_sessionfinish(session, exitstatus):
    results = list(session.config._scenario_results.values())
    mapping_path = session.config.getoption("--scenario-map")
    if mapping_path:
        target = Path(mapping_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        args = session.config.args
        complete = (len(args) == 1 and Path(args[0]).resolve() == Path(session.config.rootpath) / "tests"
                    and not session.config.option.keyword and not session.config.option.markexpr)
        target.write_text(json.dumps({"complete_collection": complete, "results": results}, indent=2) + "\n", encoding="utf-8")
    if session.config.option.collectonly:
        return
    catalog = session.config._scenario_catalog
    covered = {r["scenario_id"] for r in results}
    full = {r["scenario_id"] for r in results if r["coverage"] == "full"}
    html_path = session.config.getoption("htmlpath", default=None)
    stem = Path(html_path).stem if html_path else "index"
    filename = "scenario-results.json" if stem == "index" else stem + "-scenario-results.json"
    output = Path(session.config.rootpath) / "reports" / filename
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = {"generated_at_utc": datetime.now(timezone.utc).isoformat(), "exit_status": int(exitstatus),
               "environment": "public-demo-compatible; no business-data mutation",
               "catalog_scenarios": len(catalog), "test_variations": len(results),
               "implemented_full_scenarios_in_this_run": len(full),
               "implemented_partial_scenarios_in_this_run": len(covered - full),
               "not_selected_or_unimplemented": sorted(set(catalog) - covered), "results": results}
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


@pytest.fixture(scope="session")
def demo_url():
    return os.getenv("ORANGEHRM_URL", "https://opensource-demo.orangehrmlive.com").rstrip("/")


@pytest.fixture(scope="session")
def credentials():
    return os.getenv("ORANGEHRM_USERNAME", "Admin"), os.getenv("ORANGEHRM_PASSWORD", "admin123")


@pytest.fixture(autouse=True)
def timeouts(request):
    expect.set_options(timeout=15000)
    if "readonly_page" not in request.fixturenames:
        page = request.getfixturevalue("page")
        page.set_default_timeout(30000)
        page.set_default_navigation_timeout(60000)


@pytest.fixture
def login(page, demo_url):
    from pages.login_page import LoginPage
    model = LoginPage(page, demo_url)
    model.open()
    return model


@pytest.fixture
def authenticated_page(login, credentials):
    login.sign_in(*credentials)
    login.expect_dashboard()
    return login.page


@pytest.fixture(scope="session")
def read_only_state(browser, demo_url, credentials):
    """One login for nonmutating checks; never shared with logout/session tests."""
    from pages.login_page import LoginPage
    context = browser.new_context()
    try:
        page = context.new_page()
        page.set_default_navigation_timeout(60000)
        model = LoginPage(page, demo_url)
        model.open()
        model.sign_in(*credentials)
        model.expect_dashboard()
        return context.storage_state()
    finally:
        context.close()


@pytest.fixture
def readonly_page(new_context, read_only_state, demo_url):
    """Fresh context per variation; reusable state is kept only in memory."""
    context = new_context(storage_state=read_only_state)
    try:
        page = context.new_page()
        page.set_default_timeout(30000)
        page.set_default_navigation_timeout(60000)
        page.goto(demo_url + "/web/index.php/dashboard/index", wait_until="domcontentloaded")
        expect(page.get_by_role("heading", name="Dashboard", exact=True)).to_be_visible()
        yield page
    finally:
        context.close()
