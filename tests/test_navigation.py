import json
import re
from pathlib import Path
from uuid import uuid4

import pytest
from playwright.sync_api import expect

from pages.navigation_page import NavigationPage

DATA = json.loads((Path(__file__).parent / "data/navigation.json").read_text(encoding="utf-8"))
MODULES = DATA["modules"]


def search_unknown_value(page, module, label):
    NavigationPage(page).open_module(module)
    field = page.locator(".oxd-input-group").filter(has=page.get_by_text(label, exact=True)).get_by_role("textbox")
    # Employee IDs have a shorter API limit than usernames; this is a valid unknown value, not a length test.
    value = "q" + uuid4().hex[:9]
    field.fill(value)
    endpoint, key = ("/pim/employees", "employeeId") if module == "PIM" else ("/admin/users", "username")
    with page.expect_response(lambda response: endpoint + "?" in response.url and key + "=" + value in response.url) as pending:
        page.get_by_role("button", name="Search", exact=True).click()
    assert pending.value.status == 200, f"{module} search returned HTTP {pending.value.status}"
    expect(page.locator(".oxd-layout-context").get_by_text("No Records Found", exact=True)).to_be_visible()
    expect(page.get_by_role("row").filter(has=page.get_by_role("cell"))).to_have_count(0)
    return field


def module_param(spec):
    original = {"Admin": "COMMON-001", "PIM": "COMMON-002", "Directory": "COMMON-003"}.get(spec["module"])
    marker = pytest.mark.scenario(original) if original else pytest.mark.scenario(
        "COMMON-004", coverage="partial", variation=spec["module"] + " landing page, Admin role")
    return pytest.param(spec, id=spec["module"].replace(" ", "-"), marks=marker)


@pytest.mark.parametrize("spec", [module_param(s) for s in MODULES])
def test_module_navigation(readonly_page, spec):
    nav = NavigationPage(readonly_page)
    nav.open_module(spec["module"])
    nav.expect_destination(spec)
    if spec["module"] in {"Admin", "PIM", "Directory"}:
        expect(readonly_page.get_by_role("button", name="Search", exact=True)).to_be_visible()
    if spec["module"] == "Maintenance":
        readonly_page.get_by_role("button", name="Cancel", exact=True).click()
    nav.return_dashboard()


@pytest.mark.parametrize("spec", [pytest.param(s, id=s["module"].replace(" ", "-"), marks=pytest.mark.scenario(
    "AUTH-017", coverage="partial", variation=s["module"] + " protected entry route")) for s in MODULES])
def test_module_entry_requires_authentication(page, demo_url, spec):
    page.goto(demo_url + "/web/index.php" + spec["entry"], wait_until="domcontentloaded")
    expect(page).to_have_url(re.compile(r"/auth/login$"))
    expect(page.get_by_role("button", name="Login", exact=True)).to_be_visible()


@pytest.mark.parametrize("spec", [pytest.param(s, id=s["module"] + "-" + s["child"], marks=pytest.mark.scenario(
    "COMMON-004", coverage="partial", variation=s["module"] + "/" + s["menu"] + "/" + s["child"] + ", Admin role"))
    for s in DATA["submenus"]])
def test_submenu_destination(readonly_page, spec):
    NavigationPage(readonly_page).open_submenu(spec)


@pytest.mark.parametrize("query,names", [
    pytest.param("Admin", ["Admin"], id="full-name"),
    pytest.param("im", ["PIM", "Time", "Claim"], id="partial-name"),
    pytest.param("qa_nonexistent_menu", [], id="no-match"),
])
@pytest.mark.scenario("COMMON-005", coverage="partial", variation="sidebar search/reset, Admin role; collapse not yet covered")
def test_sidebar_search_and_clear(readonly_page, query, names):
    panel = readonly_page.get_by_role("navigation", name="Sidepanel", exact=True)
    search = panel.get_by_role("textbox", name="Search", exact=True)
    links = panel.locator(".oxd-main-menu-item")
    search.fill(query)
    expect(links).to_have_text(names)
    search.fill("")
    expect(links).to_have_text([s["module"] for s in MODULES])


@pytest.mark.parametrize("module,label", [("Admin", "Username"), ("PIM", "Employee Id")])
@pytest.mark.scenario("COMMON-007", coverage="partial", variation="unknown exact text value in Admin Username / PIM Employee Id")
def test_unknown_filter_has_empty_result(readonly_page, module, label):
    search_unknown_value(readonly_page, module, label)


@pytest.mark.parametrize("module,label", [("Admin", "Username"), ("PIM", "Employee Id")])
@pytest.mark.scenario("COMMON-009", coverage="partial", variation="Reset clears one exact text filter, Admin/PIM; list-return retention not covered")
def test_reset_clears_text_filter(readonly_page, module, label):
    field = search_unknown_value(readonly_page, module, label)
    readonly_page.get_by_role("button", name="Reset", exact=True).click()
    expect(field).to_have_value("")


@pytest.mark.scenario("MAINT-001")
def test_maintenance_cancel_returns_to_previous_page(readonly_page):
    previous_url = readonly_page.url
    readonly_page.get_by_role("link", name="Maintenance", exact=True).click()
    expect(readonly_page.get_by_role("heading", name="Administrator Access", exact=True)).to_be_visible()
    readonly_page.get_by_role("button", name="Cancel", exact=True).click()
    expect(readonly_page).to_have_url(previous_url)
    expect(readonly_page.get_by_role("heading", name="Dashboard", exact=True)).to_be_visible()
