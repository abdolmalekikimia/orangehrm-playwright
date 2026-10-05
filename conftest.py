import os
import pytest
from playwright.sync_api import expect

@pytest.fixture(scope="session")
def demo_url():
    return os.getenv("ORANGEHRM_URL", "https://opensource-demo.orangehrmlive.com").rstrip("/")

@pytest.fixture(scope="session")
def credentials():
    # Public credentials displayed by the OrangeHRM demo itself.
    return os.getenv("ORANGEHRM_USERNAME", "Admin"), os.getenv("ORANGEHRM_PASSWORD", "admin123")

@pytest.fixture(autouse=True)
def timeouts(page):
    expect.set_options(timeout=15000)
    page.set_default_timeout(30000)
    page.set_default_navigation_timeout(60000)

@pytest.fixture
def login(page, demo_url):
    from pages.login_page import LoginPage
    model = LoginPage(page, demo_url)
    model.open()
    return model

@pytest.fixture
def authenticated_page(login, credentials):
    login.sign_in(*credentials)
    login.expect_dashboard()
    return login.page
