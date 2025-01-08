import pytest
from playwright.sync_api import Page

from src.ui.pages.login_page import LoginPage


@pytest.fixture(scope="class")
@pytest.mark.usefixtures("browser")
def user_login(browser: Page):
    login_page = LoginPage(page=browser)
    login_page.user_login()
