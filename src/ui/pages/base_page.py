import allure
from playwright.sync_api import Page, Response

from src.utils.tools import Constants


class BasePage(object):
    """Класс конструктор для всех классов `*Page`"""

    def __init__(self, page: Page) -> None:
        self.page = page

    @allure.step(title="Открытие страницы")
    def open(self, uri: str) -> Response | None:
        return self.page.goto(
            url=f"{Constants.base_url_ui}/{uri}", wait_until="domcontentloaded"
        )

    @allure.step(title="Клик по элементу")
    def click(self, locator: str) -> None:
        self.page.click(selector=locator)

    @allure.step(title="Двойной клик по элементу")
    def double_click(self, locator: str) -> None:
        self.page.dblclick(selector=locator)

    @allure.step(title="Ввод текста")
    def enter_text(self, locator: str, text: str, nth: int = 0) -> None:
        self.page.locator(selector=locator).nth(index=nth).type(text=text)

    @allure.step(title="Получить текст элемента")
    def get_text(self, locator: str, nth: int = 0) -> str:
        return (
            self.page.locator(selector=locator).nth(index=nth).text_content()
        )

    @allure.step(title="Ожидание загрузки элемента")
    def wait_for_element(self, locator: str, timeout: int = 12000) -> None:
        self.page.wait_for_selector(selector=locator, timeout=timeout)

    @allure.step(title="Ожидание загрузки всех элементов")
    def wait_for_all_element(self, locator: str, timeout: int = 12000) -> None:
        elements = self.page.query_selector_all(selector=locator)

        for _ in elements:
            self.wait_for_element(selector=locator, timeout=timeout)

    @allure.step(title="Получение текущего URL страницы")
    def current_url(self) -> str:
        return self.page.url

    @allure.step(title="Проверка, что элемент отображен на странице")
    def is_element_present(self, locator: str, timeout: int = 10000) -> bool:
        try:
            self.page.wait_for_selector(selector=locator, timeout=timeout)
        except TimeoutError:
            return False
        return True

    @allure.step(title="Проверка, что элемент не отображен на странице")
    def is_element_not_present(
        self, locator: str, timeout: int = 10000
    ) -> bool:
        try:
            self.page.wait_for_selector(selector=locator, timeout=timeout)
        except TimeoutError:
            return True
        return False

    def refresh_page(self) -> Response | None:
        return self.page.reload(wait_until="domcontentloaded")
