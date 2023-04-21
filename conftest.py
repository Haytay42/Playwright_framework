import pytest
from playwright.sync_api import Playwright, sync_playwright


@pytest.fixture(scope='session')
def playwright() -> Playwright:  # определяем фикстуру playwright, которая создает экземпляр класса Playwright.
    with sync_playwright() as playwright: # создает экземпляр класса Playwright с помощью функции sync_playwright и передает его в переменную playwright.
        yield playwright # возвращает playwright как результат выполнения фикстуры


@pytest.fixture(scope='session')
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    yield browser
    context.close()
    browser.close()


@pytest.fixture(scope='function')
def page(context):
    page = context.new_page()
    yield page
    page.close()
