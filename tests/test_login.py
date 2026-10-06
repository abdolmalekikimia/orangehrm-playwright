import re
from uuid import uuid4

import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage


@pytest.mark.scenario("AUTH-001")
def test_successful_login(login, credentials):
    login.sign_in(*credentials)
    login.expect_dashboard()


@pytest.mark.scenario("AUTH-002")
def test_invalid_password_stays_on_login(login, credentials):
    login.sign_in(credentials[0], "intentionally-invalid-password")
    expect(login.page.get_by_text("Invalid credentials", exact=True)).to_be_visible()
    expect(login.submit).to_be_visible()
    expect(login.page).to_have_url(re.compile(r"/auth/login$"))


@pytest.mark.parametrize("username,password,errors", [
    pytest.param("", "", 2, id="AUTH-003-both-empty", marks=pytest.mark.scenario("AUTH-003")),
    pytest.param("Admin", "", 1, id="AUTH-005-password-empty", marks=pytest.mark.scenario("AUTH-005")),
    pytest.param("", "admin123", 1, id="AUTH-004-username-empty", marks=pytest.mark.scenario("AUTH-004")),
])
def test_required_fields(login, username, password, errors):
    login.sign_in(username, password)
    expect(login.page.get_by_text("Required", exact=True)).to_have_count(errors)
    expect(login.submit).to_be_visible()
    expect(login.page).to_have_url(re.compile(r"/auth/login$"))


@pytest.mark.scenario("AUTH-006")
def test_logout_blocks_dashboard(authenticated_page, demo_url):
    page = authenticated_page
    page.locator(".oxd-userdropdown-tab").click()
    page.get_by_role("menuitem", name="Logout").click()
    expect(page.get_by_role("button", name="Login", exact=True)).to_be_visible()
    page.goto(demo_url + "/web/index.php/dashboard/index", wait_until="domcontentloaded")
    expect(page).to_have_url(re.compile(r"/auth/login$"))
    expect(page.get_by_role("button", name="Login", exact=True)).to_be_visible()


@pytest.mark.scenario("AUTH-007")
def test_unauthenticated_dashboard_redirects(page, demo_url):
    page.goto(demo_url + "/web/index.php/dashboard/index", wait_until="domcontentloaded")
    expect(page).to_have_url(re.compile(r"/auth/login$"))
    expect(page.get_by_role("button", name="Login", exact=True)).to_be_visible()


@pytest.mark.scenario("AUTH-008")
def test_unknown_username_has_generic_error(login):
    login.sign_in("qa_unknown_" + uuid4().hex, "invalid-test-password")
    expect(login.page.get_by_text("Invalid credentials", exact=True)).to_be_visible()
    expect(login.page).to_have_url(re.compile(r"/auth/login$"))


@pytest.mark.scenario("AUTH-011")
def test_enter_and_repeated_login(login, credentials, new_context, demo_url):
    login.username.fill(credentials[0])
    login.password.fill(credentials[1])
    login.password.press("Enter")
    login.expect_dashboard()
    context = new_context()
    model = LoginPage(context.new_page(), demo_url)
    model.open()
    model.username.fill(credentials[0])
    model.password.fill(credentials[1])
    model.submit.dblclick()
    model.expect_dashboard()


@pytest.mark.scenario("AUTH-012")
def test_password_recovery_empty_and_cancel(login):
    page = login.page
    page.get_by_text("Forgot your password?", exact=True).click()
    expect(page.get_by_role("heading", name="Reset Password", exact=True)).to_be_visible()
    page.get_by_role("button", name="Reset Password", exact=True).click()
    expect(page.get_by_text("Required", exact=True)).to_be_visible()
    page.get_by_role("button", name="Cancel", exact=True).click()
    expect(login.submit).to_be_visible()
    expect(page).to_have_url(re.compile(r"/auth/login$"))


@pytest.mark.scenario("AUTH-015", coverage="partial", variation="fresh protected reads in a second tab; no write attempted")
def test_logout_invalidates_second_tab(authenticated_page, demo_url):
    page = authenticated_page
    second = page.context.new_page()
    second.goto(demo_url + "/web/index.php/dashboard/index", wait_until="domcontentloaded")
    expect(second.get_by_role("heading", name="Dashboard", exact=True)).to_be_visible()
    page.locator(".oxd-userdropdown-tab").click()
    page.get_by_role("menuitem", name="Logout").click()
    expect(page.get_by_role("button", name="Login", exact=True)).to_be_visible()
    second.reload(wait_until="domcontentloaded")
    expect(second).to_have_url(re.compile(r"/auth/login$"))
    expect(second.get_by_role("button", name="Login", exact=True)).to_be_visible()


@pytest.mark.scenario("AUTH-016", coverage="partial", variation="Back, Reload and protected read; no write attempted")
def test_back_after_logout_does_not_restore_session(authenticated_page, demo_url):
    page = authenticated_page
    page.locator(".oxd-userdropdown-tab").click()
    page.get_by_role("menuitem", name="Logout").click()
    expect(page.get_by_role("button", name="Login", exact=True)).to_be_visible()
    page.go_back(wait_until="domcontentloaded")
    page.reload(wait_until="domcontentloaded")
    page.goto(demo_url + "/web/index.php/dashboard/index", wait_until="domcontentloaded")
    expect(page).to_have_url(re.compile(r"/auth/login$"))
    expect(page.get_by_role("button", name="Login", exact=True)).to_be_visible()
