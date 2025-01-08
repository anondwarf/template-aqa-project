from playwright.sync_api import Page

from src.ui.pages import BasePage
from src.ui.tools import Constants, Assertions


class _Locators(object):
    """Локаторы страницы `LoginPage`"""

    LOGIN_INPUT: str = ""
    PASSWORD_INPUT: str = ""
    SUBMIT_BUTTON: str = ""


class LoginPage(BasePage):
    """Страница авторизации"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.assertion = Assertions(page)

    def user_login(self):
        self.open("")
        self.enter_text(locator=_Locators.LOGIN_INPUT, text=Constants.login)
        self.enter_text(
            locator=_Locators.PASSWORD_INPUT, text=Constants.password
        )
        self.click(locator=_Locators.SUBMIT_BUTTON)
        self.assertion.check_url(uri="", msg="Не верный URI")
        # TODO нужна проверка на наличие, наполнение и время изменения browser_state
        self.page.context.storage_state(path=Constants.browser_state)
