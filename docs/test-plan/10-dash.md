# Dashboard

**8 scenarios | 0 automated | 0 partial | 8 planned**

[Plan overview](README.md) | [CSV catalog](scenario-catalog.csv) | [JSON catalog](scenario-catalog.json)

## Scope

Time at Work; My Actions; six Quick Launch links; Buzz Latest Posts; Employees on Leave Today; Sub Unit/Location distribution.

## Default prerequisites

Authorized account and synthetic fixtures owned by this run.

Shared controls and [evidence rules](README.md) also apply. R = read-only public demo; I = isolated instance; D = disposable instance. Partial implementations run only their documented public-demo variation, not the complete I/D workflow.

## Scenario index

| ID | Scenario | Design environment | Implementation status |
|---|---|---|---|
| [DASH-001](#dash-001) | Quick Launch: six destinations | I | Planned |
| [DASH-002](#dash-002) | Time at Work | I | Planned |
| [DASH-003](#dash-003) | My Actions | I | Planned |
| [DASH-004](#dash-004) | Buzz Latest Posts | I | Planned |
| [DASH-005](#dash-005) | Employees on Leave Today | I | Planned |
| [DASH-006](#dash-006) | Leave Today: configuration | I | Planned |
| [DASH-007](#dash-007) | Employee Distribution charts | I | Planned |
| [DASH-008](#dash-008) | Widgets: roles and loading failures | I | Planned |

## Scenarios

### DASH-001

**Quick Launch: six destinations**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Open Assign Leave, Leave List, Timesheets, Apply Leave, My Leave and My Timesheet; return each time.

**Expected outcome:** Each shortcut reaches the right role-appropriate destination and does not bypass authorization.

### DASH-002

**Time at Work**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Inspect the widget/chart before/after Punch In/Out with known daily/weekly records.

**Expected outcome:** Status/totals agree with Attendance; no-record states are clear.

### DASH-003

**My Actions**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Create synthetic leave/timesheet/review/candidate items requiring action; open and complete them.

**Expected outcome:** Counts/links contain only current authorized actions and update after completion; available action types are version/role-dependent.

### DASH-004

**Buzz Latest Posts**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Create a synthetic post in isolation; inspect dashboard ordering and the post link.

**Expected outcome:** Latest posts match the newsfeed; long content does not break layout.

### DASH-005

**Employees on Leave Today**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Create approved/pending/rejected full/half-day requests for today/tomorrow.

**Expected outcome:** Included employees follow widget policy; no duplicate counting; date/timezone handling is consistent.

### DASH-006

**Leave Today: configuration**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Change the widget's available settings in isolation, then restore them.

**Expected outcome:** Only the intended display changes; persistence/restore work; unauthorized configuration is blocked.

### DASH-007

**Employee Distribution charts**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Use known Sub Unit/Location fixtures, missing assignments and zero employees.

**Expected outcome:** Totals/legends/percentages agree with the eligible population; no division-by-zero or broken chart occurs.

### DASH-008

**Widgets: roles and loading failures**

**Priority:** P1 · **Design environment:** I · **Role:** Admin / ESS / Supervisor · **Automation:** Planned; no implemented test

**Prerequisites:** Authorized account and synthetic fixtures owned by this run.

**Steps / test data:** Inspect Admin/ESS and narrow viewports; inject a controlled failure in one widget.

**Expected outcome:** Only permitted widgets appear; one failure does not stop the rest; errors are distinct from empty data.

[Back to scenario index](#scenario-index) | [Back to plan overview](README.md)
