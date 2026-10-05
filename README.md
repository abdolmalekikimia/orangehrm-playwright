# OrangeHRM Playwright Demo

A runnable public QA demonstration using Python, Pytest and Playwright against the public OrangeHRM demo. This project is separate from private company test suites. Implementation is AI-assisted and reviewed through live execution.

## Quick start for recruiters

Requirements: Python 3.11+, Google Chrome installed, an internet connection and access to the public demo.

**Windows:** download/unzip the repository and double-click `run-demo.cmd`. It creates a local virtual environment, installs dependencies, opens Google Chrome so you can watch the tests, and opens the HTML report afterward. The launcher detects Python 3.11+ via `py`, `python`, a standard Windows installation, or the bundled Codex runtime when present. To use another installation, set `ORANGEHRM_PYTHON` to its `python.exe` path. A bundled Codex runtime is optional; recruiters can use a normal Python installation.

**macOS / Linux:**

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest --headed --browser-channel chrome --slowmo 500
```

## Watch the tests in Google Chrome

From the project folder in Windows PowerShell, after the initial setup:

```powershell
.\.venv\Scripts\python.exe -m pytest --headed --browser-channel chrome --slowmo 500
```

Or run the automatic setup and visible test launcher:

```powershell
.\run-demo.cmd
```

Chrome opens during execution. `--headed` shows the browser; `--browser-channel chrome` selects installed Google Chrome; `--slowmo 500` adds a 500 ms delay to browser actions so they are easier to follow. Each test uses a fresh browser context; Chrome closes when the suite finishes.

Open `reports/index.html` after the run. Failed tests retain screenshots and Playwright traces in `reports/artifacts`. Open a trace with `python -m playwright show-trace path/to/trace.zip`.

For a faster run without a visible window, use `python -m pytest --browser-channel chrome`. GitHub Actions runs headlessly using its own Chromium installation.

## Coverage

10 independently isolated test cases: successful login, incorrect password, three required-field combinations, logout/session protection, unauthenticated redirect, and navigation to Admin, PIM and Directory followed by a return to Dashboard.

Tests use real browser actions and observable UI assertions; no mocked API routes or fixed sleeps. Each case receives a fresh browser context. No employee records, account settings or shared business data are changed.

The demo displays the public credentials `Admin` / `admin123`. Optional environment variables `ORANGEHRM_URL`, `ORANGEHRM_USERNAME`, `ORANGEHRM_PASSWORD` override defaults; credentials must belong to a compatible test system.

## GitHub execution

The **Live demo tests** workflow runs on pushes and pull requests, or manually from **Actions → Live demo tests → Run workflow**. Download the `orangehrm-report` artifact to inspect the report.

This is an external shared demo: downtime, changed credentials, rate limits or UI changes can cause genuine failures. Tests fail visibly rather than silently skip or retry into a green result. Passing this suite demonstrates the listed demo behaviors, not production OrangeHRM correctness or complete HR workflow coverage.


