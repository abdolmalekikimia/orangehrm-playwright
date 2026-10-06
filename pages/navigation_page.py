import re
from playwright.sync_api import expect


class NavigationPage:
    def __init__(self, page):
        self.page = page

    def open_module(self, name):
        self.page.get_by_role("link", name=name, exact=True).click()

    def expect_destination(self, spec):
        expect(self.page).to_have_url(re.compile(spec["path_regex"] + r"(?:\?.*)?$"))
        if spec.get("stateful") == "attendance_punch":
            state = "In" if "/punchIn" in self.page.url else "Out"
            expect(self.page.get_by_role("heading", name="Punch " + state, exact=True)).to_be_visible()
        elif spec.get("heading"):
            expect(self.page.get_by_role("heading", name=spec["heading"], exact=True).last).to_be_visible()
        else:
            expect(self.page.get_by_text(spec["text"], exact=True)).to_be_visible()

    def open_submenu(self, spec):
        self.open_module(spec["module"])
        top = self.page.get_by_role("navigation", name="Topbar Menu", exact=True)
        top.get_by_text(spec["menu"], exact=True).click()
        # Manage Reviews has the same label as its parent; the last match is the menu item.
        top.get_by_text(spec["child"], exact=True).last.click()
        self.expect_destination(spec)

    def return_dashboard(self):
        self.open_module("Dashboard")
        expect(self.page.get_by_role("heading", name="Dashboard", exact=True)).to_be_visible()
