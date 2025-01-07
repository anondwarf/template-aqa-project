from playwright.sync_api import (
    sync_playwright,
    Playwright,
    Page,
    Browser,
    BrowserContext,
)
from pytest import Parser, FixtureRequest, fixture


def pytest_addoption(parser: Parser) -> None:
    """Пользовательские опции командной строки"""
    parser.addoption(
        "--bn",
        action="store_true",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Выбор браузера",
    )
    parser.addoption(
        "--h",
        action="store_true",
        default=True,
        choices=[True, False],
        help="Включение режима headless браузера",
    )
    parser.addoption(
        "--s",
        action="store_true",
        default={"width": 1920, "height": 1080},
        choices=[
            {"width": 1920, "height": 1080},
            {"width": 1366, "height": 720},
        ],
        help="Разрешение браузера",
    )
    parser.addoption(
        "--t", action="store_true", default=60000, help="Выбор таймаута"
    )


@fixture(scope="class")
def browser(request: FixtureRequest) -> Page:
    playwright: Playwright = sync_playwright().start()
    if request.config.getoption("bn") == "firefox":
        browser = get_firefox_browser(playwright=playwright, request=request)
        context = get_context(browser=browser, request=request, start="local")
        page_data = context.new_page()
    else:
        browser = get_chrome_browser(playwright=playwright, request=request)
        context = get_context(browser=browser, request=request, start="local")
        page_data = context.new_page()

    yield page_data

    for _ in browser.contexts:
        context.close()
    
    browser.close()
    playwright.stop()


def get_firefox_browser(
    playwright: Playwright, request: FixtureRequest
) -> Browser:
    return playwright.firefox.launch(
        headless=request.config.getoption("h"),
    )


def get_chrome_browser(
    playwright: Playwright, request: FixtureRequest
) -> Browser:
    return playwright.chromium.launch(
        headless=request.config.getoption("h"),
    )


def get_context(
    browser: Browser, request: FixtureRequest, start: str
) -> BrowserContext:
    if start == "local":
        context = browser.new_context(no_viewport=True)
        context.set_default_timeout(
            timeout=request.config.getoption("t"),
        )
        # context.add_cookies(
        #     [{"url": "https://example.ru", "name": "ab_test", "value": "d"}]
        # )
        return context
    elif start == "remote":
        context = browser.new_context(
            viewport=request.config.getoption("s"),
        )
        context.set_default_timeout(
            timeout=request.config.getoption("t"),
        )
        # context.add_cookies(
        #     [{"url": "https://example.ru", "name": "ab_test", "value": "d"}]
        # )
        return context
