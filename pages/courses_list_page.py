from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.COURSES_TITLE = page.get_by_test_id('courses-list-toolbar-title-text')
        self.CREATE_COURSE_BUTTON = page.get_by_test_id('courses-list-toolbar-create-course-button')

        self.COURSE_TITLE = page.get_by_test_id('course-widget-title-text')
        self.COURSE_IMAGE = page.get_by_test_id('course-preview-image')
        self.COURSE_MAX_SCORE_TEXT = page.get_by_test_id('course-max-score-info-row-view-text')
        self.COURSE_MIN_SCORE_TEXT = page.get_by_test_id('course-min-score-info-row-view-text')
        self.COURSE_ESTIMATED_TIME_TEXT = page.get_by_test_id('course-estimated-time-info-row-view-text')

        self.COURSE_MENU_BUTTON = page.get_by_test_id('course-view-menu-button')
        self.COURSE_EDIT_MENU_ITEM = page.get_by_test_id('course-view-edit-menu-item')
        self.COURSE_DELETE_MENU_ITEM = page.get_by_test_id('course-view-delete-menu-item')

        self.EMPTY_VIEW_ICON = page.get_by_test_id('courses-list-empty-view-icon')
        self.EMPTY_VIEW_TITLE = page.get_by_test_id('courses-list-empty-view-title-text')
        self.EMPTY_VIEW_DESCRIPTION = page.get_by_test_id('courses-list-empty-view-description-text')

    def check_visible_courses_title(self):
        expect(self.COURSES_TITLE).to_be_visible()
        expect(self.COURSES_TITLE).to_have_text('Courses')

    def check_visible_empty_view(self):
        expect(self.EMPTY_VIEW_ICON).to_be_visible()

        expect(self.EMPTY_VIEW_TITLE).to_be_visible()
        expect(self.EMPTY_VIEW_TITLE).to_have_text('there is no results')

        expect(self.EMPTY_VIEW_DESCRIPTION).to_be_visible()
        expect(self.EMPTY_VIEW_DESCRIPTION).to_have_text(
            'results from the load test pipeline will be displayed here'
        )

    def check_visible_create_course_button(self):
        expect(self.CREATE_COURSE_BUTTON).to_be_visible()

    def click_create_course_button(self):
        self.CREATE_COURSE_BUTTON.click()

    def check_visible_course_card(
            self,
            index: int,
            title: str,
            max_score: str,
            min_score: str,
            estimated_time: str
    ):
        expect(self.COURSE_IMAGE.nth(index)).to_be_visible()

        expect(self.COURSE_TITLE.nth(index)).to_be_visible()
        expect(self.COURSE_TITLE.nth(index)).to_have_text(title)

        expect(self.COURSE_MAX_SCORE_TEXT.nth(index)).to_be_visible()
        expect(self.COURSE_MAX_SCORE_TEXT.nth(index)).to_have_text(f"Max score: {max_score}")

        expect(self.COURSE_MIN_SCORE_TEXT.nth(index)).to_be_visible()
        expect(self.COURSE_MIN_SCORE_TEXT.nth(index)).to_have_text(f"Min score: {min_score}")

        expect(self.COURSE_ESTIMATED_TIME_TEXT.nth(index)).to_be_visible()
        expect(self.COURSE_ESTIMATED_TIME_TEXT.nth(index)).to_have_text(
            f"Estimated time: {estimated_time}"
        )

    def click_edit_course(self, index: int):
        self.COURSE_MENU_BUTTON.nth(index).click()

        expect(self.COURSE_EDIT_MENU_ITEM.nth(index)).to_be_visible()
        self.COURSE_EDIT_MENU_ITEM.nth(index).click()

    def click_delete_course(self, index: int):
        self.COURSE_MENU_BUTTON.nth(index).click()

        expect(self.COURSE_DELETE_MENU_ITEM.nth(index)).to_be_visible()
        self.COURSE_DELETE_MENU_ITEM.nth(index).click()