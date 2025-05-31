from playwright.sync_api import Page, expect

from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Локаторы
        self.DASHBOARD_TITLE = page.get_by_test_id("dashboard-toolbar-title-text")
        self.STUDENTS_TITLE = page.get_by_test_id('students-widget-title-text')
        self.STUDENTS_CHART = page.get_by_test_id('students-bar-chart')

        self.ACTIVITIES_TITLE = page.get_by_test_id('activities-widget-title-text')
        self.ACTIVITIES_CHART = page.get_by_test_id('activities-line-chart')

        self.COURSES_TITLE = page.get_by_test_id('courses-widget-title-text')
        self.COURSES_CHART = page.get_by_test_id('courses-pie-chart')

        self.SCORES_TITLE = page.get_by_test_id('scores-widget-title-text')
        self.SCORES_CHART = page.get_by_test_id('scores-scatter-chart')

    def check_visible_dashboard_title(self):
        expect(self.DASHBOARD_TITLE).to_be_visible()
        expect(self.DASHBOARD_TITLE).to_have_text('Dashboard')

    def check_visible_students_chart(self):
        expect(self.STUDENTS_TITLE).to_be_visible()
        expect(self.STUDENTS_TITLE).to_have_text('Students')
        expect(self.STUDENTS_CHART).to_be_visible()

    def check_visible_courses_chart(self):
        expect(self.COURSES_TITLE).to_be_visible()
        expect(self.COURSES_TITLE).to_have_text('Courses')
        expect(self.COURSES_CHART).to_be_visible()

    def check_visible_activities_chart(self):
        expect(self.ACTIVITIES_TITLE).to_be_visible()
        expect(self.ACTIVITIES_TITLE).to_have_text('Activities')
        expect(self.ACTIVITIES_CHART).to_be_visible()

    def check_visible_scores_chart(self):
        expect(self.SCORES_TITLE).to_be_visible()
        expect(self.SCORES_TITLE).to_have_text('Scores')
        expect(self.SCORES_CHART).to_be_visible()