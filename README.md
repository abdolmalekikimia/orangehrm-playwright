# OrangeHRM Playwright QA Portfolio

[![Live demo tests](https://github.com/abdolmalekikimia/orangehrm-playwright/actions/workflows/checks.yml/badge.svg)](https://github.com/abdolmalekikimia/orangehrm-playwright/actions/workflows/checks.yml)

A runnable public QA portfolio using Python, Pytest and Playwright against the OrangeHRM demo. Implementation is AI-assisted and reviewed through live execution; this project is separate from private company test suites.

## Tech stack

Python 3.11+ · Pytest · Playwright · Google Chrome / Chromium · pytest-html · GitHub Actions

## Scope and automation status

| Measure | Current scope |
|---|---|
| Test design | 323 scenarios across all 12 main modules |
| Automated | 14 scenarios with full specified scope |
| Partial | 7 scenarios with limited implemented variations |
| Planned | 302 scenarios without automation |
| Executable checks | 97 mapped test variations |

The suite maps every test to a scenario ID. It covers login/session checks, all 12 module landing pages, 53 submenu destinations, protected entry routes, sidebar search, two text filters/reset and Maintenance cancellation. Broad navigation/filter/authorization cases are explicitly partial. No business records or configuration are changed.

**[Browse the Test Scenario Wiki](https://github.com/abdolmalekikimia/orangehrm-playwright/wiki)** for strategy, module-specific cases, authorization/integration checks, bug-report guidance and automation coverage. [Repository Markdown and catalogs](docs/test-plan/README.md) remain available as the editable source.

## Run in visible Google Chrome

Requirements: Python 3.11+, Google Chrome, internet access and a reachable public demo.

From the project folder in Windows PowerShell:

```powershell
.\run-demo.cmd
```

The launcher sets up a local virtual environment, opens Chrome during the tests and opens the HTML report afterward. For an existing environment:

```powershell
.\.venv\Scripts\python.exe -m pytest --headed --browser-channel chrome --slowmo 500
```

[macOS/Linux setup, Python detection and execution options](https://github.com/abdolmalekikimia/orangehrm-playwright/wiki/Test-Execution)

## Reports and CI

- Local report: `reports/index.html`; failures retain screenshots/traces in `reports/artifacts`; scenario outcomes are in `reports/scenario-results.json` and JUnit in `reports/junit.xml`.
- [Live demo tests and downloadable CI report artifacts](https://github.com/abdolmalekikimia/orangehrm-playwright/actions/workflows/checks.yml).
- [Automation coverage and source references](https://github.com/abdolmalekikimia/orangehrm-playwright/wiki/Automation-Coverage).

The public demo uses its published `Admin` / `admin123` credentials. It is a shared external service; availability and UI changes can cause failures. Passing this suite validates the listed behaviors, not the entire 323-scenario plan. Reports label full/partial scope and actual outcomes separately. Mutating workflow/configuration tests require an isolated instance; purge requires a disposable instance.
