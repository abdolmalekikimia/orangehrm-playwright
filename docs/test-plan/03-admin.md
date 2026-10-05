# Admin and configuration

**82 scenarios | 0 automated | 82 planned**

[Plan overview](README.md) | [CSV catalog](scenario-catalog.csv) | [JSON catalog](scenario-catalog.json)

## Scope

User Management; Job; Organization; Qualifications; Nationalities; Corporate Branding; Configuration.

## Default prerequisites

Authorized account and synthetic fixtures owned by this run.

Shared controls and evidence rules in [COMMON](02-common.md) and the [overview](README.md) also apply. Environment codes: R = read-only demo, I = isolated instance, D = disposable instance.

## Scenario index

| ID | Scenario | Environment | Automation status |
|---|---|---|---|
| [ADMIN-001](#admin-001) | Users: Create and persist | I | Planned |
| [ADMIN-002](#admin-002) | Users: Required fields and boundaries | I | Planned |
| [ADMIN-003](#admin-003) | Users: Duplicates and normalization | I | Planned |
| [ADMIN-004](#admin-004) | Users: Edit and cancel | I | Planned |
| [ADMIN-005](#admin-005) | Users: Delete and dependencies | I | Planned |
| [ADMIN-006](#admin-006) | Users: filters | I | Planned |
| [ADMIN-007](#admin-007) | Users: role and account status | I | Planned |
| [ADMIN-008](#admin-008) | Users: employee association | I | Planned |
| [ADMIN-009](#admin-009) | Users: password reset | I | Planned |
| [ADMIN-010](#admin-010) | Job Titles: Create and persist | I | Planned |
| [ADMIN-011](#admin-011) | Job Titles: Required fields and boundaries | I | Planned |
| [ADMIN-012](#admin-012) | Job Titles: Duplicates and normalization | I | Planned |
| [ADMIN-013](#admin-013) | Job Titles: Edit and cancel | I | Planned |
| [ADMIN-014](#admin-014) | Job Titles: Delete and dependencies | I | Planned |
| [ADMIN-015](#admin-015) | Pay Grades: Create and persist | I | Planned |
| [ADMIN-016](#admin-016) | Pay Grades: Required fields and boundaries | I | Planned |
| [ADMIN-017](#admin-017) | Pay Grades: Duplicates and normalization | I | Planned |
| [ADMIN-018](#admin-018) | Pay Grades: Edit and cancel | I | Planned |
| [ADMIN-019](#admin-019) | Pay Grades: Delete and dependencies | I | Planned |
| [ADMIN-020](#admin-020) | Employment Status: Create and persist | I | Planned |
| [ADMIN-021](#admin-021) | Employment Status: Required fields and boundaries | I | Planned |
| [ADMIN-022](#admin-022) | Employment Status: Duplicates and normalization | I | Planned |
| [ADMIN-023](#admin-023) | Employment Status: Edit and cancel | I | Planned |
| [ADMIN-024](#admin-024) | Employment Status: Delete and dependencies | I | Planned |
| [ADMIN-025](#admin-025) | Job Categories: Create and persist | I | Planned |
| [ADMIN-026](#admin-026) | Job Categories: Required fields and boundaries | I | Planned |
| [ADMIN-027](#admin-027) | Job Categories: Duplicates and normalization | I | Planned |
| [ADMIN-028](#admin-028) | Job Categories: Edit and cancel | I | Planned |
| [ADMIN-029](#admin-029) | Job Categories: Delete and dependencies | I | Planned |
| [ADMIN-030](#admin-030) | Work Shifts: Create and persist | I | Planned |
| [ADMIN-031](#admin-031) | Work Shifts: Required fields and boundaries | I | Planned |
| [ADMIN-032](#admin-032) | Work Shifts: Duplicates and normalization | I | Planned |
| [ADMIN-033](#admin-033) | Work Shifts: Edit and cancel | I | Planned |
| [ADMIN-034](#admin-034) | Work Shifts: Delete and dependencies | I | Planned |
| [ADMIN-035](#admin-035) | Locations: Create and persist | I | Planned |
| [ADMIN-036](#admin-036) | Locations: Required fields and boundaries | I | Planned |
| [ADMIN-037](#admin-037) | Locations: Duplicates and normalization | I | Planned |
| [ADMIN-038](#admin-038) | Locations: Edit and cancel | I | Planned |
| [ADMIN-039](#admin-039) | Locations: Delete and dependencies | I | Planned |
| [ADMIN-040](#admin-040) | Skills: Create and persist | I | Planned |
| [ADMIN-041](#admin-041) | Skills: Required fields and boundaries | I | Planned |
| [ADMIN-042](#admin-042) | Skills: Duplicates and normalization | I | Planned |
| [ADMIN-043](#admin-043) | Skills: Edit and cancel | I | Planned |
| [ADMIN-044](#admin-044) | Skills: Delete and dependencies | I | Planned |
| [ADMIN-045](#admin-045) | Education: Create and persist | I | Planned |
| [ADMIN-046](#admin-046) | Education: Required fields and boundaries | I | Planned |
| [ADMIN-047](#admin-047) | Education: Duplicates and normalization | I | Planned |
| [ADMIN-048](#admin-048) | Education: Edit and cancel | I | Planned |
| [ADMIN-049](#admin-049) | Education: Delete and dependencies | I | Planned |
| [ADMIN-050](#admin-050) | Licenses: Create and persist | I | Planned |
| [ADMIN-051](#admin-051) | Licenses: Required fields and boundaries | I | Planned |
| [ADMIN-052](#admin-052) | Licenses: Duplicates and normalization | I | Planned |
| [ADMIN-053](#admin-053) | Licenses: Edit and cancel | I | Planned |
| [ADMIN-054](#admin-054) | Licenses: Delete and dependencies | I | Planned |
| [ADMIN-055](#admin-055) | Languages: Create and persist | I | Planned |
| [ADMIN-056](#admin-056) | Languages: Required fields and boundaries | I | Planned |
| [ADMIN-057](#admin-057) | Languages: Duplicates and normalization | I | Planned |
| [ADMIN-058](#admin-058) | Languages: Edit and cancel | I | Planned |
| [ADMIN-059](#admin-059) | Languages: Delete and dependencies | I | Planned |
| [ADMIN-060](#admin-060) | Memberships: Create and persist | I | Planned |
| [ADMIN-061](#admin-061) | Memberships: Required fields and boundaries | I | Planned |
| [ADMIN-062](#admin-062) | Memberships: Duplicates and normalization | I | Planned |
| [ADMIN-063](#admin-063) | Memberships: Edit and cancel | I | Planned |
| [ADMIN-064](#admin-064) | Memberships: Delete and dependencies | I | Planned |
| [ADMIN-065](#admin-065) | Nationalities: Create and persist | I | Planned |
| [ADMIN-066](#admin-066) | Nationalities: Required fields and boundaries | I | Planned |
| [ADMIN-067](#admin-067) | Nationalities: Duplicates and normalization | I | Planned |
| [ADMIN-068](#admin-068) | Nationalities: Edit and cancel | I | Planned |
| [ADMIN-069](#admin-069) | Nationalities: Delete and dependencies | I | Planned |
| [ADMIN-070](#admin-070) | General Information | I | Planned |
| [ADMIN-071](#admin-071) | Organization Structure: hierarchy | I | Planned |
| [ADMIN-072](#admin-072) | Pay Grades: currencies and limits | I | Planned |
| [ADMIN-073](#admin-073) | Work Shifts: duration and employee assignment | I | Planned |
| [ADMIN-074](#admin-074) | Corporate Branding | I | Planned |
| [ADMIN-075](#admin-075) | Email Configuration | I | Planned |
| [ADMIN-076](#admin-076) | Email Subscriptions | I | Planned |
| [ADMIN-077](#admin-077) | Localization | I | Planned |
| [ADMIN-078](#admin-078) | Language Packages | I | Planned |
| [ADMIN-079](#admin-079) | Modules | I | Planned |
| [ADMIN-080](#admin-080) | Social Media Authentication | I | Planned |
| [ADMIN-081](#admin-081) | Register OAuth Client | I | Planned |
| [ADMIN-082](#admin-082) | LDAP Configuration | I | Planned |

## Scenarios

### ADMIN-001

**Users: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete Employee Name, User Role, Status, Username, Password and Confirm Password with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. The employee must be selected by identity; password confirmation and stated password policy apply; username and role remain correct.

### ADMIN-002

**Users: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For Employee Name, User Role, Status, Username, Password and Confirm Password, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. The employee must be selected by identity; password confirmation and stated password policy apply; username and role remain correct.

### ADMIN-003

**Users: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Users key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. The employee must be selected by identity; password confirmation and stated password policy apply; username and role remain correct.

### ADMIN-004

**Users: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. The employee must be selected by identity; password confirmation and stated password policy apply; username and role remain correct.

### ADMIN-005

**Users: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against the last administrator account or a user linked to an employee in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### ADMIN-006

**Users: filters**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Search known users by Username, Role, Employee Name and Status, independently and together.

**Expected outcome:** Only matching users appear; Reset restores the configured defaults.

### ADMIN-007

**Users: role and account status**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Disable/enable a synthetic ESS account; change its role in isolation and sign in again.

**Expected outcome:** Capabilities follow the new role/status matrix; visible menus alone do not prove authorization.

### ADMIN-008

**Users: employee association**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Select same-name employees, an employee without an account and one with an existing account.

**Expected outcome:** The correct employee ID is linked; account-per-employee limits follow the contract; display names do not cause misassociation.

### ADMIN-009

**Users: password reset**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reset a synthetic account's password in isolation; try old/new credentials afterward.

**Expected outcome:** Only the new password works; passwords are not exposed in tables, reports or logs; credential entry/change follows the applicable manual/tool policy.

### ADMIN-010

**Job Titles: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete Job Title, Job Description, Note and Job Specification with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. The title is available in employee Job forms; specification attachments follow the page limits.

### ADMIN-011

**Job Titles: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For Job Title, Job Description, Note and Job Specification, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. The title is available in employee Job forms; specification attachments follow the page limits.

### ADMIN-012

**Job Titles: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Job Titles key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. The title is available in employee Job forms; specification attachments follow the page limits.

### ADMIN-013

**Job Titles: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. The title is available in employee Job forms; specification attachments follow the page limits.

### ADMIN-014

**Job Titles: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a job title used by an employee in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### ADMIN-015

**Pay Grades: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete grade name, currency and minimum/maximum salary with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. Minimum must not exceed maximum; numbers/currencies are valid and available in Salary.

### ADMIN-016

**Pay Grades: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For grade name, currency and minimum/maximum salary, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. Minimum must not exceed maximum; numbers/currencies are valid and available in Salary.

### ADMIN-017

**Pay Grades: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Pay Grades key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. Minimum must not exceed maximum; numbers/currencies are valid and available in Salary.

### ADMIN-018

**Pay Grades: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. Minimum must not exceed maximum; numbers/currencies are valid and available in Salary.

### ADMIN-019

**Pay Grades: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a pay grade or currency used by a salary record in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### ADMIN-020

**Employment Status: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete employment status name with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. The status appears correctly in PIM and employee filters.

### ADMIN-021

**Employment Status: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For employment status name, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. The status appears correctly in PIM and employee filters.

### ADMIN-022

**Employment Status: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Employment Status key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. The status appears correctly in PIM and employee filters.

### ADMIN-023

**Employment Status: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. The status appears correctly in PIM and employee filters.

### ADMIN-024

**Employment Status: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a status assigned to an employee in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### ADMIN-025

**Job Categories: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete job category name with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. The category is selectable in Job and remains distinct from Job Title.

### ADMIN-026

**Job Categories: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For job category name, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. The category is selectable in Job and remains distinct from Job Title.

### ADMIN-027

**Job Categories: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Job Categories key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. The category is selectable in Job and remains distinct from Job Title.

### ADMIN-028

**Job Categories: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. The category is selectable in Job and remains distinct from Job Title.

### ADMIN-029

**Job Categories: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a category assigned to an employee in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### ADMIN-030

**Work Shifts: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete shift name, start/end time and assigned employees with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. Duration follows the approved time/shift rules; overnight shifts require a defined policy.

### ADMIN-031

**Work Shifts: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For shift name, start/end time and assigned employees, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. Duration follows the approved time/shift rules; overnight shifts require a defined policy.

### ADMIN-032

**Work Shifts: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Work Shifts key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. Duration follows the approved time/shift rules; overnight shifts require a defined policy.

### ADMIN-033

**Work Shifts: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. Duration follows the approved time/shift rules; overnight shifts require a defined policy.

### ADMIN-034

**Work Shifts: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a shift assigned to employees in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### ADMIN-035

**Locations: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete name, country, address and contact fields with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. Country/location fields are consistent; the location appears correctly in Job and Directory.

### ADMIN-036

**Locations: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For name, country, address and contact fields, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. Country/location fields are consistent; the location appears correctly in Job and Directory.

### ADMIN-037

**Locations: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Locations key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. Country/location fields are consistent; the location appears correctly in Job and Directory.

### ADMIN-038

**Locations: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. Country/location fields are consistent; the location appears correctly in Job and Directory.

### ADMIN-039

**Locations: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a location assigned to employees or other active records in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### ADMIN-040

**Skills: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete skill name and description with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. The skill is available in employee Qualifications.

### ADMIN-041

**Skills: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For skill name and description, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. The skill is available in employee Qualifications.

### ADMIN-042

**Skills: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Skills key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. The skill is available in employee Qualifications.

### ADMIN-043

**Skills: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. The skill is available in employee Qualifications.

### ADMIN-044

**Skills: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a skill assigned in Qualifications in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### ADMIN-045

**Education: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete education level with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. The level is available in employee Qualifications.

### ADMIN-046

**Education: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For education level, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. The level is available in employee Qualifications.

### ADMIN-047

**Education: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Education key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. The level is available in employee Qualifications.

### ADMIN-048

**Education: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. The level is available in employee Qualifications.

### ADMIN-049

**Education: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against an education level used by an employee in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### ADMIN-050

**Licenses: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete license name with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. The license links to employee-specific qualification data.

### ADMIN-051

**Licenses: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For license name, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. The license links to employee-specific qualification data.

### ADMIN-052

**Licenses: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Licenses key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. The license links to employee-specific qualification data.

### ADMIN-053

**Licenses: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. The license links to employee-specific qualification data.

### ADMIN-054

**Licenses: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a license used in employee Qualifications in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### ADMIN-055

**Languages: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete language name with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. The language is available in employee Qualifications.

### ADMIN-056

**Languages: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For language name, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. The language is available in employee Qualifications.

### ADMIN-057

**Languages: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Languages key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. The language is available in employee Qualifications.

### ADMIN-058

**Languages: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. The language is available in employee Qualifications.

### ADMIN-059

**Languages: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a language used in employee Qualifications in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### ADMIN-060

**Memberships: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete membership name with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. The type is available in employee Memberships.

### ADMIN-061

**Memberships: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For membership name, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. The type is available in employee Memberships.

### ADMIN-062

**Memberships: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Memberships key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. The type is available in employee Memberships.

### ADMIN-063

**Memberships: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. The type is available in employee Memberships.

### ADMIN-064

**Memberships: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a membership type assigned to an employee in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### ADMIN-065

**Nationalities: Create and persist**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Add; complete nationality name with valid synthetic data and a unique key; Save, search and reload.

**Expected outcome:** One record is created; stored details remain correct after returning. The nationality is available in Personal Details.

### ADMIN-066

**Nationalities: Required fields and boundaries**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For nationality name, omit each required field separately; test whitespace-only input, each stated limit and one value beyond it.

**Expected outcome:** Invalid data cannot be saved; errors identify the affected field; valid boundary values are accepted. The nationality is available in Personal Details.

### ADMIN-067

**Nationalities: Duplicates and normalization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Reuse the same Nationalities key; change letter case and surrounding whitespace; submit twice quickly.

**Expected outcome:** The approved uniqueness policy is enforced without unintended duplicates; where duplicates are allowed, record IDs remain independent. The nationality is available in Personal Details.

### ADMIN-068

**Nationalities: Edit and cancel**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Edit an owned fixture and Save; change it again and select Cancel; reopen the record.

**Expected outcome:** Saved edits persist; canceled edits do not; untouched fields and record identity remain unchanged. The nationality is available in Personal Details.

### ADMIN-069

**Nationalities: Delete and dependencies**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** For an unreferenced fixture, first cancel deletion, then confirm; repeat against a nationality assigned to an employee in isolation.

**Expected outcome:** Cancel preserves the record; confirmation affects only its target; dependency policy either prevents deletion or handles references consistently without orphan records.

### ADMIN-070

**General Information**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Inspect organization details, displayed employee count, name, tax identifiers, address and contact fields; change editable fields in isolation.

**Expected outcome:** Read-only fields remain protected; required/email validation applies; saved values persist.

### ADMIN-071

**Organization Structure: hierarchy**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Add a synthetic root/subunit, change its name or position, expand/collapse the tree and attempt deletion with dependencies.

**Expected outcome:** The hierarchy remains correct; cycles/inconsistent deletions are prevented; PIM Sub Unit choices match the structure.

### ADMIN-072

**Pay Grades: currencies and limits**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Add currencies to a grade; edit limits; test duplicates, negative/decimal values and reversed limits.

**Expected outcome:** Currency uniqueness follows policy; precision is correct; deleting an in-use currency does not corrupt salary records.

### ADMIN-073

**Work Shifts: duration and employee assignment**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Test equal/reversed/boundary times and multiple assigned employees.

**Expected outcome:** Duration follows the approved shift rules; duplicate/conflicting assignments are handled according to policy.

### ADMIN-074

**Corporate Branding**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Preview logos/colors; test invalid files and Cancel; save and restore defaults in isolation.

**Expected outcome:** Preview matches the applied result; cancellation makes no change; branding is consistent across relevant pages.

### ADMIN-075

**Email Configuration**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Configure test SMTP, authentication and ports in isolation; test incomplete values; send only to a test mail sink.

**Expected outcome:** Validation and connection errors are clear; secrets are masked; no email is sent to real recipients.

### ADMIN-076

**Email Subscriptions**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Configure supported subscription types and synthetic recipients; enable/disable; test duplicate/invalid addresses.

**Expected outcome:** Each event reaches only authorized active test recipients; disabling prevents delivery.

### ADMIN-077

**Localization**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Change language/date format in isolation; reopen dates in Leave, PIM and Time.

**Expected outcome:** Text/format are consistent; underlying stored dates do not change; manual input and calendar selection agree.

### ADMIN-078

**Language Packages**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Inspect packages; install/activate only where supported in an isolated instance; test invalid packages.

**Expected outcome:** Package status is clear; translated menus remain usable; unavailable features are recorded as limitations.

### ADMIN-079

**Modules**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Disable/enable a module in isolation; inspect the sidebar and direct URLs using different roles.

**Expected outcome:** Disabled modules are blocked in the UI and at protected routes; existing data survives re-enabling.

### ADMIN-080

**Social Media Authentication**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Use a test identity provider; test incomplete settings, valid/invalid callbacks and canceled login.

**Expected outcome:** Only verified identities map to authorized accounts; invalid state/callbacks are rejected; secrets are not exposed.

### ADMIN-081

**Register OAuth Client**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Create a synthetic client with valid/invalid names and redirect URLs; edit/delete/revoke where supported.

**Expected outcome:** Only approved exact redirects work; secrets remain protected; revoked clients cannot obtain new tokens; mark Blocked without a test integration.

### ADMIN-082

**LDAP Configuration**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Connect to a test directory; test valid/invalid connectivity, user synchronization and inactive accounts.

**Expected outcome:** Connection/sync results are clear; no unintended duplication/deletion occurs; mark Blocked without a test LDAP service.

[Back to scenario index](#scenario-index) | [Back to plan overview](README.md)
