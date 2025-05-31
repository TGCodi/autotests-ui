from playwright.sync_api import Page, expect

from pages.base_page import BasePage

class RegistrationPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        # Локаторы
        self.EMAIL_INPUT = page.get_by_test_id('registration-form-email-input').locator('input')
        self.USERNAME_INPUT = page.get_by_test_id('registration-form-username-input').locator('input')
        self.PASSWORD_INPUT = page.get_by_test_id('registration-form-password-input').locator('input')
        self.REGISTRATION_BUTTON = page.get_by_test_id('registration-page-registration-button')

    def fill_registration_form(self, email: str, username:str, password:str):   # Метод для заполения формы регистрации

        self.EMAIL_INPUT.fill(email)    # Ввод email
        expect(self.EMAIL_INPUT).to_have_value(email)   # Проверка поля email

        self.USERNAME_INPUT.fill(username)  # Ввод username
        expect(self.USERNAME_INPUT).to_have_value(username) # Проверка поля username

        self.PASSWORD_INPUT.fill(password)  # Ввод password
        expect(self.PASSWORD_INPUT).to_have_value(password) # Проверка поля password

    def click_registration_button(self):    # Клик по кнопке регистрации
        self.REGISTRATION_BUTTON.click()



