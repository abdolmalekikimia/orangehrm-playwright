# PIM: employees and configuration

**24 scenarios | 0 automated | 0 partial | 24 planned**

[Plan overview](README.md) | [CSV catalog](scenario-catalog.csv) | [JSON catalog](scenario-catalog.json)

## Scope

Employee List; Add Employee; Reports; Optional Fields; Custom Fields; Data Import; Reporting Methods; Termination Reasons.

## Default prerequisites

Authorized account and synthetic fixtures owned by this run.

Shared controls and [evidence rules](README.md) also apply. R = read-only public demo; I = isolated instance; D = disposable instance. Partial implementations run only their documented public-demo variation, not the complete I/D workflow.

## Scenario index

| ID | Scenario | Design environment | Implementation status |
|---|---|---|---|
| [PIM-001](#pim-001) | Employee List: all filters | I | Planned |
| [PIM-002](#pim-002) | Add Employee: valid minimum data | I | Planned |
| [PIM-003](#pim-003) | Add Employee: invalid names and IDs | I | Planned |
| [PIM-004](#pim-004) | Add Employee: photo | I | Planned |
| [PIM-005](#pim-005) | Add Employee: optional login account | I | Planned |
| [PIM-006](#pim-006) | Add Employee: cancel and repeated Save | I | Planned |
| [PIM-007](#pim-007) | Employee List: details and deletion | I | Planned |
| [PIM-008](#pim-008) | Optional Fields | I | Planned |
| [PIM-009](#pim-009) | Custom Fields: type and placement | I | Planned |
| [PIM-010](#pim-010) | Custom Fields: validation | I | Planned |
| [PIM-011](#pim-011) | Data Import: valid file | I | Planned |
| [PIM-012](#pim-012) | Data Import: invalid and repeated files | I | Planned |
| [PIM-013](#pim-013) | Reports: definition and execution | I | Planned |
| [PIM-014](#pim-014) | Reports: modification and export | I | Planned |
| [PIM-015](#pim-015) | Reporting Methods: Create and persist | I | Planned |
| [PIM-016](#pim-016) | Reporting Methods: Required fields and boundaries | I | Planned |
| [PIM-017](#pim-017) | Reporting Methods: Duplicates and normalization | I | Planned |
| [PIM-018](#pim-018) | Reporting Methods: Edit and cancel | I | Planned |
| [PIM-019](#pim-019) | Reporting Methods: Delete and dependencies | I | Planned |
| [PIM-020](#pim-020) | Termination Reasons: Create and persist | I | Planned |
| [PIM-021](#pim-021) | Termination Reasons: Required fields and boundaries | I | Planned |
| [PIM-022](#pim-022) | Termination Reasons: Duplicates and normalization | I | Planned |
| [PIM-023](#pim-023) | Termination Reasons: Edit and cancel | I | Planned |
| [PIM-024](#pim-024) | Termination Reasons: Delete and dependencies | I | Planned |

## Scenarios

### PIM-001

**Employee List: all filters**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Apply Employee Name, ID, Employment Status, Include, Supervisor Name, Job Title and Sub Unit independently and together.

**Expected outcome:** Results match known fixtures; Current/Past/All employee views are correctly separated.

### PIM-002

**Add Employee: valid minimum data**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Enter required First/Last Name and a unique Employee ID; Save; reopen details and the list.

**Expected outcome:** One employee is created with the correct ID/name; other modules refer to the same person.

### PIM-003

**Add Employee: invalid names and IDs**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Omit First/Last Name separately; omit Middle Name; test duplicate IDs, whitespace and values above the stated length limit.

**Expected outcome:** Required fields are validated; middle-name optionality follows the form; ID policy is clear and no record is overwritten.

### PIM-004

**Add Employee: photo**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Test valid jpg/png/gif up to the stated 1 MB limit, boundary/oversized/invalid files, replacement and cancellation.

**Expected outcome:** The form's stated limits are applied; the correct employee gets the photo; a failed save does not leave a partial employee.

### PIM-005

**Add Employee: optional login account**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Toggle Create Login Details; test unique/duplicate Username, Status and Password/Confirm.

**Expected outcome:** Disabled toggle creates no user; enabled toggle links the user to this employee; account failures follow a documented atomic/compensating policy.

### PIM-006

**Add Employee: cancel and repeated Save**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Complete the form and cancel; repeat and click Save twice quickly.

**Expected outcome:** Cancellation creates nothing; successful submission creates only one employee/account.

### PIM-007

**Employee List: details and deletion**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open/edit an owned fixture; cancel/confirm individual and bulk deletion in isolation.

**Expected outcome:** Details belong to the correct person; only selected employees are removed; accounts/references follow policy.

### PIM-008

**Optional Fields**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Toggle every option available in this version; reopen Personal Details.

**Expected outcome:** Only relevant fields appear/disappear; previous data is retained according to policy; ESS follows the same configuration.

### PIM-009

**Custom Fields: type and placement**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Create text/dropdown fields on a chosen page; edit options/order/name.

**Expected outcome:** Fields appear on the intended page with correct types/options; values remain independent per employee; deletion behavior is defined.

### PIM-010

**Custom Fields: validation**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Test empty/duplicate names, missing pages, empty/duplicate options and the stated field-count limit.

**Expected outcome:** Clear errors enforce actual version limits; incomplete fields or invalid options are not created.

### PIM-011

**Data Import: valid file**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Use the version's CSV template with correct headers and several unique synthetic employees; import and inspect the list.

**Expected outcome:** Successful count matches the file; columns map correctly; multilingual text remains intact.

### PIM-012

**Data Import: invalid and repeated files**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Test empty CSV, missing headers, different encodings, invalid rows/duplicate IDs; import the same file again.

**Expected outcome:** Row errors and success/failure counts are reported; partial/atomic policy is clear; repetition does not unexpectedly overwrite or duplicate data.

### PIM-013

**Reports: definition and execution**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Create a synthetic report with known criteria/display fields; Save and Run against known employees.

**Expected outcome:** Columns, ordering and filters are correct; out-of-scope records and unauthorized confidential fields are excluded.

### PIM-014

**Reports: modification and export**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit/copy/delete reports where supported; test available downloads and an empty result.

**Expected outcome:** Saved definitions persist; exports match the displayed results; absent export controls are N/A, not Pass.

### PIM-015

**Reporting Methods: Create and persist**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete reporting method name with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. The method is available in employee Report-to relationships.

### PIM-016

**Reporting Methods: Required fields and boundaries**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For reporting method name, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. The method is available in employee Report-to relationships.

### PIM-017

**Reporting Methods: Duplicates and normalization**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Reporting Methods key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. The method is available in employee Report-to relationships.

### PIM-018

**Reporting Methods: Edit and cancel**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. The method is available in employee Report-to relationships.

### PIM-019

**Reporting Methods: Delete and dependencies**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a method used in an active reporting relationship in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### PIM-020

**Termination Reasons: Create and persist**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete termination reason name with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. The reason is available during termination; existing history remains intact.

### PIM-021

**Termination Reasons: Required fields and boundaries**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For termination reason name, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. The reason is available during termination; existing history remains intact.

### PIM-022

**Termination Reasons: Duplicates and normalization**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Termination Reasons key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. The reason is available during termination; existing history remains intact.

### PIM-023

**Termination Reasons: Edit and cancel**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. The reason is available during termination; existing history remains intact.

### PIM-024

**Termination Reasons: Delete and dependencies**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a reason referenced by termination history in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

[Back to scenario index](#scenario-index) | [Back to plan overview](README.md)
