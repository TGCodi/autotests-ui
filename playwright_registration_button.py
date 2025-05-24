from playwright.sync_api import sync_playwright, expect

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()  # Создаем новую страницу()

    #  Переходим на страницу регистрации
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Находим кнопку "Registration" и проверяем состояние
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).not_to_be_enabled()

    # Находим поле "Email" и заполняем его
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill('user.name@gmail.com')

    # Находим поле "Username" и заполняем его
    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill('username')

    # Находим поле "Password" и заполняем его
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill('password')

    # Проверяем состояние кнопки "Registarion"
    expect(registration_button).to_be_enabled()