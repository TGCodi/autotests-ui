import pytest

from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.registration_form.fill(
        email="user.name@gmail.com",
        username="username",
        password="password"
    )
    registration_page.click_registration_button()
    registration_page.dashboard_tool_bar_view.check_visible()
