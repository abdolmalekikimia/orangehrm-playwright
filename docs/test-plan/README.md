# OrangeHRM Test Scenario Plan

For the portfolio navigation view, browse the [Test Scenario Wiki](https://github.com/abdolmalekikimia/orangehrm-playwright/wiki). These files and catalogs remain the editable source with the same scenario IDs.

**323 designed scenarios: 14 automated, 7 partially automated and 302 planned; 97 executable test variations.**

> Implementation scope and execution outcome are separate. The public-demo suite covers the mapped read-only variations; the remaining workflows require isolated fixtures and approved rules.

Based on OrangeHRM OS 5.9, inspected on **2026-10-05**. Scenario IDs are preserved from the original Persian plan.

## Browse by area

| Area | Scenarios | Automated | Partial | Planned |
|---|---:|---:|---:|---:|
| [Authentication and sessions](01-auth.md) | 21 | 10 | 3 | 8 |
| [Shared controls and navigation](02-common.md) | 23 | 3 | 4 | 16 |
| [Admin and configuration](03-admin.md) | 82 | 0 | 0 | 82 |
| [PIM: employees and configuration](04-pim.md) | 24 | 0 | 0 | 24 |
| [My Info and employee details](05-profile.md) | 20 | 0 | 0 | 20 |
| [Leave management](06-leave.md) | 28 | 0 | 0 | 28 |
| [Time and attendance](07-time.md) | 26 | 0 | 0 | 26 |
| [Recruitment](08-recruit.md) | 17 | 0 | 0 | 17 |
| [Performance management](09-perf.md) | 19 | 0 | 0 | 19 |
| [Dashboard](10-dash.md) | 8 | 0 | 0 | 8 |
| [Employee Directory](11-dir.md) | 5 | 0 | 0 | 5 |
| [Maintenance](12-maint.md) | 8 | 1 | 0 | 7 |
| [Claims and expenses](13-claim.md) | 21 | 0 | 0 | 21 |
| [Buzz social feed](14-buzz.md) | 11 | 0 | 0 | 11 |
| [Authorization and cross-module integrity](15-rbac.md) | 10 | 0 | 0 | 10 |
| **Total** | **323** | **14** | **7** | **302** |

Each area has a linked scenario index and full prerequisites, steps/data and expected outcomes. Use the [CSV catalog](scenario-catalog.csv) for filtering/import and the [JSON catalog](scenario-catalog.json) for tooling.

## Feature coverage matrix

| Main module | Features in scope | Scenario area |
|---|---|---|
| Admin | Users; Job Titles; Pay Grades; Employment Status; Job Categories; Work Shifts; General Information; Locations; Structure; Skills; Education; Licenses; Languages; Memberships; Nationalities; Corporate Branding; Email Configuration/Subscriptions; Localization; Language Packages; Modules; Social Media Authentication; OAuth Client; LDAP | [ADMIN](03-admin.md) |
| PIM | Employee List; Add Employee; Reports; Optional Fields; Custom Fields; Data Import; Reporting Methods; Termination Reasons | [PIM](04-pim.md) |
| My Info / Employee | Personal Details; Contact; Emergency; Dependents; Immigration; Job; Salary; Report-to; Qualifications; Memberships; custom fields; attachments | [PROFILE](05-profile.md) |
| Leave | Apply; My Leave; Add/Employee/My Entitlements; employee/self usage reports; Leave Period; Leave Types; Work Week; Holidays; Leave List; Assign | [LEAVE](06-leave.md) |
| Time | My/Employee Timesheets; My/Employee Attendance; Punch In/Out; Attendance Configuration; Project/Employee Reports; Attendance Summary; Customers; Projects/Activities | [TIME](07-time.md) |
| Recruitment | Candidates; Vacancies; application details; Interview; Offer/Hire and History where supported | [RECRUIT](08-recruit.md) |
| Performance | KPIs; Trackers; Manage/My/Employee Reviews; My/Employee Trackers and logs | [PERF](09-perf.md) |
| Dashboard | Time at Work; My Actions; six Quick Launch links; Latest Buzz; Leave Today; Sub Unit/Location distribution | [DASH](10-dash.md) |
| Directory | Filters; cards/details; pagination; profile consistency; permissions | [DIR](11-dir.md) |
| Maintenance | Observed Administrator Access gate; Purge Employee/Candidate and Access Records require isolated version confirmation | [MAINT](12-maint.md) |
| Claim | Events; Expense Types; Submit; My/Employee Claims; Assign; expenses/attachments; workflow | [CLAIM](13-claim.md) |
| Buzz | Text; Photos; Video; Like; Comment; Share; sorting; edit/delete; Read More; conditional widgets | [BUZZ](14-buzz.md) |

Shared navigation/form/table/upload checks are in [COMMON](02-common.md). Cross-module workflows and authorization are in [RBAC](15-rbac.md). These checks supplement the feature-specific scenarios.

## Execution environments

| Code | Environment | Intended use |
|---|---|---|
| R | Read-only public demo | Recruiter-friendly checks without business-data mutations. |
| I | Isolated OrangeHRM instance | Synthetic CRUD, workflow, integration, role and failure tests. |
| D | Disposable instance with snapshot | Controlled purge and destructive maintenance tests. |

**Keep I/D scenarios out of the default shared-demo run.** A scenario is a test specification, not an instruction to mutate the public demo.

## Scope and evidence rules

1. This is a scenario plan and automation backlog, not evidence that every feature or combination has been tested. 323 designed scenarios: 14 automated, 7 partially automated and 302 planned; 97 executable test variations. Implementation status is separate from execution outcome.
2. Inventory basis: read-only inspection of the public OrangeHRM OS 5.9 UI on 2026-10-05 and inspection of the two existing test files. Opening a page or menu does not establish workflow correctness.
3. R: read-only, suitable for the recruiter demo. I: isolated instance with synthetic data and controlled accounts. D: disposable instance with a restorable snapshot for purge testing. No record mutation, publishing, global configuration change or purge was performed during the inventory review.
4. P1: authentication, authorization, sensitive data, core workflows and data integrity. P2: existing navigation and secondary capabilities. Review priority against actual risk/roles; automation effort does not determine business importance.
5. COMMON scenarios apply to every relevant page. Record a separate result for each applicable page/control; one passing example cannot represent the entire module. The scenario count is not a count of all combinations or executed coverage.
6. Do not invent unknown rules: field limits, name uniqueness, half-day rounding, negative leave policy, permission revocation timing and state transitions must be confirmed against the target UI/version and approved requirements. Mark the affected execution Blocked while its oracle is unresolved.
7. Maintenance pages after credential revalidation were not inspected. LDAP, SMTP, OAuth, Language Packages and some workflow actions depend on version/infrastructure. Verify availability before execution; use N/A with a reason only when a capability is genuinely absent/out of scope.
8. Use qa_<run-id> fixture names and test-domain email addresses. Keep an ID manifest and clean up only records owned by the run. Do not assert fixed names/counts from the mutable shared demo.
9. A Pass requires observable evidence: reload persistence, correct identity/reference, before/after values, legal state changes and no unintended changes to other records. A toast or HTTP 200 alone is insufficient.
10. Execution outcomes: Not Run, Pass, Fail, Blocked or N/A. Record version/time/role/fixtures/scenario ID/expected/actual/evidence. Report simulated failure tests separately from live end-to-end validation.

## Role model to confirm before execution

| Role | Expected scope, subject to approved policy |
|---|---|
| Admin | Administrative configuration/employee access as defined by policy; Maintenance still requires its separate gate. |
| ESS | Own My Info/Leave/Timesheets/Claims/Reviews/Trackers plus explicitly permitted shared features; no implicit administration of others. |
| Supervisor | Only scoped employees and delegated approval/evaluation actions; supervisor status does not imply all Admin capabilities. |
| Guest / expired session | No protected page/operation access; public vacancies are an exception only if intentionally supported by the target version. |

## Result oracles

| Area | Evidence used to judge correctness |
|---|---|
| Users / jobs / employees | List and details, reload persistence, identity links and PIM/Directory consistency. |
| Leave | Known calendar, full/half-day duration, entitled/used/balance before and after, self/employee reports. |
| Time | Daily/activity entries, day/week totals, state and employee/project reports. |
| Claim | Expense sum with approved precision, currency, owner/reference, state and both list/detail views. |
| Review / recruitment | Approved transition matrix, actor permissions, state/history and legal next actions. |
| Uploads | Stated type/size limits, downloaded file hash, entity association and download permissions. |
| Authorization | Allowed/disallowed accounts, direct URLs, operation attempts and unchanged out-of-scope data. |

## Apply shared checks per page

- **Lists:** apply all available individual/combined filters, Reset, autocomplete, sorting, pagination and selection checks.
- **Forms:** apply required-field/boundary validation, Save/reload persistence, Cancel/Back/Reload and repeated-submission checks.
- **Delete controls:** exercise Cancel/Close/Escape/Confirm and relevant dependencies.
- **Uploads:** use the limits stated by that page and verify downloaded content and access.
- **Protected features:** test both visible UI and direct-route/operation authorization using controlled accounts.
- **Every applicable page:** accessibility, layout and controlled error handling. Missing controls are N/A with a reason; unresolved business rules are Blocked.

## Suggested implementation order

1. Run the mapped public-demo cases, inspect per-scenario evidence and distinguish full from partial scope.
2. In I, establish master data and employee/user fixtures; implement CRUD and validation, then Leave/Time/Claim/Recruitment/Performance workflows and role tests.
3. Add controlled failure, concurrency, upload, accessibility/browser and cross-module checks.
4. Run D scenarios only in a disposable environment after snapshot/scope confirmation. Never include purge in the default recruiter run.
5. Derive coverage reports from recorded execution results. Planned, Blocked and N/A are not successful executed coverage.

## Recording an execution

Use one result row per scenario **and applicable page/variation**:

| Scenario ID | Page / variation | Version | Role | Fixture IDs | Expected | Actual | Outcome | Evidence | Time |
|---|---|---|---|---|---|---|---|---|---|
| COMMON-007 | Page and filter under test | Target version | Test role | Run-owned IDs | Approved oracle | Observed result | Not Run / Pass / Fail / Blocked / N/A | Trace, screenshot, report or comparison | Timestamp |

Automation status in this catalog means **implemented in source**, not a fresh successful live execution. Test references point to the current cases; the plan does not add test implementations.

[Back to the project README](../../README.md)
