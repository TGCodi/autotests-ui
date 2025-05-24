from playwright.sync_api import sync_playwright, expect

# Открываем браузер с использованием Playwright
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    contex = browser.new_context()
    page = contex.new_page()

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
    contex.storage_state(path='browser-state.json')


# Открываем браузер с использованием Playwright
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    contex = browser.new_context(storage_state='browser-state.json')        # Указываем файл с сохраненным состоянием
    page = contex.new_page()

    # Переходим на страницу с курсом
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    # проверяем наличие и текст заголовка "Courses"
    title_text = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(title_text).to_be_visible()
    expect(title_text).to_contain_text('Courses')

    # проверяем иконку папки
    title_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(title_icon).to_be_visible()

    # проверяем текст блока "There is no results"
    empty_view_title_locator = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_view_title_locator).to_contain_text('There is no results')

    # проверяем описание блока "There is no results"
    empty_view_description_locator = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_view_description_locator).to_contain_text('Results from the load test pipeline will be displayed here')

