import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button

class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_title = Text(page,'create-course-toolbar-title-text', 'Create title')
        self.create_button = Button(page,'create-course-toolbar-create-course-button', 'Create')

    @allure.step('Check visible "Create course" title')
    def check_visible(self, is_create_course_disabled=True):
        self.create_title.check_visible()
        self.create_title.check_have_text('Create course')

        self.create_button.check_visible()
        self.create_button.check_disabled()

        if not is_create_course_disabled:
            self.create_button.check_visible()
            self.create_button.check_enabled()

    @allure.step('Click create course button')
    def click_create_course_button(self):
        self.create_button.click()
