# Maintenance

**8 scenarios | 0 automated | 8 planned**

[Plan overview](README.md) | [CSV catalog](scenario-catalog.csv) | [JSON catalog](scenario-catalog.json)

## Scope

Administrator Access was observed; post-gate Purge Employee/Candidate and Access Records require confirmation in the target version.

## Default prerequisites

Disposable isolated instance with a restorable snapshot; post-gate pages were not inspected in the source review.

Shared controls and evidence rules in [COMMON](02-common.md) and the [overview](README.md) also apply. Environment codes: R = read-only demo, I = isolated instance, D = disposable instance.

## Scenario index

| ID | Scenario | Environment | Automation status |
|---|---|---|---|
| [MAINT-001](#maint-001) | Administrator Access: cancellation | D | Planned |
| [MAINT-002](#maint-002) | Administrator Access: invalid credentials | D | Planned |
| [MAINT-003](#maint-003) | Administrator Access: authorization | D | Planned |
| [MAINT-004](#maint-004) | Purge Employee: preview and cancellation | D | Planned |
| [MAINT-005](#maint-005) | Purge Employee: outcome | D | Planned |
| [MAINT-006](#maint-006) | Purge Candidate | D | Planned |
| [MAINT-007](#maint-007) | Access Records | D | Planned |
| [MAINT-008](#maint-008) | Purge: failure and repetition | D | Planned |

## Scenarios

### MAINT-001

**Administrator Access: cancellation**

**Priority:** P1 · **Environment:** D · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Disposable isolated instance with a restorable snapshot; post-gate pages were not inspected in the source review.

**Steps / test data:** Open Maintenance and select Cancel.

**Expected outcome:** Return to the previous page without changing data or executing a critical action.

### MAINT-002

**Administrator Access: invalid credentials**

**Priority:** P1 · **Environment:** D · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Disposable isolated instance with a restorable snapshot; post-gate pages were not inspected in the source review.

**Steps / test data:** In isolation, test empty/incorrect passwords and Confirm.

**Expected outcome:** Clear errors appear; purge/export access remains blocked.

### MAINT-003

**Administrator Access: authorization**

**Priority:** P1 · **Environment:** D · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Disposable isolated instance with a restorable snapshot; post-gate pages were not inspected in the source review.

**Steps / test data:** Compare ESS/Admin, direct operation URLs and old sessions before/after logout.

**Expected outcome:** Only authorized Admin access with valid revalidation is allowed; routes/stale sessions cannot bypass the gate.

### MAINT-004

**Purge Employee: preview and cancellation**

**Priority:** P1 · **Environment:** D · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Disposable isolated instance with a restorable snapshot; post-gate pages were not inspected in the source review.

**Steps / test data:** In a disposable instance, select a synthetic terminated employee with related history; inspect scope and Cancel.

**Expected outcome:** Eligible target/history are clearly identified; cancellation permanently deletes nothing.

### MAINT-005

**Purge Employee: outcome**

**Priority:** P1 · **Environment:** D · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Disposable isolated instance with a restorable snapshot; post-gate pages were not inspected in the source review.

**Steps / test data:** With a snapshot and a separate confirmation procedure, purge synthetic data; inspect profile, account, files and reports.

**Expected outcome:** Only the declared scope is removed; unrelated records remain; no orphan records or residual file access persist; unavailable capability is N/A.

### MAINT-006

**Purge Candidate**

**Priority:** P1 · **Environment:** D · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Disposable isolated instance with a restorable snapshot; post-gate pages were not inspected in the source review.

**Steps / test data:** In isolation, use a synthetic candidate eligible under retention rules; filter, cancel and perform an authorized purge.

**Expected outcome:** Only eligible records are removed; out-of-scope candidates remain; resumes/references follow policy.

### MAINT-007

**Access Records**

**Priority:** P1 · **Environment:** D · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Disposable isolated instance with a restorable snapshot; post-gate pages were not inspected in the source review.

**Steps / test data:** Select a synthetic employee and use the available export in isolation; inspect the file.

**Expected outcome:** Only the intended employee's approved data is exported; the file opens correctly; unauthorized downloads are blocked.

### MAINT-008

**Purge: failure and repetition**

**Priority:** P1 · **Environment:** D · **Role:** Admin · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Disposable isolated instance with a restorable snapshot; post-gate pages were not inspected in the source review.

**Steps / test data:** In isolation, inject mid-operation failure, repeat the purge and test concurrent execution; compare with/restored snapshots.

**Expected outcome:** Deletion/error state is clear; partial deletion and out-of-scope effects are prevented or reported according to the contract.

[Back to scenario index](#scenario-index) | [Back to plan overview](README.md)
