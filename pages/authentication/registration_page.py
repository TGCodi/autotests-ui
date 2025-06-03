import re

from playwright.sync_api import Page

from components.authentication.registration_form_component import RegistrationFormComponent

from elements.button import Button
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = Button(page,'registration-page-registration-button', 'Registration')

    def click_registration_button(self):    # Клик по кнопке регистрации
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()
        # Добавили проверку
        self.check_current_url(re.compile(".*/#/auth/login"))



