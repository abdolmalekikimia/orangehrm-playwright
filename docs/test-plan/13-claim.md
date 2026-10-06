# Claims and expenses

**21 scenarios | 0 automated | 0 partial | 21 planned**

[Plan overview](README.md) | [CSV catalog](scenario-catalog.csv) | [JSON catalog](scenario-catalog.json)

## Scope

Events; Expense Types; Submit Claim; My Claims; Employee Claims; Assign Claim; expenses/attachments; workflow.

## Default prerequisites

Authorized account and synthetic fixtures owned by this run.

Shared controls and [evidence rules](README.md) also apply. R = read-only public demo; I = isolated instance; D = disposable instance. Partial implementations run only their documented public-demo variation, not the complete I/D workflow.

## Scenario index

| ID | Scenario | Design environment | Implementation status |
|---|---|---|---|
| [CLAIM-001](#claim-001) | Events: Create and persist | I | Planned |
| [CLAIM-002](#claim-002) | Events: Required fields and boundaries | I | Planned |
| [CLAIM-003](#claim-003) | Events: Duplicates and normalization | I | Planned |
| [CLAIM-004](#claim-004) | Events: Edit and cancel | I | Planned |
| [CLAIM-005](#claim-005) | Events: Delete and dependencies | I | Planned |
| [CLAIM-006](#claim-006) | Expense Types: Create and persist | I | Planned |
| [CLAIM-007](#claim-007) | Expense Types: Required fields and boundaries | I | Planned |
| [CLAIM-008](#claim-008) | Expense Types: Duplicates and normalization | I | Planned |
| [CLAIM-009](#claim-009) | Expense Types: Edit and cancel | I | Planned |
| [CLAIM-010](#claim-010) | Expense Types: Delete and dependencies | I | Planned |
| [CLAIM-011](#claim-011) | Submit Claim: create draft | I | Planned |
| [CLAIM-012](#claim-012) | Claim: invalid fields and cancellation | I | Planned |
| [CLAIM-013](#claim-013) | Expenses: lifecycle | I | Planned |
| [CLAIM-014](#claim-014) | Expenses: amount and date boundaries | I | Planned |
| [CLAIM-015](#claim-015) | Claim attachments | I | Planned |
| [CLAIM-016](#claim-016) | Claim: submit | I | Planned |
| [CLAIM-017](#claim-017) | My Claims | I | Planned |
| [CLAIM-018](#claim-018) | Employee Claims: all filters | I | Planned |
| [CLAIM-019](#claim-019) | Assign Claim | I | Planned |
| [CLAIM-020](#claim-020) | Claim: approve, reject and paid status | I | Planned |
| [CLAIM-021](#claim-021) | Claim: concurrent decisions and foreign references | I | Planned |

## Scenarios

### CLAIM-001

**Events: Create and persist**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete name, description and Active status with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. Active events are available for new claims; deactivation preserves history.

### CLAIM-002

**Events: Required fields and boundaries**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For name, description and Active status, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. Active events are available for new claims; deactivation preserves history.

### CLAIM-003

**Events: Duplicates and normalization**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Events key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. Active events are available for new claims; deactivation preserves history.

### CLAIM-004

**Events: Edit and cancel**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. Active events are available for new claims; deactivation preserves history.

### CLAIM-005

**Events: Delete and dependencies**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against an event referenced by a claim in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### CLAIM-006

**Expense Types: Create and persist**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete name, description and Active status with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. Active types are available for expenses; historical use of inactive types follows policy.

### CLAIM-007

**Expense Types: Required fields and boundaries**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For name, description and Active status, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. Active types are available for expenses; historical use of inactive types follows policy.

### CLAIM-008

**Expense Types: Duplicates and normalization**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Expense Types key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. Active types are available for expenses; historical use of inactive types follows policy.

### CLAIM-009

**Expense Types: Edit and cancel**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. Active types are available for expenses; historical use of inactive types follows policy.

### CLAIM-010

**Expense Types: Delete and dependencies**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against an expense type referenced by an expense in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### CLAIM-011

**Submit Claim: create draft**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Choose an active event, currency and remarks; Create; inspect reference/status.

**Expected outcome:** One draft receives a unique reference and correct currency; it appears in the owner's My Claims.

### CLAIM-012

**Claim: invalid fields and cancellation**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Test missing/inactive event/currency, long remarks, Cancel and repeated Create.

**Expected outcome:** Validation is clear; cancellation creates nothing; repeated clicks do not create extra drafts.

### CLAIM-013

**Expenses: lifecycle**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Add type, date, amount and note across multiple expenses; edit/delete and Cancel.

**Expected outcome:** Rows/totals are accurate; claim currency remains consistent; editing one expense updates the total correctly.

### CLAIM-014

**Expenses: amount and date boundaries**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Test negative/zero/decimal boundary/text/very large amounts and invalid dates.

**Expected outcome:** Amount/date policies and financial precision apply; rounding is consistent; invalid values cannot be saved.

### CLAIM-015

**Claim attachments**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Upload valid/invalid synthetic receipts; download; cancel/confirm deletion.

**Expected outcome:** Files remain intact and linked to the right claim; page limits and role-based downloads are enforced.

### CLAIM-016

**Claim: submit**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Submit drafts with/without expenses; repeat submission and attempt edits afterward.

**Expected outcome:** Prerequisites/legal transitions apply; locking/edit policy follows the workflow; repetition has no additional effect.

### CLAIM-017

**My Claims**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Filter available reference/event/status/date fields; inspect details and cancellation where supported.

**Expected outcome:** Only owned claims appear; status/totals match details; cancellation requires an eligible stage.

### CLAIM-018

**Employee Claims: all filters**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Apply Employee, Reference ID, Event, Status, From/To and Include.

**Expected outcome:** Only matching authorized records appear; Past/Current and Reset work correctly.

### CLAIM-019

**Assign Claim**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Admin creates a claim for a synthetic employee, adds expenses and submits.

**Expected outcome:** The intended employee owns it and sees it in My Claims; author/history are correct where exposed.

### CLAIM-020

**Claim: approve, reject and paid status**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** In isolation, follow supported Submitted to Approved/Rejected/Paid transitions with authorized actors and synthetic data.

**Expected outcome:** Only transitions supported by this version succeed; permissions are enforced; Paid is a test status, never a real transaction; all views agree.

### CLAIM-021

**Claim: concurrent decisions and foreign references**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Attempt two decisions on a claim; access another employee's known reference.

**Expected outcome:** Final state is consistent; a second action cannot create a conflicting outcome; reference changes do not expand access.

[Back to scenario index](#scenario-index) | [Back to plan overview](README.md)
