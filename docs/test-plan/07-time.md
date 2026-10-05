# Time and attendance

**26 scenarios | 0 automated | 26 planned**

[Plan overview](README.md) | [CSV catalog](scenario-catalog.csv) | [JSON catalog](scenario-catalog.json)

## Scope

My/Employee Timesheets; My Records; Punch In/Out; Employee Records; Attendance Configuration; Project/Employee Reports; Attendance Summary; Customers; Projects/Activities.

## Default prerequisites

Authorized account and synthetic fixtures owned by this run.

Shared controls and evidence rules in [COMMON](02-common.md) and the [overview](README.md) also apply. Environment codes: R = read-only demo, I = isolated instance, D = disposable instance.

## Scenario index

| ID | Scenario | Environment | Automation status |
|---|---|---|---|
| [TIME-001](#time-001) | Customers: Create and persist | I | Planned |
| [TIME-002](#time-002) | Customers: Required fields and boundaries | I | Planned |
| [TIME-003](#time-003) | Customers: Duplicates and normalization | I | Planned |
| [TIME-004](#time-004) | Customers: Edit and cancel | I | Planned |
| [TIME-005](#time-005) | Customers: Delete and dependencies | I | Planned |
| [TIME-006](#time-006) | Projects: Create and persist | I | Planned |
| [TIME-007](#time-007) | Projects: Required fields and boundaries | I | Planned |
| [TIME-008](#time-008) | Projects: Duplicates and normalization | I | Planned |
| [TIME-009](#time-009) | Projects: Edit and cancel | I | Planned |
| [TIME-010](#time-010) | Projects: Delete and dependencies | I | Planned |
| [TIME-011](#time-011) | Project Activities | I | Planned |
| [TIME-012](#time-012) | My Timesheets: week selection | I | Planned |
| [TIME-013](#time-013) | Timesheet: record hours | I | Planned |
| [TIME-014](#time-014) | Timesheet: hour boundaries | I | Planned |
| [TIME-015](#time-015) | Timesheet: row edits | I | Planned |
| [TIME-016](#time-016) | Timesheet: submit | I | Planned |
| [TIME-017](#time-017) | Employee Timesheets | I | Planned |
| [TIME-018](#time-018) | Timesheet: approve and reject | I | Planned |
| [TIME-019](#time-019) | Punch In/Out lifecycle | I | Planned |
| [TIME-020](#time-020) | Punch: invalid states and time boundaries | I | Planned |
| [TIME-021](#time-021) | Attendance: edit and delete | I | Planned |
| [TIME-022](#time-022) | Attendance Configuration | I | Planned |
| [TIME-023](#time-023) | My Records and Employee Records | I | Planned |
| [TIME-024](#time-024) | Project Reports | I | Planned |
| [TIME-025](#time-025) | Employee Reports | I | Planned |
| [TIME-026](#time-026) | Attendance Summary | I | Planned |

## Scenarios

### TIME-001

**Customers: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete name, description and fields exposed by the form with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. The customer is available in Projects; deletion respects project dependencies.

### TIME-002

**Customers: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For name, description and fields exposed by the form, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. The customer is available in Projects; deletion respects project dependencies.

### TIME-003

**Customers: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Customers key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. The customer is available in Projects; deletion respects project dependencies.

### TIME-004

**Customers: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. The customer is available in Projects; deletion respects project dependencies.

### TIME-005

**Customers: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a customer with an active project in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### TIME-006

**Projects: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete name, Customer, Project Admin and description with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. Customer/admin identities are valid; the project is available in timesheets.

### TIME-007

**Projects: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For name, Customer, Project Admin and description, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. Customer/admin identities are valid; the project is available in timesheets.

### TIME-008

**Projects: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Projects key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. Customer/admin identities are valid; the project is available in timesheets.

### TIME-009

**Projects: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. Customer/admin identities are valid; the project is available in timesheets.

### TIME-010

**Projects: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a project with activities or recorded time in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### TIME-011

**Project Activities**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Add/edit/delete activities; test duplicate names and copying from another project where supported.

**Expected outcome:** Activities belong to the correct project; deleting an in-use activity does not corrupt time history.

### TIME-012

**My Timesheets: week selection**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Select current/previous/next weeks; create existing/new periods and refresh.

**Expected outcome:** The correct period opens without duplicate timesheets; dates follow localization.

### TIME-013

**Timesheet: record hours**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Enter project/activity, daily hours and comments across multiple rows; Save and total.

**Expected outcome:** Daily/weekly sums and project/activity links are correct; values persist after returning.

### TIME-014

**Timesheet: hour boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Test empty/zero/negative/text values, decimal boundaries, hh:mm and values above the stated daily limit.

**Expected outcome:** Formats/precision follow the contract; invalid input is rejected; rounded values agree with reports.

### TIME-015

**Timesheet: row edits**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Add/delete rows; use duplicate activities; Cancel; inspect inactive/deleted projects.

**Expected outcome:** Cancellation preserves data; duplicates follow policy; historical records with deleted references remain explainable.

### TIME-016

**Timesheet: submit**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Submit a Draft, an incomplete sheet and a repeated submission; attempt edits after submission.

**Expected outcome:** Legal transitions and completeness rules apply; only permitted actions remain available; repetition has no extra effect.

### TIME-017

**Employee Timesheets**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Select valid, free-text and same-name employees; use View and inspect Pending Action.

**Expected outcome:** The intended employee's periods appear; access is limited to authorized managers; pending items match statuses.

### TIME-018

**Timesheet: approve and reject**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Manager approves/rejects a submitted sheet and adds comments; ESS corrects and resubmits.

**Expected outcome:** Draft/Submitted/Approved/Rejected transitions follow this version; history/reports agree; illegal transitions are rejected.

### TIME-019

**Punch In/Out lifecycle**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Punch In and Out for a fixture at known times; inspect My Records and Dashboard.

**Expected outcome:** One interval has the correct duration; buttons and time displays remain consistent.

### TIME-020

**Punch: invalid states and time boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Test repeated In without Out, Out without In, reversed times, midnight crossing and timezone changes.

**Expected outcome:** Invalid states are rejected; duration follows configured time/zone rules; no duplicate attendance record is created.

### TIME-021

**Attendance: edit and delete**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit/delete a fixture using an authorized role; test restricted roles, required fields and Cancel.

**Expected outcome:** Configuration permissions apply; modified records and totals remain consistent.

### TIME-022

**Attendance Configuration**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Change ESS/supervisor editing permissions in isolation; attempt direct-route access.

**Expected outcome:** UI and backend enforce the new policy; hidden routes do not preserve unauthorized access.

### TIME-023

**My Records and Employee Records**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Search known dates, employees and attendance periods; test empty/multiple results and invalid dates.

**Expected outcome:** Records/durations are correct; My shows only self; Employee shows only the authorized scope.

### TIME-024

**Project Reports**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Filter project/activity/date range and available status options; compare with known hours.

**Expected outcome:** Activity/project totals are correct; selected status policy determines which sheets count.

### TIME-025

**Employee Reports**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Filter an employee/period containing hours across projects and statuses.

**Expected outcome:** Employee totals match the underlying hours according to report policy; ESS cannot access others' data.

### TIME-026

**Attendance Summary**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Use fixtures with known intervals, boundary dates, no records and midnight crossing.

**Expected outcome:** Totals match attendance records; empty behavior is clear; rounding/timezone rules are consistent.

[Back to scenario index](#scenario-index) | [Back to plan overview](README.md)
