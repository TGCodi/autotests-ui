from playwright.sync_api import Page, expect

from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Локаторы
        self.DASHBOARD_TITLE = page.get_by_test_id("dashboard-toolbar-title-text")


    def dashboard_tiile_visibility(self):
        expect(self.DASHBOARD_TITLE).to_be_visible()
        expect(self.DASHBOARD_TITLE).to_have_text("Dashboard")