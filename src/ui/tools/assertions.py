from typing import Any, Optional

import allure
from playwright.sync_api import Page, expect

from src.ui.pages import BasePage
from src.utils.tools import Constants


class Assertions(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @allure.step(title="Проверка URL")
    def check_url(
        self, uri: str, timeout: int = 10000, msg: Optional[str] = None
    ) -> None:
        expect(actual=self.page, msg=msg).to_have_url(
            url=f"{Constants.base_url_ui}/{uri}", timeout=timeout
        )

    @allure.step(title="Проверка наличия текста у элемента")
    def have_text(
        self, locator: str, text: str, msg: Optional[str] = None
    ) -> None:
        loc = self.page.locator(selector=locator)
        expect(actual=loc, msg=msg).to_have_text(text=text)

    @allure.step(title="Проверка видимости элемента на странице")
    def check_presence(
        self, locator: str, timeout: int = 10000, msg: Optional[str] = None
    ) -> None:
        loc = self.page.locator(selector=locator)
        expect(actual=loc, msg=msg).to_be_visible(
            visible=True, timeout=timeout
        )

    @allure.step(title="Проверка, что элемент скрыт")
    def check_absence(
        self, locator: str, timeout: int = 500, msg: Optional[str] = None
    ) -> None:
        loc = self.page.locator(selector=locator)
        expect(actual=loc, msg=msg).to_be_hidden(timeout=timeout)

    @allure.step("Проверка равенства")
    def check_equals(
        self, first: Any, second: Any, msg: Optional[str] = None
    ) -> None:
        assert first == second, msg

    @allure.step(title="Проверка, что кнопка не активна")
    def button_is_disabled(
        self, locator: str, msg: Optional[str] = None
    ) -> tuple[bool, Optional[str]]:
        button = self.page.locator(selector=locator)
        return button.is_disabled(), msg

    def element_disables(
        self, locator: str, msg: Optional[str] = None
    ) -> None:
        loc = self.page.locator(selector=locator)
        expect(actual=loc, msg=msg).to_be_disabled()

    @allure.step(title="Проверка что URI входит в URL страницы")
    def check_url_content(self, uri: str, msg: Optional[str] = None) -> None:
        assert f"{uri}" in self.page.url, msg

    @allure.step(title="Проверка, что элемент можно редактировать (текст)")
    def to_be_editable(self, locator: str, msg: Optional[str] = None) -> None:
        loc = self.page.locator(selector=locator)
        expect(actual=loc, msg=msg).to_be_editable()

    @allure.step(title="Проверка, что элемент содержит текст")
    def contain_text(
        self, locator: str, text: str, msg: Optional[str] = None
    ) -> None:
        loc = self.page.locator(selector=locator)
        expect(actual=loc, msg=msg).to_contain_text(text=text)
