import re
import pytest
from playwright.sync_api import expect

def test_successful_login(login, credentials):
    login.sign_in(*credentials)
    login.expect_dashboard()

def test_invalid_password_stays_on_login(login, credentials):
    login.sign_in(credentials[0], "intentionally-invalid-password")
    expect(login.page.get_by_text("Invalid credentials", exact=True)).to_be_visible()
    expect(login.submit).to_be_visible()
    expect(login.page).to_have_url(re.compile(r"/auth/login$"))

@pytest.mark.parametrize("username,password,errors", [("", "", 2), ("Admin", "", 1), ("", "admin123", 1)])
def test_required_fields(login, username, password, errors):
    login.sign_in(username, password)
    expect(login.page.get_by_text("Required", exact=True)).to_have_count(errors)
    expect(login.submit).to_be_visible()

def test_logout_blocks_dashboard(authenticated_page, demo_url):
    page = authenticated_page
    page.locator(".oxd-userdropdown-tab").click()
    page.get_by_role("menuitem", name="Logout").click()
    expect(page.get_by_role("button", name="Login", exact=True)).to_be_visible()
    page.goto(demo_url + "/web/index.php/dashboard/index", wait_until="domcontentloaded")
    expect(page).to_have_url(re.compile(r"/auth/login$"))
    expect(page.get_by_role("button", name="Login", exact=True)).to_be_visible()

def test_unauthenticated_dashboard_redirects(page, demo_url):
    page.goto(demo_url + "/web/index.php/dashboard/index", wait_until="domcontentloaded")
    expect(page).to_have_url(re.compile(r"/auth/login$"))
    expect(page.get_by_role("button", name="Login", exact=True)).to_be_visible()
