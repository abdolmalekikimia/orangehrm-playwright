# Authentication and sessions

**21 scenarios | 10 automated | 3 partial | 8 planned**

[Plan overview](README.md) | [CSV catalog](scenario-catalog.csv) | [JSON catalog](scenario-catalog.json)

## Scope

Login; Forgot Password; Change Password; Logout; direct access; account status; session expiration.

## Default prerequisites

For R cases, the public demo must be reachable. Account/session-controlled cases require an isolated instance.

Shared controls and [evidence rules](README.md) also apply. R = read-only public demo; I = isolated instance; D = disposable instance. Partial implementations run only their documented public-demo variation, not the complete I/D workflow.

## Scenario index

| ID | Scenario | Design environment | Implementation status |
|---|---|---|---|
| [AUTH-001](#auth-001) | Successful login | R | Automated |
| [AUTH-002](#auth-002) | Invalid password | R | Automated |
| [AUTH-003](#auth-003) | Both credentials empty | R | Automated |
| [AUTH-004](#auth-004) | Empty username | R | Automated |
| [AUTH-005](#auth-005) | Empty password | R | Automated |
| [AUTH-006](#auth-006) | Logout blocks subsequent dashboard access | R | Automated |
| [AUTH-007](#auth-007) | Dashboard without an authenticated session | R | Automated |
| [AUTH-008](#auth-008) | Unknown username | R | Automated |
| [AUTH-009](#auth-009) | Disabled account | I | Planned |
| [AUTH-010](#auth-010) | Characters and whitespace in credentials | I | Planned |
| [AUTH-011](#auth-011) | Enter key and repeated submission | R | Automated |
| [AUTH-012](#auth-012) | Forgot Password: empty input and cancellation | R | Automated |
| [AUTH-013](#auth-013) | Forgot Password: valid recovery lifecycle | I | Planned |
| [AUTH-014](#auth-014) | Session expiration during save | I | Planned |
| [AUTH-015](#auth-015) | Logout across browser tabs | I | Partial |
| [AUTH-016](#auth-016) | Browser Back after logout | I | Partial |
| [AUTH-017](#auth-017) | Direct access to all protected modules | I | Partial |
| [AUTH-018](#auth-018) | Change Password: valid change | I | Planned |
| [AUTH-019](#auth-019) | Change Password: invalid input and cancellation | I | Planned |
| [AUTH-020](#auth-020) | Recovery for an unknown account | I | Planned |
| [AUTH-021](#auth-021) | Session and request integrity | I | Planned |

## Scenarios

### AUTH-001

**Successful login**

**Priority:** P1 · **Design environment:** R · **Role:** Admin · **Automation:** Automated for the specified scenario scope

**Prerequisites:** For R cases, the public demo must be reachable. Account/session-controlled cases require an isolated instance.

**Steps / test data:** Enter the public demo credentials Admin/admin123 and select Login.

**Expected outcome:** The dashboard opens and displays the expected heading.

<details><summary>Implemented variations (1)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_login.py::test_successful_login[chromium]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_login.py) | full | Specified scenario scope |

</details>

Implementation metadata is not a fresh passing execution result.

### AUTH-002

**Invalid password**

**Priority:** P1 · **Design environment:** R · **Role:** Admin · **Automation:** Automated for the specified scenario scope

**Prerequisites:** For R cases, the public demo must be reachable. Account/session-controlled cases require an isolated instance.

**Steps / test data:** Enter a valid username and a deliberately invalid password; select Login.

**Expected outcome:** Invalid credentials is visible; the login page remains open.

<details><summary>Implemented variations (1)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_login.py::test_invalid_password_stays_on_login[chromium]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_login.py) | full | Specified scenario scope |

</details>

Implementation metadata is not a fresh passing execution result.

### AUTH-003

**Both credentials empty**

**Priority:** P1 · **Design environment:** R · **Role:** Admin · **Automation:** Automated for the specified scenario scope

**Prerequisites:** For R cases, the public demo must be reachable. Account/session-controlled cases require an isolated instance.

**Steps / test data:** Leave both inputs empty and select Login.

**Expected outcome:** Two Required messages appear; authentication does not occur.

<details><summary>Implemented variations (1)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_login.py::test_required_fields[chromium-AUTH-003-both-empty]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_login.py) | full | Specified scenario scope |

</details>

Implementation metadata is not a fresh passing execution result.

### AUTH-004

**Empty username**

**Priority:** P1 · **Design environment:** R · **Role:** Admin · **Automation:** Automated for the specified scenario scope

**Prerequisites:** For R cases, the public demo must be reachable. Account/session-controlled cases require an isolated instance.

**Steps / test data:** Leave the username empty; enter the valid demo password; select Login.

**Expected outcome:** One Required message appears; authentication does not occur.

<details><summary>Implemented variations (1)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_login.py::test_required_fields[chromium-AUTH-004-username-empty]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_login.py) | full | Specified scenario scope |

</details>

Implementation metadata is not a fresh passing execution result.

### AUTH-005

**Empty password**

**Priority:** P1 · **Design environment:** R · **Role:** Admin · **Automation:** Automated for the specified scenario scope

**Prerequisites:** For R cases, the public demo must be reachable. Account/session-controlled cases require an isolated instance.

**Steps / test data:** Enter Admin; leave the password empty; select Login.

**Expected outcome:** One Required message appears; authentication does not occur.

<details><summary>Implemented variations (1)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_login.py::test_required_fields[chromium-AUTH-005-password-empty]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_login.py) | full | Specified scenario scope |

</details>

Implementation metadata is not a fresh passing execution result.

### AUTH-006

**Logout blocks subsequent dashboard access**

**Priority:** P1 · **Design environment:** R · **Role:** Admin · **Automation:** Automated for the specified scenario scope

**Prerequisites:** For R cases, the public demo must be reachable. Account/session-controlled cases require an isolated instance.

**Steps / test data:** Log in, select Logout, then open the dashboard URL directly.

**Expected outcome:** The login form appears; the dashboard cannot be accessed without signing in again.

<details><summary>Implemented variations (1)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_login.py::test_logout_blocks_dashboard[chromium]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_login.py) | full | Specified scenario scope |

</details>

Implementation metadata is not a fresh passing execution result.

### AUTH-007

**Dashboard without an authenticated session**

**Priority:** P1 · **Design environment:** R · **Role:** Admin · **Automation:** Automated for the specified scenario scope

**Prerequisites:** For R cases, the public demo must be reachable. Account/session-controlled cases require an isolated instance.

**Steps / test data:** Open the dashboard URL in a fresh browser context.

**Expected outcome:** The browser is redirected to the login page and the Login form is visible.

<details><summary>Implemented variations (1)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_login.py::test_unauthenticated_dashboard_redirects[chromium]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_login.py) | full | Specified scenario scope |

</details>

Implementation metadata is not a fresh passing execution result.

### AUTH-008

**Unknown username**

**Priority:** P1 · **Design environment:** R · **Role:** Admin · **Automation:** Automated for the specified scenario scope

**Prerequisites:** Reachable public demo; valid published Admin credentials where authentication is required. No business-data mutation.

**Steps / test data:** Enter a synthetic unknown username and any password; select Login.

**Expected outcome:** Login is rejected without unnecessarily exposing account existence or sensitive details.

<details><summary>Implemented variations (1)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_login.py::test_unknown_username_has_generic_error[chromium]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_login.py) | full | Specified scenario scope |

</details>

Implementation metadata is not a fresh passing execution result.

### AUTH-009

**Disabled account**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** For R cases, the public demo must be reachable. Account/session-controlled cases require an isolated instance.

**Steps / test data:** Sign in with a disabled synthetic account; enable it in the isolated environment and repeat.

**Expected outcome:** The disabled account cannot authenticate; enabling it restores access according to policy.

### AUTH-010

**Characters and whitespace in credentials**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** For R cases, the public demo must be reachable. Account/session-controlled cases require an isolated instance.

**Steps / test data:** Test Persian characters, leading/trailing spaces, long strings and symbols independently in each input.

**Expected outcome:** Inputs are handled according to the authentication contract without server errors, script execution or unauthorized password normalization.

### AUTH-011

**Enter key and repeated submission**

**Priority:** P1 · **Design environment:** R · **Role:** Admin · **Automation:** Automated for the specified scenario scope

**Prerequisites:** Reachable public demo; valid published Admin credentials where authentication is required. No business-data mutation.

**Steps / test data:** Authenticate using Enter; in a new session, double-click Login quickly.

**Expected outcome:** A clear outcome and one valid session result; repeated submission does not lock the interface.

<details><summary>Implemented variations (1)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_login.py::test_enter_and_repeated_login[chromium]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_login.py) | full | Specified scenario scope |

</details>

Implementation metadata is not a fresh passing execution result.

### AUTH-012

**Forgot Password: empty input and cancellation**

**Priority:** P1 · **Design environment:** R · **Role:** Admin · **Automation:** Automated for the specified scenario scope

**Prerequisites:** Reachable public demo; valid published Admin credentials where authentication is required. No business-data mutation.

**Steps / test data:** Open Forgot Password, submit an empty username, then select Cancel.

**Expected outcome:** Required-field validation appears; cancellation returns to Login without creating a recovery request.

<details><summary>Implemented variations (1)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_login.py::test_password_recovery_empty_and_cancel[chromium]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_login.py) | full | Specified scenario scope |

</details>

Implementation metadata is not a fresh passing execution result.

### AUTH-013

**Forgot Password: valid recovery lifecycle**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** For R cases, the public demo must be reachable. Account/session-controlled cases require an isolated instance.

**Steps / test data:** Use a test mailbox in an isolated environment; request recovery and test valid, expired and previously used links.

**Expected outcome:** Only the intended account can use a valid link; expired/used links are rejected; the response avoids unnecessary account enumeration.

### AUTH-014

**Session expiration during save**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** For R cases, the public demo must be reachable. Account/session-controlled cases require an isolated instance.

**Steps / test data:** Expire an open form's session in the isolated environment; attempt Save, then sign in again.

**Expected outcome:** No unauthorized update occurs; reauthentication is clearly requested; the save outcome is not ambiguous.

### AUTH-015

**Logout across browser tabs**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Partially automated; remaining variations are planned

**Prerequisites:** For R cases, the public demo must be reachable. Account/session-controlled cases require an isolated instance.

**Steps / test data:** Open two tabs sharing a session; log out in one; attempt protected reads and Save in the other.

**Expected outcome:** The other tab cannot obtain fresh protected data or modify records using the ended session.

<details><summary>Implemented variations (1)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_login.py::test_logout_invalidates_second_tab[chromium]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_login.py) | partial | fresh protected reads in a second tab; no write attempted |

</details>

Implementation metadata is not a fresh passing execution result.

### AUTH-016

**Browser Back after logout**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Partially automated; remaining variations are planned

**Prerequisites:** For R cases, the public demo must be reachable. Account/session-controlled cases require an isolated instance.

**Steps / test data:** After Logout, use Back and Reload, then revisit the previous form URL.

**Expected outcome:** The session is not restored; fresh confidential data and protected operations remain inaccessible.

<details><summary>Implemented variations (1)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_login.py::test_back_after_logout_does_not_restore_session[chromium]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_login.py) | partial | Back, Reload and protected read; no write attempted |

</details>

Implementation metadata is not a fresh passing execution result.

### AUTH-017

**Direct access to all protected modules**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Partially automated; remaining variations are planned

**Prerequisites:** For R cases, the public demo must be reachable. Account/session-controlled cases require an isolated instance.

**Steps / test data:** Without authentication, open the recorded URLs of all 12 modules and their protected detail forms.

**Expected outcome:** Every protected route requires authentication; the existing automated test covers the dashboard only.

<details><summary>Implemented variations (12)</summary>

| Source test | Scope | Implemented variation |
|---|---|---|
| [`tests/test_navigation.py::test_module_entry_requires_authentication[chromium-Admin]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Admin protected entry route |
| [`tests/test_navigation.py::test_module_entry_requires_authentication[chromium-PIM]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | PIM protected entry route |
| [`tests/test_navigation.py::test_module_entry_requires_authentication[chromium-Leave]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Leave protected entry route |
| [`tests/test_navigation.py::test_module_entry_requires_authentication[chromium-Time]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Time protected entry route |
| [`tests/test_navigation.py::test_module_entry_requires_authentication[chromium-Recruitment]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Recruitment protected entry route |
| [`tests/test_navigation.py::test_module_entry_requires_authentication[chromium-My-Info]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | My Info protected entry route |
| [`tests/test_navigation.py::test_module_entry_requires_authentication[chromium-Performance]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Performance protected entry route |
| [`tests/test_navigation.py::test_module_entry_requires_authentication[chromium-Dashboard]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Dashboard protected entry route |
| [`tests/test_navigation.py::test_module_entry_requires_authentication[chromium-Directory]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Directory protected entry route |
| [`tests/test_navigation.py::test_module_entry_requires_authentication[chromium-Maintenance]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Maintenance protected entry route |
| [`tests/test_navigation.py::test_module_entry_requires_authentication[chromium-Claim]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Claim protected entry route |
| [`tests/test_navigation.py::test_module_entry_requires_authentication[chromium-Buzz]`](https://github.com/abdolmalekikimia/orangehrm-playwright/blob/main/tests/test_navigation.py) | partial | Buzz protected entry route |

</details>

Implementation metadata is not a fresh passing execution result.

### AUTH-018

**Change Password: valid change**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** For R cases, the public demo must be reachable. Account/session-controlled cases require an isolated instance.

**Steps / test data:** With a synthetic account in an isolated instance, manually submit valid Current/New/Confirm values; log out and test old/new passwords.

**Expected outcome:** Only the new password authenticates; success is clear; passwords are not logged; no real account credential is changed.

### AUTH-019

**Change Password: invalid input and cancellation**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** For R cases, the public demo must be reachable. Account/session-controlled cases require an isolated instance.

**Steps / test data:** Test an incorrect current password, mismatched confirmation, empty fields and a new password outside the stated policy; select Cancel.

**Expected outcome:** Invalid changes are rejected with field-specific errors; cancellation preserves the old password.

### AUTH-020

**Recovery for an unknown account**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** For R cases, the public demo must be reachable. Account/session-controlled cases require an isolated instance.

**Steps / test data:** Request recovery for an unknown username using test mail infrastructure; compare the visible response with a valid account.

**Expected outcome:** The response does not unnecessarily reveal account existence; no usable recovery link is created for another account.

### AUTH-021

**Session and request integrity**

**Priority:** P1 · **Design environment:** I · **Role:** Admin · **Automation:** Planned; no implemented test

**Prerequisites:** For R cases, the public demo must be reachable. Account/session-controlled cases require an isolated instance.

**Steps / test data:** In an isolated instance, attempt changes with an expired/invalid session and, where required, without the contract's CSRF protection.

**Expected outcome:** Invalid requests cannot change data; successful login establishes an appropriate session identity; this requires a separate technical test.

[Back to scenario index](#scenario-index) | [Back to plan overview](README.md)
