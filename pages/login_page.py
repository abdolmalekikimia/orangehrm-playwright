import re
from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url
        self.username = page.get_by_placeholder("Username", exact=True)
        self.password = page.get_by_placeholder("Password", exact=True)
        self.submit = page.get_by_role("button", name="Login", exact=True)

    def open(self):
        self.page.goto(self.base_url + "/web/index.php/auth/login", wait_until="domcontentloaded")
        expect(self.submit).to_be_visible()

    def sign_in(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.submit.click()

    def expect_dashboard(self):
        expect(self.page).to_have_url(re.compile(r"/dashboard/index(?:\?.*)?$"))
        expect(self.page.get_by_role("heading", name="Dashboard", exact=True)).to_be_visible()
