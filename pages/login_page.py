from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        # Локаторы
        self.EMAIL_INPUT = page.get_by_test_id('login-form-email-input').locator('input')
        self.PASSWORD_INPUT = page.get_by_test_id('login-form-password-input').locator('input')
        self.LOGIN_BUTTON = page.get_by_test_id('login-page-login-button')
        self.REGISTRATION_LINK = page.get_by_test_id('login-page-registration-link')
        self.WRONG_EMAIL_OR_PASSWORD_ALERT = page.get_by_test_id('login-page-wrong-email-or-password-alert')

    def fill_login_form(self, email: str, password: str):   # Метод для заполнения формы авторизации
        self.EMAIL_INPUT.fill(email)
        expect(self.EMAIL_INPUT).to_have_value(email)   # Проверяем, что email введен корректно

        self.PASSWORD_INPUT.fill(password)
        expect(self.PASSWORD_INPUT).to_have_value(password) # Проверяем, что пароль введен корректно

    def click_login_button(self):   # Метод для нажатия на кнопку "Login"
        self.LOGIN_BUTTON.click()

    def click_registration_link(self):  # Метод для нажатия на ссылку "Registration"
        self.REGISTRATION_LINK.click()

    def check_visible_wrong_email_or_password_alert(self):  # Метод для проверки отображения алерта с ошибкой
        expect(self.WRONG_EMAIL_OR_PASSWORD_ALERT).to_be_visible()
        expect(self.WRONG_EMAIL_OR_PASSWORD_ALERT).to_have_text("Wrong email or password")