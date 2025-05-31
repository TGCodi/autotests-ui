import pytest
from playwright.sync_api import Page

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.parametrize(
        "email, username, password",
        [
                ("client@mail.com", "client", "password")
        ],
        ids=
        [
                "Successful registration"
        ]
)
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage, email: str, username: str, password: str ):  # Создаем тестовую функцию
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.fill_registration_form(email=email, username=username, password=password)
        registration_page.click_registration_button()
        dashboard_page.dashboard_tiile_visibility()