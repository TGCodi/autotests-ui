import pytest
from playwright.sync_api import Playwright, Page

@pytest.fixture(scope="session")    # Фикстура для получения кредов пользака
def initialize_browser_state(playwright: Playwright) -> Page:
# Открываем браузер с использованием Playwright
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Переходим на страницу регистрации
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Находим поле "Email" и заполняем его
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill('user.name@gmail.com')

    # Находим поле "Username" и заполняем его
    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill('username')

    # Находим поле "Password" и заполняем его
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill('password')

    # Находим кнопку "Registration" и кликаем на нее
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

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
