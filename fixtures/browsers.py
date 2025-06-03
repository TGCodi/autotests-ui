import pytest
from playwright.sync_api import Playwright, Page

from pages.authentication.registration_page import RegistrationPage


@pytest.fixture(scope="session")    # Фикстура для получения кредов пользака
def initialize_browser_state(playwright: Playwright) -> Page:
# Открываем браузер с использованием Playwright
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email='user.name@gmail.com', username='username',password='password')
    registration_page.click_registration_button()

    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path='browser-state.json')

@pytest.fixture     # Фикстура для открытия залогиненого пользака
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')  # Указываем файл с сохраненным состоянием
        page = context.new_page()
        yield page
        browser.close()


@pytest.fixture     # Фикстура для открытьия браузера
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()
