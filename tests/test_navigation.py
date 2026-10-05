import re
import pytest
from playwright.sync_api import expect

@pytest.mark.parametrize("module,path,content", [
    ("Admin", "/admin/viewSystemUsers", "System Users"),
    ("PIM", "/pim/viewEmployeeList", "Employee Information"),
    ("Directory", "/directory/viewDirectory", "Directory"),
])
def test_module_navigation(authenticated_page, module, path, content):
    page = authenticated_page
    page.get_by_role("link", name=module, exact=True).click()
    expect(page).to_have_url(re.compile(re.escape(path) + r"(?:\?.*)?$"))
    # Assert the search panel title, not the similarly named top navigation title.
    expect(page.get_by_role("heading", name=content, level=5, exact=True)).to_be_visible()
    expect(page.get_by_role("button", name="Search", exact=True)).to_be_visible()
    page.get_by_role("link", name="Dashboard", exact=True).click()
    expect(page.get_by_role("heading", name="Dashboard", exact=True)).to_be_visible()
