# Leave management

**28 scenarios | 0 automated | 28 planned**

[Plan overview](README.md) | [CSV catalog](scenario-catalog.csv) | [JSON catalog](scenario-catalog.json)

## Scope

Apply; My Leave; Add/Employee/My Entitlements; employee/self usage reports; Leave Period; Leave Types; Work Week; Holidays; Leave List; Assign Leave.

## Default prerequisites

Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

Shared controls and evidence rules in [COMMON](02-common.md) and the [overview](README.md) also apply. Environment codes: R = read-only demo, I = isolated instance, D = disposable instance.

## Scenario index

| ID | Scenario | Environment | Automation status |
|---|---|---|---|
| [LEAVE-001](#leave-001) | Leave Types: Create and persist | I | Planned |
| [LEAVE-002](#leave-002) | Leave Types: Required fields and boundaries | I | Planned |
| [LEAVE-003](#leave-003) | Leave Types: Duplicates and normalization | I | Planned |
| [LEAVE-004](#leave-004) | Leave Types: Edit and cancel | I | Planned |
| [LEAVE-005](#leave-005) | Leave Types: Delete and dependencies | I | Planned |
| [LEAVE-006](#leave-006) | Holidays: Create and persist | I | Planned |
| [LEAVE-007](#leave-007) | Holidays: Required fields and boundaries | I | Planned |
| [LEAVE-008](#leave-008) | Holidays: Duplicates and normalization | I | Planned |
| [LEAVE-009](#leave-009) | Holidays: Edit and cancel | I | Planned |
| [LEAVE-010](#leave-010) | Holidays: Delete and dependencies | I | Planned |
| [LEAVE-011](#leave-011) | Leave Period | I | Planned |
| [LEAVE-012](#leave-012) | Work Week | I | Planned |
| [LEAVE-013](#leave-013) | Add Entitlements: individual | I | Planned |
| [LEAVE-014](#leave-014) | Add Entitlements: group | I | Planned |
| [LEAVE-015](#leave-015) | Entitlements: invalid values and changes | I | Planned |
| [LEAVE-016](#leave-016) | Apply: one full day | I | Planned |
| [LEAVE-017](#leave-017) | Apply: multiple days and holidays | I | Planned |
| [LEAVE-018](#leave-018) | Apply: partial days | I | Planned |
| [LEAVE-019](#leave-019) | Apply: balance boundaries | I | Planned |
| [LEAVE-020](#leave-020) | Apply: dates and overlap | I | Planned |
| [LEAVE-021](#leave-021) | My Leave: filters and cancellation | I | Planned |
| [LEAVE-022](#leave-022) | Leave List: all filters | I | Planned |
| [LEAVE-023](#leave-023) | Leave List: approve and reject | I | Planned |
| [LEAVE-024](#leave-024) | Leave List: bulk action | I | Planned |
| [LEAVE-025](#leave-025) | Assign Leave | I | Planned |
| [LEAVE-026](#leave-026) | Comments and daily details | I | Planned |
| [LEAVE-027](#leave-027) | Employee Entitlements and Usage Report | I | Planned |
| [LEAVE-028](#leave-028) | My Entitlements and Usage Report | I | Planned |

## Scenarios

### LEAVE-001

**Leave Types: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Open Add; complete type name and available entitlement-related options with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. The active type is available in Apply/Assign and reports.

### LEAVE-002

**Leave Types: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** For type name and available entitlement-related options, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. The active type is available in Apply/Assign and reports.

### LEAVE-003

**Leave Types: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Reuse the same Leave Types key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. The active type is available in Apply/Assign and reports.

### LEAVE-004

**Leave Types: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. The active type is available in Apply/Assign and reports.

### LEAVE-005

**Leave Types: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a leave type with entitlement or request history in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### LEAVE-006

**Holidays: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Open Add; complete name, date and available full/half-day/recurrence options with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. The holiday affects leave duration for the correct year/day.

### LEAVE-007

**Holidays: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** For name, date and available full/half-day/recurrence options, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. The holiday affects leave duration for the correct year/day.

### LEAVE-008

**Holidays: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Reuse the same Holidays key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. The holiday affects leave duration for the correct year/day.

### LEAVE-009

**Holidays: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. The holiday affects leave duration for the correct year/day.

### LEAVE-010

**Holidays: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a holiday affecting existing leave calculations in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### LEAVE-011

**Leave Period**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Change the period start; inspect calculated periods; test year boundaries and invalid days.

**Expected outcome:** Periods follow policy without unintended gaps/overlaps; entitlements/reports use the same period.

### LEAVE-012

**Work Week**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Configure working/nonworking/half days; request leave spanning all three.

**Expected outcome:** Duration uses the configured work calendar and half days; report calculations use the same basis.

### LEAVE-013

**Add Entitlements: individual**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Select employee, type, period and a valid amount; Save; inspect Employee/My Entitlements.

**Expected outcome:** Entitlement is credited to the correct employee/type/period; balances follow totals and usage.

### LEAVE-014

**Add Entitlements: group**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Select supported employee/unit/location groups; preview the scope and save in isolation.

**Expected outcome:** Only eligible employees receive the correct amounts; repeated submission does not duplicate credits.

### LEAVE-015

**Entitlements: invalid values and changes**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Test empty/negative/text/decimal amounts, unknown employees and invalid periods; edit/delete used entitlement.

**Expected outcome:** Amount and usage-dependency policies are enforced; balances/history cannot be corrupted without an explicit policy.

### LEAVE-016

**Apply: one full day**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Choose a type with enough balance and one working day; Apply; inspect My Leave.

**Expected outcome:** One request has the correct duration/status; balance treatment follows the approved Pending/Approved policy.

### LEAVE-017

**Apply: multiple days and holidays**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Request a range spanning weekends, holidays and a half day; compare with the known calendar.

**Expected outcome:** Chargeable duration is accurate; nonworking days do not incorrectly consume entitlement.

### LEAVE-018

**Apply: partial days**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Test Half Day/Specify Time where available, morning/afternoon, equal/reversed times and multiday requests.

**Expected outcome:** Duration is correct; invalid times are rejected; partial-day choices apply only as defined by the form.

### LEAVE-019

**Apply: balance boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Test no entitlement, zero balance, exactly sufficient balance and an amount above balance.

**Expected outcome:** Equal/exceeded boundaries follow policy; errors are clear; rejected requests do not consume entitlement.

### LEAVE-020

**Apply: dates and overlap**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Test reversed/out-of-period/past ranges and overlapping requests including a shared boundary day.

**Expected outcome:** Approved period/past-date rules apply; prohibited overlaps are rejected without creating hidden requests.

### LEAVE-021

**My Leave: filters and cancellation**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Filter by available status/type/date; cancel owned requests at different workflow stages.

**Expected outcome:** Only the employee's requests appear; only eligible states can be canceled; balances/manager views remain consistent.

### LEAVE-022

**Leave List: all filters**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Use From/To, multiple Status values, Leave Type, Employee, Sub Unit and Include Past Employees.

**Expected outcome:** Filters/multiselect work; date/required validation applies; supervisors see only authorized employees.

### LEAVE-023

**Leave List: approve and reject**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** An authorized manager approves one Pending request and rejects another; add comments where supported.

**Expected outcome:** Only legal transitions occur; history/balance are correct; repeated processing does not consume entitlement twice.

### LEAVE-024

**Leave List: bulk action**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Select synthetic requests with matching/mixed statuses; cancel/confirm bulk actions.

**Expected outcome:** Only selected eligible requests change; partial errors and successful counts are clear.

### LEAVE-025

**Assign Leave**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Assign leave for a fixture with sufficient/insufficient balance; test comments and partial-day ranges.

**Expected outcome:** Employee/duration are correct; warning overrides follow policy; results appear in that employee's My Leave and reports.

### LEAVE-026

**Comments and daily details**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Open a multiday request; inspect/add permitted comments and per-day details; attempt access with an unauthorized account.

**Expected outcome:** Dates/duration/authors are correct; text is safe; unauthorized reads/changes are rejected.

### LEAVE-027

**Employee Entitlements and Usage Report**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** Filter employee/type/period/unit; compare with known entitlements and requests.

**Expected outcome:** Entitled/used/balance follow actual events and approved rounding; empty results are clear.

### LEAVE-028

**My Entitlements and Usage Report**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Test employee/supervisor, leave type, period, entitlements and a known work calendar; mutations occur only in isolation.

**Steps / test data:** As ESS, report the same period and compare with the Admin report for that employee.

**Expected outcome:** Totals agree; ESS cannot obtain other employees' data; test exports only if the version exposes them.

[Back to scenario index](#scenario-index) | [Back to plan overview](README.md)
