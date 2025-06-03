import pytest

from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_displaying(dashboard_page: DashboardPage):
    dashboard_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    dashboard_page.sidebar.check_visible()

    dashboard_page.navbar.check_visible("username")

    dashboard_page.dashboard_tool_bar_view.check_visible()

    dashboard_page.scores_chart_view.check_visible("Scores")
    dashboard_page.courses_chart_view.check_visible("Courses")
    dashboard_page.students_chart_view.check_visible("Students")
    dashboard_page.activities_chart_view.check_visible("Activities")