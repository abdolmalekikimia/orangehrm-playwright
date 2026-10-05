# OrangeHRM Playwright Demo

A runnable public QA demonstration using Python, Pytest and Playwright against the public OrangeHRM demo. This project is separate from private company test suites. Implementation is AI-assisted and reviewed through live execution.

## Quick start for recruiters

Requirements: Python 3.11+, an internet connection and access to the public demo.

**Windows:** download/unzip the repository and double-click `run-demo.cmd`. It creates a local virtual environment, installs dependencies and Chromium, runs the tests and opens the HTML report. Install Python with the Python launcher (`py`) enabled first.

**macOS / Linux:**

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest
```

On Linux, if browser system libraries are missing, use `python -m playwright install --with-deps chromium`.

Open `reports/index.html` after the run. To watch the browser, run `python -m pytest --headed` (Windows: `run-demo.cmd --headed`). Failed tests retain screenshots and Playwright traces in `reports/artifacts`. Open a trace with `python -m playwright show-trace path/to/trace.zip`.

If Chromium downloads are unavailable in your region, the Windows launcher tries installed Google Chrome. To choose it directly on any platform, use `python -m pytest --browser-channel chrome` (requires Chrome installed).

## Coverage

10 independently isolated test cases: successful login, incorrect password, three required-field combinations, logout/session protection, unauthenticated redirect, and navigation to Admin, PIM and Directory followed by a return to Dashboard.

Tests use real browser actions and observable UI assertions; no mocked API routes or fixed sleeps. Each case receives a fresh browser context. No employee records, account settings or shared business data are changed.

The demo displays the public credentials `Admin` / `admin123`. Optional environment variables `ORANGEHRM_URL`, `ORANGEHRM_USERNAME`, `ORANGEHRM_PASSWORD` override defaults; credentials must belong to a compatible test system.

## GitHub execution

The **Live demo tests** workflow runs on pushes and pull requests, or manually from **Actions → Live demo tests → Run workflow**. Download the `orangehrm-report` artifact to inspect the report.

This is an external shared demo: downtime, changed credentials, rate limits or UI changes can cause genuine failures. Tests fail visibly rather than silently skip or retry into a green result. Passing this suite demonstrates the listed demo behaviors, not production OrangeHRM correctness or complete HR workflow coverage.
