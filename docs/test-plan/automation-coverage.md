# Implementation Coverage

323 designed scenarios: 14 automated, 7 partially automated and 302 planned; 97 executable test variations.

This table is generated from collected `scenario` markers. Full means the specified scenario scope has an implementation; partial means only the named variations are implemented. Neither means the latest run passed.

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

## Implemented mappings

| ID | Status | Test variations |
|---|---|---:|
| [AUTH-001](01-auth.md#auth-001) | automated | 1 |
| [AUTH-002](01-auth.md#auth-002) | automated | 1 |
| [AUTH-003](01-auth.md#auth-003) | automated | 1 |
| [AUTH-004](01-auth.md#auth-004) | automated | 1 |
| [AUTH-005](01-auth.md#auth-005) | automated | 1 |
| [AUTH-006](01-auth.md#auth-006) | automated | 1 |
| [AUTH-007](01-auth.md#auth-007) | automated | 1 |
| [AUTH-008](01-auth.md#auth-008) | automated | 1 |
| [AUTH-011](01-auth.md#auth-011) | automated | 1 |
| [AUTH-012](01-auth.md#auth-012) | automated | 1 |
| [AUTH-015](01-auth.md#auth-015) | partial | 1 |
| [AUTH-016](01-auth.md#auth-016) | partial | 1 |
| [AUTH-017](01-auth.md#auth-017) | partial | 12 |
| [COMMON-001](02-common.md#common-001) | automated | 1 |
| [COMMON-002](02-common.md#common-002) | automated | 1 |
| [COMMON-003](02-common.md#common-003) | automated | 1 |
| [COMMON-004](02-common.md#common-004) | partial | 62 |
| [COMMON-005](02-common.md#common-005) | partial | 3 |
| [COMMON-007](02-common.md#common-007) | partial | 2 |
| [COMMON-009](02-common.md#common-009) | partial | 2 |
| [MAINT-001](12-maint.md#maint-001) | automated | 1 |

## Reports

- `reports/index.html`: test results with scenario ID, scope and variation.
- `reports/junit.xml`: machine-readable results and scenario properties.
- `reports/scenario-results.json`: actual outcomes, fixture errors, selected variations and unmapped scenarios.
- A subset run has only its selected cases; unselected scenarios are not failures or passes.

## Regenerate implementation metadata

```powershell
.\.venv\Scripts\python.exe -m pytest --collect-only -q -o addopts='' --scenario-map reports/scenario-map.json
.\.venv\Scripts\python.exe tools/sync_scenario_docs.py --map reports/scenario-map.json
```

Add `--wiki-dir PATH` to render a Wiki checkout before publishing. No live tests or mutations run during documentation generation.
