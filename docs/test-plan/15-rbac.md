# Authorization and cross-module integrity

**10 scenarios | 0 automated | 10 planned**

[Plan overview](README.md) | [CSV catalog](scenario-catalog.csv) | [JSON catalog](scenario-catalog.json)

## Scope

Admin/ESS/Supervisor permissions; page and operation access; linked workflows and reports.

## Default prerequisites

Independent synthetic accounts and an approved authorization policy; the public Admin account alone cannot establish RBAC coverage.

Shared controls and evidence rules in [COMMON](02-common.md) and the [overview](README.md) also apply. Environment codes: R = read-only demo, I = isolated instance, D = disposable instance.

## Scenario index

| ID | Scenario | Environment | Automation status |
|---|---|---|---|
| [RBAC-001](#rbac-001) | Page and operation authorization | I | Planned |
| [RBAC-002](#rbac-002) | Another employee's ID | I | Planned |
| [RBAC-003](#rbac-003) | Role and supervisor changes | I | Planned |
| [RBAC-004](#rbac-004) | Employee-to-Directory workflow | I | Planned |
| [RBAC-005](#rbac-005) | Leave-to-Dashboard workflow | I | Planned |
| [RBAC-006](#rbac-006) | Project-to-Report workflow | I | Planned |
| [RBAC-007](#rbac-007) | Recruitment-to-Employee workflow | I | Planned |
| [RBAC-008](#rbac-008) | Claim-to-Decision workflow | I | Planned |
| [RBAC-009](#rbac-009) | Termination across modules | I | Planned |
| [RBAC-010](#rbac-010) | Master-data integrity | I | Planned |

## Scenarios

### RBAC-001

**Page and operation authorization**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Independent synthetic accounts and an approved authorization policy; the public Admin account alone cannot establish RBAC coverage.

**Steps / test data:** For each matrix route, use allowed/disallowed roles, direct URLs and its Save/Delete/Download operations.

**Expected outcome:** UI and operation processing enforce the same policy; no out-of-scope read/write access succeeds.

### RBAC-002

**Another employee's ID**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Independent synthetic accounts and an approved authorization policy; the public Admin account alone cannot establish RBAC coverage.

**Steps / test data:** As ESS/a scoped manager, use known out-of-scope employee/claim/review/leave IDs in test routes.

**Expected outcome:** Horizontal access is denied; no confidential data is returned and no other employee's record changes.

### RBAC-003

**Role and supervisor changes**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Independent synthetic accounts and an approved authorization policy; the public Admin account alone cannot establish RBAC coverage.

**Steps / test data:** Change a fixture's role/supervisor relationship; inspect old/new sessions and direct routes.

**Expected outcome:** New permissions take effect according to timing policy; previous access does not remain without justification.

### RBAC-004

**Employee-to-Directory workflow**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Independent synthetic accounts and an approved authorization policy; the public Admin account alone cannot establish RBAC coverage.

**Steps / test data:** Create employee/user, set Job/Location/Unit/Contact; sign in as ESS; inspect Directory and PIM filters.

**Expected outcome:** IDs/data agree across views; ESS access remains scoped; cleanup preserves relationship consistency.

### RBAC-005

**Leave-to-Dashboard workflow**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Independent synthetic accounts and an approved authorization policy; the public Admin account alone cannot establish RBAC coverage.

**Steps / test data:** Configure entitlement, apply, approve, report and inspect My Leave/Leave Today; cancel where permitted.

**Expected outcome:** Duration/status/balance/widgets reflect one consistent event history without duplicate usage or stale balances.

### RBAC-006

**Project-to-Report workflow**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Independent synthetic accounts and an approved authorization policy; the public Admin account alone cannot establish RBAC coverage.

**Steps / test data:** Create customer/project/activity; record/submit/approve hours; inspect project/employee reports.

**Expected outcome:** References, hours, statuses and totals agree; deleting historical references does not corrupt data.

### RBAC-007

**Recruitment-to-Employee workflow**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Independent synthetic accounts and an approved authorization policy; the public Admin account alone cannot establish RBAC coverage.

**Steps / test data:** Create vacancy/candidate and follow synthetic hiring; convert only if the version actually supports it.

**Expected outcome:** Status/history are correct; conversion creates only one correctly linked employee; unsupported conversion is N/A, not a product failure.

### RBAC-008

**Claim-to-Decision workflow**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Independent synthetic accounts and an approved authorization policy; the public Admin account alone cannot establish RBAC coverage.

**Steps / test data:** Create event/type, draft, expenses/receipts; submit and approve/reject; inspect My/Employee Claims.

**Expected outcome:** Owner/reference/amount/status agree; attachments belong to the right person; unauthorized decisions are rejected.

### RBAC-009

**Termination across modules**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Independent synthetic accounts and an approved authorization policy; the public Admin account alone cannot establish RBAC coverage.

**Steps / test data:** Terminate a fixture; inspect PIM Include, Directory, Leave/Time/Claim and the employee's login.

**Expected outcome:** Current/history visibility and access follow approved policy; retained history remains reportable; assumptions do not replace requirements.

### RBAC-010

**Master-data integrity**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Independent synthetic accounts and an approved authorization policy; the public Admin account alone cannot establish RBAC coverage.

**Steps / test data:** Rename/disable/delete title/location/leave type/skill fixtures; inspect related profiles and historical records.

**Expected outcome:** References/display remain consistent; no orphan records or silently changed historical meaning result.

[Back to scenario index](#scenario-index) | [Back to plan overview](README.md)
