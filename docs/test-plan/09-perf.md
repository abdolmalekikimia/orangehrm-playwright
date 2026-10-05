# Performance management

**19 scenarios | 0 automated | 19 planned**

[Plan overview](README.md) | [CSV catalog](scenario-catalog.csv) | [JSON catalog](scenario-catalog.json)

## Scope

KPIs; Trackers; Manage/My/Employee Reviews; My/Employee Trackers and logs.

## Default prerequisites

Authorized account and synthetic fixtures owned by this run.

Shared controls and evidence rules in [COMMON](02-common.md) and the [overview](README.md) also apply. Environment codes: R = read-only demo, I = isolated instance, D = disposable instance.

## Scenario index

| ID | Scenario | Environment | Automation status |
|---|---|---|---|
| [PERF-001](#perf-001) | KPIs: Create and persist | I | Planned |
| [PERF-002](#perf-002) | KPIs: Required fields and boundaries | I | Planned |
| [PERF-003](#perf-003) | KPIs: Duplicates and normalization | I | Planned |
| [PERF-004](#perf-004) | KPIs: Edit and cancel | I | Planned |
| [PERF-005](#perf-005) | KPIs: Delete and dependencies | I | Planned |
| [PERF-006](#perf-006) | Trackers: Create and persist | I | Planned |
| [PERF-007](#perf-007) | Trackers: Required fields and boundaries | I | Planned |
| [PERF-008](#perf-008) | Trackers: Duplicates and normalization | I | Planned |
| [PERF-009](#perf-009) | Trackers: Edit and cancel | I | Planned |
| [PERF-010](#perf-010) | Trackers: Delete and dependencies | I | Planned |
| [PERF-011](#perf-011) | Manage Reviews: create | I | Planned |
| [PERF-012](#perf-012) | Review: invalid dates and references | I | Planned |
| [PERF-013](#perf-013) | Review: activate and edit | I | Planned |
| [PERF-014](#perf-014) | My Reviews: self review | I | Planned |
| [PERF-015](#perf-015) | Review: rating boundaries and mandatory input | I | Planned |
| [PERF-016](#perf-016) | Employee Reviews: supervisor evaluation | I | Planned |
| [PERF-017](#perf-017) | Review filters | I | Planned |
| [PERF-018](#perf-018) | Tracker Logs | I | Planned |
| [PERF-019](#perf-019) | My Trackers and Employee Trackers | I | Planned |

## Scenarios

### PERF-001

**KPIs: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete Job Title, indicator name, Minimum/Maximum Rating and available Default option with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. Minimum must not exceed maximum; the indicator belongs to the correct job title.

### PERF-002

**KPIs: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For Job Title, indicator name, Minimum/Maximum Rating and available Default option, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. Minimum must not exceed maximum; the indicator belongs to the correct job title.

### PERF-003

**KPIs: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same KPIs key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. Minimum must not exceed maximum; the indicator belongs to the correct job title.

### PERF-004

**KPIs: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. Minimum must not exceed maximum; the indicator belongs to the correct job title.

### PERF-005

**KPIs: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a KPI referenced by an existing review in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### PERF-006

**Trackers: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete name, Employee and Reviewers with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. Employee/reviewer identities are valid; access is limited to authorized participants.

### PERF-007

**Trackers: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For name, Employee and Reviewers, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. Employee/reviewer identities are valid; access is limited to authorized participants.

### PERF-008

**Trackers: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Trackers key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. Employee/reviewer identities are valid; access is limited to authorized participants.

### PERF-009

**Trackers: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. Employee/reviewer identities are valid; access is limited to authorized participants.

### PERF-010

**Trackers: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a tracker with reviewers or existing logs in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### PERF-011

**Manage Reviews: create**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Enter Employee, Supervisor, Review Period and Due Date; save a draft.

**Expected outcome:** People/dates are correct; KPIs follow the job; the draft appears in the proper list.

### PERF-012

**Review: invalid dates and references**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Test reversed dates, inconsistent due dates, unknown reviewers and duplicate periods.

**Expected outcome:** Period/duplicate rules follow the contract; errors are clear; no incomplete review is created.

### PERF-013

**Review: activate and edit**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit/activate a draft; attempt edit/delete after activation.

**Expected outcome:** Only stage-appropriate operations succeed; assigned reviewers can access it; saved data/period remain correct.

### PERF-014

**My Reviews: self review**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** As ESS, enter valid ratings/comments; Save Draft and Submit.

**Expected outcome:** Only own reviews are accessible; draft values persist; submission and edit restrictions follow the workflow.

### PERF-015

**Review: rating boundaries and mandatory input**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Test values below/above/exactly at KPI limits, empty/text ratings and long comments.

**Expected outcome:** Valid boundaries pass; invalid input fails without losing valid ratings.

### PERF-016

**Employee Reviews: supervisor evaluation**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** An authorized manager evaluates/submits/finalizes reviews for scoped employees using supported actions.

**Expected outcome:** Ratings/comments have the correct author; transitions are legal; employees outside scope remain inaccessible.

### PERF-017

**Review filters**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Apply Employee, Job Title, Sub Unit, Include, Review Status and From/To.

**Expected outcome:** Results match fixtures; Past/Current, Reset and empty states are correct.

### PERF-018

**Tracker Logs**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Authorized reviewer adds positive/negative logs and comments; edit/delete and Cancel.

**Expected outcome:** Logs belong to the correct tracker/employee; author/time are accurate; others cannot edit without permission.

### PERF-019

**My Trackers and Employee Trackers**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Inspect the same tracker/logs as ESS and supervisor; attempt out-of-scope access.

**Expected outcome:** Only authorized trackers appear; shared data agrees; direct URLs do not expand access.

[Back to scenario index](#scenario-index) | [Back to plan overview](README.md)
