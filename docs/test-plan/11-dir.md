# Employee Directory

**5 scenarios | 0 automated | 5 planned**

[Plan overview](README.md) | [CSV catalog](scenario-catalog.csv) | [JSON catalog](scenario-catalog.json)

## Scope

Employee Name; Job Title; Location; cards/details; pagination and profile consistency.

## Default prerequisites

Authorized account and synthetic fixtures owned by this run.

Shared controls and evidence rules in [COMMON](02-common.md) and the [overview](README.md) also apply. Environment codes: R = read-only demo, I = isolated instance, D = disposable instance.

## Scenario index

| ID | Scenario | Environment | Automation status |
|---|---|---|---|
| [DIR-001](#dir-001) | Directory: all filters | I | Planned |
| [DIR-002](#dir-002) | Directory: cards and details | I | Planned |
| [DIR-003](#dir-003) | Directory: counts and pagination | I | Planned |
| [DIR-004](#dir-004) | Directory: profile changes | I | Planned |
| [DIR-005](#dir-005) | Directory: permissions | I | Planned |

## Scenarios

### DIR-001

**Directory: all filters**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Apply each filter and combinations to known employees; test same names, no matches and Reset.

**Expected outcome:** Only matching cards appear with correct identity; empty states are clear.

### DIR-002

**Directory: cards and details**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open employees with/without photos; inspect title, unit, location and permitted contact fields.

**Expected outcome:** Values match that employee's profile; placeholders work; restricted confidential data is not exposed.

### DIR-003

**Directory: counts and pagination**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Use enough fixtures for multiple pages; change a filter from the last page.

**Expected outcome:** Pagination/counts are correct; without data changes, employees are not skipped or duplicated.

### DIR-004

**Directory: profile changes**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Change a fixture's name/title/location in PIM; reload Directory.

**Expected outcome:** The correct card reflects new values; others remain unchanged; terminated-employee visibility follows policy.

### DIR-005

**Directory: permissions**

**Priority:** P1 · **Environment:** I · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** As ESS, inspect restricted contact details and a known URL for another employee.

**Expected outcome:** Only approved public fields are visible; salary, sensitive IDs and private files do not leak.

[Back to scenario index](#scenario-index) | [Back to plan overview](README.md)
