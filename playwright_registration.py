from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
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

    # Проверяем заголовок "Dashboard"
    dashboard_label = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_label).to_have_text('Dashboard')
