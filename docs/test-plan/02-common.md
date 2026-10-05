# Shared controls and navigation

**23 scenarios | 3 automated | 20 planned**

[Plan overview](README.md) | [CSV catalog](scenario-catalog.csv) | [JSON catalog](scenario-catalog.json)

## Scope

Apply these checks separately to every relevant page in the matrix; one example is not evidence for all pages.

## Default prerequisites

Authorized account; known fixtures in isolation for deterministic filtering comparisons.

Shared controls and evidence rules in [COMMON](02-common.md) and the [overview](README.md) also apply. Environment codes: R = read-only demo, I = isolated instance, D = disposable instance.

## Scenario index

| ID | Scenario | Environment | Automation status |
|---|---|---|---|
| [COMMON-001](#common-001) | Initial navigation to Admin | R | Automated |
| [COMMON-002](#common-002) | Initial navigation to PIM | R | Automated |
| [COMMON-003](#common-003) | Initial navigation to Directory | R | Automated |
| [COMMON-004](#common-004) | Every menu and submenu | I | Planned |
| [COMMON-005](#common-005) | Sidebar search and collapse | I | Planned |
| [COMMON-006](#common-006) | Account menu and Help | I | Planned |
| [COMMON-007](#common-007) | Individual filters | I | Planned |
| [COMMON-008](#common-008) | Combined filters | I | Planned |
| [COMMON-009](#common-009) | Reset and return to the list | I | Planned |
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

**Priority:** P2 · **Environment:** R · **Role:** Admin · **Automation:** Implemented in current source

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Select Admin; verify System Users and Search; return to Dashboard.

**Expected outcome:** The expected route and panel heading appear; returning displays Dashboard.

**Existing test reference:** `tests/test_navigation.py::test_module_navigation[chromium-Admin-/admin/viewSystemUsers-System Users]`

### COMMON-002

**Initial navigation to PIM**

**Priority:** P2 · **Environment:** R · **Role:** Admin · **Automation:** Implemented in current source

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Select PIM; verify Employee Information and Search; return to Dashboard.

**Expected outcome:** The expected route and panel heading appear; returning displays Dashboard.

**Existing test reference:** `tests/test_navigation.py::test_module_navigation[chromium-PIM-/pim/viewEmployeeList-Employee Information]`

### COMMON-003

**Initial navigation to Directory**

**Priority:** P2 · **Environment:** R · **Role:** Admin · **Automation:** Implemented in current source

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Select Directory; verify the Directory search-panel heading and Search; return to Dashboard.

**Expected outcome:** The expected route and panel heading appear; returning displays Dashboard.

**Existing test reference:** `tests/test_navigation.py::test_module_navigation[chromium-Directory-/directory/viewDirectory-Directory]`

### COMMON-004

**Every menu and submenu**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Open each route in the feature matrix through the menus; inspect its heading, primary content and active navigation state.

**Expected outcome:** The corresponding page opens without unexpected errors, empty screens or incorrect headings; role/version-dependent features are recorded separately.

### COMMON-005

**Sidebar search and collapse**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Search using a full, partial and nonexistent menu name; clear the search; collapse and expand the sidebar.

**Expected outcome:** Matching menus appear; clearing restores the list; collapsing does not disrupt navigation or the active page.

### COMMON-006

**Account menu and Help**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Open and close About, Support and Help; inspect the Upgrade destination without changing anything.

**Expected outcome:** The expected destinations and return path work; no unintended configuration change or upgrade occurs.

### COMMON-007

**Individual filters**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** On every filterable page, apply each filter independently to known matching and nonmatching data.

**Expected outcome:** All and only matching records appear; a clear empty state is shown when nothing matches.

### COMMON-008

**Combined filters**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Apply compatible and contradictory pairs and combinations of filters to known data.

**Expected outcome:** Results follow the approved AND/OR contract and exclude records that do not satisfy it.

### COMMON-009

**Reset and return to the list**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Change filters, Search, Reset, then navigate from a detail page back to the list.

**Expected outcome:** Reset restores defaults; filter/page retention on return follows a documented, consistent policy.

### COMMON-010

**Autocomplete identity selection**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Enter partial, duplicate and unknown names; choose a suggestion; then manually change the input text.

**Expected outcome:** The selected record's ID is used; invalid free text cannot silently target another record.

### COMMON-011

**Sorting**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Sort supported columns ascending/descending; inspect ties and results spanning several pages.

**Expected outcome:** Ordering respects the data type and remains consistent across pages; the direction indicator is correct.

### COMMON-012

**Pagination**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Use known data spanning multiple pages; visit first/middle/last pages; filter and delete the last record on a page.

**Expected outcome:** Records are not unintentionally skipped or repeated; page numbers and counts remain valid after changes.

### COMMON-013

**Single and bulk selection**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Select row/header checkboxes; clear selection; change pages and filters; cancel and confirm bulk deletion in isolation.

**Expected outcome:** Only actually selected IDs are affected; cross-page selection policy is clear; partial errors and successes are reported unambiguously.

### COMMON-014

**Date filters**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Test equal/reversed/empty/invalid ranges, month ends and leap days using the calendar and manual typing.

**Expected outcome:** Valid ranges include the correct records; invalid values are rejected; display/storage follow localization settings.

### COMMON-015

**Form persistence and cancellation**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** In each Save form, test valid/invalid input, Cancel, Back and Reload.

**Expected outcome:** Only a successful save changes data; errors retain valid input; handling of unsaved changes is clear.

### COMMON-016

**Multilingual text**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Store Persian/English text, symbols, emoji and multiline content in fields that permit them.

**Expected outcome:** Content is stored/displayed intact and treated as text without executing scripts.

### COMMON-017

**Upload and attachment boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** For every upload, test allowed/disallowed types, empty files, size limits and one size above, duplicate names and mismatched content/extensions.

**Expected outcome:** The page's actual limits are enforced; errors are clear; valid files download intact; invalid uploads cannot execute active content.

### COMMON-018

**Delete confirmation controls**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** For each delete feature, separately test Cancel, Close, Escape and Confirm.

**Expected outcome:** Cancellation preserves the record; confirmation affects only the intended target; references remain consistent.

### COMMON-019

**Repeated submission and concurrent edits**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Double-click Save; edit the same record from two accounts; reload afterward.

**Expected outcome:** Unintended duplicates/deletions do not occur; conflicts follow the contract and produce a clear final outcome.

### COMMON-020

**Network and service failures**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** In a controlled environment, inject disconnection, delay and 401/403/404/500 responses during reads/saves; retry.

**Expected outcome:** Loading ends, errors are understandable, false success is avoided and retry does not duplicate data. Fault injection is not evidence of live backend correctness.

### COMMON-021

**Keyboard accessibility**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Use only Tab/Shift+Tab/Enter/Escape with forms, dropdowns, dialogs and calendars.

**Expected outcome:** Focus and ordering are clear; labels/errors are understandable to assistive technology; closing a dialog restores focus.

### COMMON-022

**Browser, viewport and zoom**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Inspect forms/tables in Chrome and Firefox, desktop/narrow viewports and 200% zoom.

**Expected outcome:** Core data/actions remain accessible without overlap or clipping; record explicitly if mobile behavior is outside scope.

### COMMON-023

**Response-time measurement**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account; known fixtures in isolation for deterministic filtering comparisons.

**Steps / test data:** Repeatedly measure loading, filtering and saving with known data and a stable network.

**Expected outcome:** Record timing and error rates; without an approved SLA, report measurements rather than a performance Pass/Fail claim.

[Back to scenario index](#scenario-index) | [Back to plan overview](README.md)
