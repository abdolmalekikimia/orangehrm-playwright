# My Info and employee details

**20 scenarios | 0 automated | 0 partial | 20 planned**

[Plan overview](README.md) | [CSV catalog](scenario-catalog.csv) | [JSON catalog](scenario-catalog.json)

## Scope

Personal Details; Contact Details; Emergency Contacts; Dependents; Immigration; Job; Salary; Report-to; Qualifications; Memberships; custom fields; attachments.

## Default prerequisites

Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

Shared controls and [evidence rules](README.md) also apply. R = read-only public demo; I = isolated instance; D = disposable instance. Partial implementations run only their documented public-demo variation, not the complete I/D workflow.

## Scenario index

| ID | Scenario | Design environment | Implementation status |
|---|---|---|---|
| [PROFILE-001](#profile-001) | Personal Details: identity | I | Planned |
| [PROFILE-002](#profile-002) | Personal Details: dates | I | Planned |
| [PROFILE-003](#profile-003) | Contact Details | I | Planned |
| [PROFILE-004](#profile-004) | Emergency Contacts | I | Planned |
| [PROFILE-005](#profile-005) | Dependents | I | Planned |
| [PROFILE-006](#profile-006) | Immigration | I | Planned |
| [PROFILE-007](#profile-007) | Job: details and contract | I | Planned |
| [PROFILE-008](#profile-008) | Job: termination and reactivation | I | Planned |
| [PROFILE-009](#profile-009) | Salary: component lifecycle | I | Planned |
| [PROFILE-010](#profile-010) | Salary: invalid values and bank fields | I | Planned |
| [PROFILE-011](#profile-011) | Report-to: supervisors and subordinates | I | Planned |
| [PROFILE-012](#profile-012) | Qualifications: Work Experience | I | Planned |
| [PROFILE-013](#profile-013) | Qualifications: Education | I | Planned |
| [PROFILE-014](#profile-014) | Qualifications: Skills | I | Planned |
| [PROFILE-015](#profile-015) | Qualifications: Languages | I | Planned |
| [PROFILE-016](#profile-016) | Qualifications: Licenses | I | Planned |
| [PROFILE-017](#profile-017) | Memberships | I | Planned |
| [PROFILE-018](#profile-018) | Custom Fields: Blood Type and other fields | I | Planned |
| [PROFILE-019](#profile-019) | Attachments: full lifecycle | I | Planned |
| [PROFILE-020](#profile-020) | ESS profile permissions | I | Planned |

## Scenarios

### PROFILE-001

**Personal Details: identity**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** Change name, Employee/Other ID, nationality, marital status and gender; Save and reopen.

**Expected outcome:** Values persist for the correct person; ESS cannot modify read-only fields; Directory names remain consistent.

### PROFILE-002

**Personal Details: dates**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** Test future/invalid/leap-day birth dates and empty/expired/valid license numbers and expiry dates.

**Expected outcome:** Stated rules and date format apply; invalid dates cannot be stored; future-date restrictions require an approved requirement.

### PROFILE-003

**Contact Details**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** Save address, country, province, postal code, home/mobile/work phones and emails.

**Expected outcome:** Fields persist independently; invalid email is rejected; phone/postal constraints follow the country/contract rather than test assumptions.

### PROFILE-004

**Emergency Contacts**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** Add a contact with name, relationship and valid phone details; edit; test required fields; cancel/confirm deletion.

**Expected outcome:** The correct employee owns the contact; the form's mandatory phone rules apply; canceled deletion preserves it.

### PROFILE-005

**Dependents**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** Add name, relationship and birth date; test Other with a description; edit/delete.

**Expected outcome:** Other requires a description where specified; dates are valid; dependents do not appear under another employee.

### PROFILE-006

**Immigration**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** Add Passport/Visa with number, issue/expiry dates, country and status; edit/delete; attach a test file.

**Expected outcome:** Document type/data are correct; date ordering follows policy; record/file remain associated with the intended employee.

### PROFILE-007

**Job: details and contract**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** Change title, category, unit, location, employment status, joined date and contract fields; attach a test contract.

**Expected outcome:** Choices come from Admin; dates/files are valid; PIM/Directory filters reflect the new values correctly.

### PROFILE-008

**Job: termination and reactivation**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** Terminate a fixture using a configured reason; inspect Past employees; reactivate if supported.

**Expected outcome:** Status/date/reason and Current/Past filters are consistent; login access changes only according to approved policy.

### PROFILE-009

**Salary: component lifecycle**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** Add a valid component, pay grade, frequency, currency and amount; edit/delete.

**Expected outcome:** Only authorized roles have access; amount/currency/precision are correct; pay-grade limits follow the contract.

### PROFILE-010

**Salary: invalid values and bank fields**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** Test empty/negative/text amounts and incompatible currency; test synthetic Direct Deposit/account/routing fields if present.

**Expected outcome:** Errors are specific; bank details remain protected; conditional fields are mandatory only when activated.

### PROFILE-011

**Report-to: supervisors and subordinates**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** Assign supervisor/subordinate using a reporting method; test same names, self-reference, duplicates and cycles.

**Expected outcome:** Correct IDs are linked; self-reference/cycles follow approved prevention rules; supervisor filters/permissions remain consistent.

### PROFILE-012

**Qualifications: Work Experience**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** Add company, job title, From/To and comments; test ongoing employment and reversed dates; edit/delete.

**Expected outcome:** Valid date ranges and ongoing-work behavior follow the form; records persist independently.

### PROFILE-013

**Qualifications: Education**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** Enter level, institute, major, year, score and available dates.

**Expected outcome:** Levels come from Admin; year/score formats and ranges follow the form; changes do not affect other records.

### PROFILE-014

**Qualifications: Skills**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** Add skill, years of experience and comments; test duplicates and negative/decimal experience.

**Expected outcome:** Choices and experience constraints are enforced; duplicate policy is followed; employee records remain independent.

### PROFILE-015

**Qualifications: Languages**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** Add language, fluency/competency and comments; test duplicate combinations and edits.

**Expected outcome:** Language/level are correct; invalid combinations are rejected; deleting one row preserves other abilities.

### PROFILE-016

**Qualifications: Licenses**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** Add license, number and issue/expiry dates; test invalid dates; edit/delete.

**Expected outcome:** License choices come from Admin; number/dates are valid; employee links and attachments remain correct.

### PROFILE-017

**Memberships**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** Add type, payer, subscription amount/currency and available membership dates.

**Expected outcome:** Dates/amounts are valid; types come from Admin; changes affect only the intended membership.

### PROFILE-018

**Custom Fields: Blood Type and other fields**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** Save available custom fields for two employees; test optional values and invalid dropdown selections.

**Expected outcome:** Configuration controls choices; values are independent; schema changes do not silently corrupt stored data.

### PROFILE-019

**Attachments: full lifecycle**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** On each tab supporting attachments, add a test file; download and compare its hash; edit description; cancel/confirm deletion.

**Expected outcome:** Downloaded content is intact; employee/tab association, actual size/type limits and download authorization are enforced.

### PROFILE-020

**ESS profile permissions**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS · **Automation:** Planned; no implemented test

**Prerequisites:** Two synthetic employees with Admin and ESS accounts; use PIM for administrative edits and My Info for self-service.

**Steps / test data:** With ESS, inspect own records and known URLs for another employee's Salary/Job/Contact tabs.

**Expected outcome:** Only approved read/edit access works; changing the URL cannot grant access; hiding a button is insufficient proof.

[Back to scenario index](#scenario-index) | [Back to plan overview](README.md)
