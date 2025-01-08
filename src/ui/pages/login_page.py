from playwright.sync_api import Page

from src.ui.pages import BasePage


class _Locators(object):
    """Локаторы страницы `LoginPage`"""


class LoginPage(BasePage):
    """Страница авторизации"""

    def __init__(self, page: Page):
        super().__init__(page)
