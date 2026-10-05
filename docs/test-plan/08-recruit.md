# Recruitment

**17 scenarios | 0 automated | 17 planned**

[Plan overview](README.md) | [CSV catalog](scenario-catalog.csv) | [JSON catalog](scenario-catalog.json)

## Scope

Candidates; Vacancies; application details; hiring workflow.

## Default prerequisites

Fully synthetic vacancies/candidates in isolation; emails route to a test mail sink; no real employment decisions.

Shared controls and evidence rules in [COMMON](02-common.md) and the [overview](README.md) also apply. Environment codes: R = read-only demo, I = isolated instance, D = disposable instance.

## Scenario index

| ID | Scenario | Environment | Automation status |
|---|---|---|---|
| [RECRUIT-001](#recruit-001) | Vacancies: Create and persist | I | Planned |
| [RECRUIT-002](#recruit-002) | Vacancies: Required fields and boundaries | I | Planned |
| [RECRUIT-003](#recruit-003) | Vacancies: Duplicates and normalization | I | Planned |
| [RECRUIT-004](#recruit-004) | Vacancies: Edit and cancel | I | Planned |
| [RECRUIT-005](#recruit-005) | Vacancies: Delete and dependencies | I | Planned |
| [RECRUIT-006](#recruit-006) | Vacancies: filters | I | Planned |
| [RECRUIT-007](#recruit-007) | Candidates: valid creation | I | Planned |
| [RECRUIT-008](#recruit-008) | Candidates: validation | I | Planned |
| [RECRUIT-009](#recruit-009) | Candidates: duplicates | I | Planned |
| [RECRUIT-010](#recruit-010) | Candidates: all filters | I | Planned |
| [RECRUIT-011](#recruit-011) | Candidate: edit, download and delete | I | Planned |
| [RECRUIT-012](#recruit-012) | Shortlist and Reject | I | Planned |
| [RECRUIT-013](#recruit-013) | Schedule Interview | I | Planned |
| [RECRUIT-014](#recruit-014) | Interview outcome | I | Planned |
| [RECRUIT-015](#recruit-015) | Offer and Hire workflow | I | Planned |
| [RECRUIT-016](#recruit-016) | History and concurrent actions | I | Planned |
| [RECRUIT-017](#recruit-017) | Published Vacancy | I | Planned |

## Scenarios

### RECRUIT-001

**Vacancies: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Fully synthetic vacancies/candidates in isolation; emails route to a test mail sink; no real employment decisions.

**Steps / test data:** Open Add; complete name, Job Title, Hiring Manager, Number of Positions, description and available Active/Publish options with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. Title/manager are valid; position count follows the stated rules; publishing occurs only in the test instance.

### RECRUIT-002

**Vacancies: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Fully synthetic vacancies/candidates in isolation; emails route to a test mail sink; no real employment decisions.

**Steps / test data:** For name, Job Title, Hiring Manager, Number of Positions, description and available Active/Publish options, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. Title/manager are valid; position count follows the stated rules; publishing occurs only in the test instance.

### RECRUIT-003

**Vacancies: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Fully synthetic vacancies/candidates in isolation; emails route to a test mail sink; no real employment decisions.

**Steps / test data:** Reuse the same Vacancies key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. Title/manager are valid; position count follows the stated rules; publishing occurs only in the test instance.

### RECRUIT-004

**Vacancies: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Fully synthetic vacancies/candidates in isolation; emails route to a test mail sink; no real employment decisions.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. Title/manager are valid; position count follows the stated rules; publishing occurs only in the test instance.

### RECRUIT-005

**Vacancies: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Fully synthetic vacancies/candidates in isolation; emails route to a test mail sink; no real employment decisions.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a vacancy with candidate/application history in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### RECRUIT-006

**Vacancies: filters**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Fully synthetic vacancies/candidates in isolation; emails route to a test mail sink; no real employment decisions.

**Steps / test data:** Apply available Job Title, Vacancy, Hiring Manager and Status filters independently and together.

**Expected outcome:** Only matching vacancies appear; inactive vacancies are excluded from new selections according to policy.

### RECRUIT-007

**Candidates: valid creation**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Fully synthetic vacancies/candidates in isolation; emails route to a test mail sink; no real employment decisions.

**Steps / test data:** Enter required name/email, vacancy and optional fields; attach a synthetic resume; Save and reopen.

**Expected outcome:** One candidate/application is correctly linked; data/file are intact; initial status matches the version.

### RECRUIT-008

**Candidates: validation**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Fully synthetic vacancies/candidates in isolation; emails route to a test mail sink; no real employment decisions.

**Steps / test data:** Test missing name/email, invalid email/phone/text/date, disallowed files and available consent controls.

**Expected outcome:** Errors are specific; consent follows policy; incomplete data and prohibited files are rejected.

### RECRUIT-009

**Candidates: duplicates**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Fully synthetic vacancies/candidates in isolation; emails route to a test mail sink; no real employment decisions.

**Steps / test data:** Reuse an email for the same/different vacancy; submit twice quickly.

**Expected outcome:** Duplicate/application rules apply without silent overwrites.

### RECRUIT-010

**Candidates: all filters**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Fully synthetic vacancies/candidates in isolation; emails route to a test mail sink; no real employment decisions.

**Steps / test data:** Test Job Title, Vacancy, Manager, Status, Name, Keywords, Application Date and Method of Application.

**Expected outcome:** Individual/combined results match fixtures; multi-keyword logic follows policy; date boundaries are correct.

### RECRUIT-011

**Candidate: edit, download and delete**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Fully synthetic vacancies/candidates in isolation; emails route to a test mail sink; no real employment decisions.

**Steps / test data:** Edit contact details, keywords and notes; download the resume; cancel/confirm deletion in isolation.

**Expected outcome:** The correct candidate/file is affected; cancellation preserves data; deletion follows retention/history policy.

### RECRUIT-012

**Shortlist and Reject**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Fully synthetic vacancies/candidates in isolation; emails route to a test mail sink; no real employment decisions.

**Steps / test data:** Shortlist/reject a new synthetic application using an authorized actor; attempt illegal transitions.

**Expected outcome:** Only permitted transitions occur; status/history/notes agree; unauthorized accounts cannot record decisions.

### RECRUIT-013

**Schedule Interview**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Fully synthetic vacancies/candidates in isolation; emails route to a test mail sink; no real employment decisions.

**Steps / test data:** Enter interview name, interviewers, date and time; test missing/invalid values and supported reschedule/cancel actions.

**Expected outcome:** Interview/participants are correct; validation applies; calendar/history agree; no invitation reaches a real person.

### RECRUIT-014

**Interview outcome**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Fully synthetic vacancies/candidates in isolation; emails route to a test mail sink; no real employment decisions.

**Steps / test data:** Pass/fail a synthetic candidate after an interview; add notes; attempt the action before the interview stage.

**Expected outcome:** Transitions require the correct stage; actor/time/outcome are accurately recorded.

### RECRUIT-015

**Offer and Hire workflow**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Fully synthetic vacancies/candidates in isolation; emails route to a test mail sink; no real employment decisions.

**Steps / test data:** For a synthetic candidate, follow application through offer/hire and available offer-declined paths.

**Expected outcome:** Only legal actions appear/execute at each status; history is accurate; employee conversion is tested only if actually supported.

### RECRUIT-016

**History and concurrent actions**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Fully synthetic vacancies/candidates in isolation; emails route to a test mail sink; no real employment decisions.

**Steps / test data:** Perform competing actions on one application from two sessions; reload details/history.

**Expected outcome:** Final state is consistent; conflicting decisions are not silently overwritten; events are not lost.

### RECRUIT-017

**Published Vacancy**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Fully synthetic vacancies/candidates in isolation; emails route to a test mail sink; no real employment decisions.

**Steps / test data:** Toggle Publish for a fixture in isolation and inspect the version's public vacancy view.

**Expected outcome:** Only approved published details are visible; inactive/unpublished visibility follows policy; unsupported capability is N/A.

[Back to scenario index](#scenario-index) | [Back to plan overview](README.md)
