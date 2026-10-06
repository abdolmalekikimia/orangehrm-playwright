# Shared controls and navigation

**23 scenarios | 3 automated | 4 partial | 16 planned**

[Plan overview](README.md) | [CSV catalog](scenario-catalog.csv) | [JSON catalog](scenario-catalog.json)

## Scope

Apply these checks separately to every relevant page in the matrix; one example is not evidence for all pages.

## Default prerequisites

Authorized account; known fixtures in isolation for deterministic filtering comparisons.

Shared controls and [evidence rules](README.md) also apply. R = read-only public demo; I = isolated instance; D = disposable instance. Partial implementations run only their documented public-demo variation, not the complete I/D workflow.

## Scenario index

| ID | Scenario | Design environment | Implementation status |
|---|---|---|---|
| [COMMON-001](#common-001) | Initial navigation to Admin | R | Automated |
| [COMMON-002](#common-002) | Initial navigation to PIM | R | Automated |
| [COMMON-003](#common-003) | Initial navigation to Directory | R | Automated |
| [COMMON-004](#common-004) | Every menu and submenu | I | Partial |
| [COMMON-005](#common-005) | Sidebar search and collapse | I | Partial |
| [COMMON-006](#common-006) | Account menu and Help | I | Planned |
| [COMMON-007](#common-007) | Individual filters | I | Partial |
| [COMMON-008](#common-008) | Combined filters | I | Planned |
| [COMMON-009](#common-009) | Reset and return to the list | I | Partial |
| [COMMON-010](#common-010) | Autocomplete identity selection | I | Planned |
| [COMMON-011](#common-011) | Sorting | I | Planned |
| [COMMON-012](#common-012) | Pagination | I | Planned |
| [COMMON-013](#common-013) | Single and bulk selection | I | Planned |
| [COMMON-014](#common-014) | Date filters | I | Planned |
| [COMMON-015](#common-015) | Form persistence and cancellation | I | Planned |
| [COMMON-016](#common-016) | Multilingual text | I | Planned |
| [COMMON-017](#common-017) | Upload and attachment boundaries | I | Planned |
| [COMMON-018](#common-018) | Delete confirmation controls | I | Planned |
| [COMMON-019](#common-019) | Repeated submission and concurrent edits | I | Planned |
| [COMMON-020](#common-020) | Network and service failures | I | Planned |
| [COMMON-021](#common-021) | Keyboard accessibility | I | Planned |
| [COMMON-022](#common-022) | Browser, viewport and zoom | I | Planned |
| [COMMON-023](#common-023) | Response-time measurement | I | Planned |

## Scenarios

### COMMON-001

**Initial navigation to Admin**

**Priority:** P2 · **Design environment:** R · **Role:** Admin · **Automation:** Automated for the specified scenario scope

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Select Admin; verify System Users and Search; return to Dashboard.

**Expected outcome:** The expected route and panel heading appear; returning displays Dashboard.

<details><summary>Implemented variations (1)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_navigation.py::test_module_navigation[chromium-Admin]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | full | Specified scenario scope |

</details>

Implementation metadata is not a fresh passing execution result.

### COMMON-002

**Initial navigation to PIM**

**Priority:** P2 · **Design environment:** R · **Role:** Admin · **Automation:** Automated for the specified scenario scope

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Select PIM; verify Employee Information and Search; return to Dashboard.

**Expected outcome:** The expected route and panel heading appear; returning displays Dashboard.

<details><summary>Implemented variations (1)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_navigation.py::test_module_navigation[chromium-PIM]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | full | Specified scenario scope |

</details>

Implementation metadata is not a fresh passing execution result.

### COMMON-003

**Initial navigation to Directory**

**Priority:** P2 · **Design environment:** R · **Role:** Admin · **Automation:** Automated for the specified scenario scope

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Select Directory; verify the Directory search-panel heading and Search; return to Dashboard.

**Expected outcome:** The expected route and panel heading appear; returning displays Dashboard.

<details><summary>Implemented variations (1)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_navigation.py::test_module_navigation[chromium-Directory]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | full | Specified scenario scope |

</details>

Implementation metadata is not a fresh passing execution result.

### COMMON-004

**Every menu and submenu**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Partially automated; remaining variations are planned

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Open each route in the feature matrix through the menus; inspect its heading, primary content and active navigation state.

**Expected outcome:** The corresponding page opens without unexpected errors, empty screens or incorrect headings; role/version-dependent features are recorded separately.

<details><summary>Implemented variations (62)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-Job Titles]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Job/Job Titles, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-Pay Grades]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Job/Pay Grades, Admin role |
| [`tests/test_navigation.py::test_module_navigation[chromium-Leave]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Leave landing page, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-Employment Status]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Job/Employment Status, Admin role |
| [`tests/test_navigation.py::test_module_navigation[chromium-Time]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Time landing page, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-Job Categories]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Job/Job Categories, Admin role |
| [`tests/test_navigation.py::test_module_navigation[chromium-Recruitment]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Recruitment landing page, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-Work Shifts]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Job/Work Shifts, Admin role |
| [`tests/test_navigation.py::test_module_navigation[chromium-My-Info]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | My Info landing page, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-General Information]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Organization/General Information, Admin role |
| [`tests/test_navigation.py::test_module_navigation[chromium-Performance]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Performance landing page, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-Locations]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Organization/Locations, Admin role |
| [`tests/test_navigation.py::test_module_navigation[chromium-Dashboard]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Dashboard landing page, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-Structure]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Organization/Structure, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-Skills]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Qualifications/Skills, Admin role |
| [`tests/test_navigation.py::test_module_navigation[chromium-Maintenance]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Maintenance landing page, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-Education]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Qualifications/Education, Admin role |
| [`tests/test_navigation.py::test_module_navigation[chromium-Claim]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Claim landing page, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-Licenses]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Qualifications/Licenses, Admin role |
| [`tests/test_navigation.py::test_module_navigation[chromium-Buzz]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Buzz landing page, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-Languages]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Qualifications/Languages, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-Memberships]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Qualifications/Memberships, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-Email Configuration]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Configuration/Email Configuration, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-Email Subscriptions]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Configuration/Email Subscriptions, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-Localization]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Configuration/Localization, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-Language Packages]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Configuration/Language Packages, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-Modules]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Configuration/Modules, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-Social Media Authentication]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Configuration/Social Media Authentication, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-Register OAuth Client]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Configuration/Register OAuth Client, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Admin-LDAP Configuration]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin/Configuration/LDAP Configuration, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-PIM-Optional Fields]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | PIM/Configuration/Optional Fields, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-PIM-Custom Fields]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | PIM/Configuration/Custom Fields, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-PIM-Data Import]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | PIM/Configuration/Data Import, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-PIM-Reporting Methods]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | PIM/Configuration/Reporting Methods, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-PIM-Termination Reasons]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | PIM/Configuration/Termination Reasons, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Leave-Add Entitlements]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Leave/Entitlements/Add Entitlements, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Leave-Employee Entitlements]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Leave/Entitlements/Employee Entitlements, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Leave-My Entitlements]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Leave/Entitlements/My Entitlements, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Leave-Leave Entitlements and Usage Report]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Leave/Reports/Leave Entitlements and Usage Report, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Leave-My Leave Entitlements and Usage Report]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Leave/Reports/My Leave Entitlements and Usage Report, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Leave-Leave Period]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Leave/Configure/Leave Period, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Leave-Leave Types]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Leave/Configure/Leave Types, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Leave-Work Week]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Leave/Configure/Work Week, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Leave-Holidays]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Leave/Configure/Holidays, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Time-My Timesheets]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Time/Timesheets/My Timesheets, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Time-Employee Timesheets]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Time/Timesheets/Employee Timesheets, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Time-My Records]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Time/Attendance/My Records, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Time-Punch In/Out]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Time/Attendance/Punch In/Out, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Time-Employee Records]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Time/Attendance/Employee Records, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Time-Configuration]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Time/Attendance/Configuration, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Time-Project Reports]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Time/Reports/Project Reports, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Time-Employee Reports]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Time/Reports/Employee Reports, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Time-Attendance Summary]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Time/Reports/Attendance Summary, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Time-Customers]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Time/Project Info/Customers, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Time-Projects]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Time/Project Info/Projects, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Performance-KPIs]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Performance/Configure/KPIs, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Performance-Trackers]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Performance/Configure/Trackers, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Performance-Manage Reviews]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Performance/Manage Reviews/Manage Reviews, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Performance-My Reviews]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Performance/Manage Reviews/My Reviews, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Performance-Employee Reviews]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Performance/Manage Reviews/Employee Reviews, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Claim-Events]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Claim/Configuration/Events, Admin role |
| [`tests/test_navigation.py::test_submenu_destination[chromium-Claim-Expense Types]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Claim/Configuration/Expense Types, Admin role |

</details>

Implementation metadata is not a fresh passing execution result.

### COMMON-005

**Sidebar search and collapse**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Partially automated; remaining variations are planned

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Search using a full, partial and nonexistent menu name; clear the search; collapse and expand the sidebar.

**Expected outcome:** Matching menus appear; clearing restores the list; collapsing does not disrupt navigation or the active page.

<details><summary>Implemented variations (3)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_navigation.py::test_sidebar_search_and_clear[chromium-full-name]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | sidebar search/reset, Admin role; collapse not yet covered |
| [`tests/test_navigation.py::test_sidebar_search_and_clear[chromium-partial-name]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | sidebar search/reset, Admin role; collapse not yet covered |
| [`tests/test_navigation.py::test_sidebar_search_and_clear[chromium-no-match]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | sidebar search/reset, Admin role; collapse not yet covered |

</details>

Implementation metadata is not a fresh passing execution result.

### COMMON-006

**Account menu and Help**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Open and close About, Support and Help; inspect the Upgrade destination without changing anything.

**Expected outcome:** The expected destinations and return path work; no unintended configuration change or upgrade occurs.

### COMMON-007

**Individual filters**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Partially automated; remaining variations are planned

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** On every filterable page, apply each filter independently to known matching and nonmatching data.

**Expected outcome:** All and only matching records appear; a clear empty state is shown when nothing matches.

<details><summary>Implemented variations (2)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_navigation.py::test_unknown_filter_has_empty_result[chromium-Admin-Username]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | unknown exact text value in Admin Username / PIM Employee Id |
| [`tests/test_navigation.py::test_unknown_filter_has_empty_result[chromium-PIM-Employee Id]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | unknown exact text value in Admin Username / PIM Employee Id |

</details>

Implementation metadata is not a fresh passing execution result.

### COMMON-008

**Combined filters**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Apply compatible and contradictory pairs and combinations of filters to known data.

**Expected outcome:** Results follow the approved AND/OR contract and exclude records that do not satisfy it.

### COMMON-009

**Reset and return to the list**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Partially automated; remaining variations are planned

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Change filters, Search, Reset, then navigate from a detail page back to the list.

**Expected outcome:** Reset restores defaults; filter/page retention on return follows a documented, consistent policy.

<details><summary>Implemented variations (2)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_navigation.py::test_reset_clears_text_filter[chromium-Admin-Username]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Reset clears one exact text filter, Admin/PIM; list-return retention not covered |
| [`tests/test_navigation.py::test_reset_clears_text_filter[chromium-PIM-Employee Id]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Reset clears one exact text filter, Admin/PIM; list-return retention not covered |

</details>

Implementation metadata is not a fresh passing execution result.

### COMMON-010

**Autocomplete identity selection**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Enter partial, duplicate and unknown names; choose a suggestion; then manually change the input text.

**Expected outcome:** The selected record's ID is used; invalid free text cannot silently target another record.

### COMMON-011

**Sorting**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Sort supported columns ascending/descending; inspect ties and results spanning several pages.

**Expected outcome:** Ordering respects the data type and remains consistent across pages; the direction indicator is correct.

### COMMON-012

**Pagination**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Use known data spanning multiple pages; visit first/middle/last pages; filter and delete the last record on a page.

**Expected outcome:** Records are not unintentionally skipped or repeated; page numbers and counts remain valid after changes.

### COMMON-013

**Single and bulk selection**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Select row/header checkboxes; clear selection; change pages and filters; cancel and confirm bulk deletion in isolation.

**Expected outcome:** Only actually selected IDs are affected; cross-page selection policy is clear; partial errors and successes are reported unambiguously.

### COMMON-014

**Date filters**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Test equal/reversed/empty/invalid ranges, month ends and leap days using the calendar and manual typing.

**Expected outcome:** Valid ranges include the correct records; invalid values are rejected; display/storage follow localization settings.

### COMMON-015

**Form persistence and cancellation**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** In each Save form, test valid/invalid input, Cancel, Back and Reload.

**Expected outcome:** Only a successful save changes data; errors retain valid input; handling of unsaved changes is clear.

### COMMON-016

**Multilingual text**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Store Persian/English text, symbols, emoji and multiline content in fields that permit them.

**Expected outcome:** Content is stored/displayed intact and treated as text without executing scripts.

### COMMON-017

**Upload and attachment boundaries**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** For every upload, test allowed/disallowed types, empty files, size limits and one size above, duplicate names and mismatched content/extensions.

**Expected outcome:** The page's actual limits are enforced; errors are clear; valid files download intact; invalid uploads cannot execute active content.

### COMMON-018

**Delete confirmation controls**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** For each delete feature, separately test Cancel, Close, Escape and Confirm.

**Expected outcome:** Cancellation preserves the record; confirmation affects only the intended target; references remain consistent.

### COMMON-019

**Repeated submission and concurrent edits**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Double-click Save; edit the same record from two accounts; reload afterward.

**Expected outcome:** Unintended duplicates/deletions do not occur; conflicts follow the contract and produce a clear final outcome.

### COMMON-020

**Network and service failures**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** In a controlled environment, inject disconnection, delay and 401/403/404/500 responses during reads/saves; retry.

**Expected outcome:** Loading ends, errors are understandable, false success is avoided and retry does not duplicate data. Fault injection is not evidence of live backend correctness.

### COMMON-021

**Keyboard accessibility**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Use only Tab/Shift+Tab/Enter/Escape with forms, dropdowns, dialogs and calendars.

**Expected outcome:** Focus and ordering are clear; labels/errors are understandable to assistive technology; closing a dialog restores focus.

### COMMON-022

**Browser, viewport and zoom**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Inspect forms/tables in Chrome and Firefox, desktop/narrow viewports and 200% zoom.

**Expected outcome:** Core data/actions remain accessible without overlap or clipping; record explicitly if mobile behavior is outside scope.

### COMMON-023

**Response-time measurement**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Repeatedly measure loading, filtering and saving with known data and a stable network.

**Expected outcome:** Record timing and error rates; without an approved SLA, report measurements rather than a performance Pass/Fail claim.

[Back to scenario index](#scenario-index) | [Back to plan overview](README.md)
