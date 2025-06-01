from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')


    def fill(self, email: str, username:str, password:str):   # Метод для заполения формы регистрации
        self.email_input.fill(email)    # Ввод email

        self.username_input.fill(username)  # Ввод username

        self.password_input.fill(password)  # Ввод password

    def check_visible(self, email: str, username: str, password: str):
        expect(self.email_input).to_be_visible(email)    # Проверка поля email
        expect(self.email_input).to_have_value()

        expect(self.username_input).to_be_visible() # Проверка поля username
        expect(self.username_input).to_have_value(username)

        expect(self.password_input).to_be_visible() # Проверка поля password
        expect(self.password_input).to_have_value(password)
