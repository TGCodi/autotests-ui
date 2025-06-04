import allure
import pytest
from allure_commons.types import Severity

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag

@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page_with_state: CoursesListPage):
        courses_list_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_list_page_with_state.navbar.check_visible("username")

        courses_list_page_with_state.sidebar.check_visible()

        courses_list_page_with_state.toolbar_view.check_visible()

        courses_list_page_with_state.check_visible_empty_view()

    @pytest.mark.courses
    @pytest.mark.regression
    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page_with_state: CoursesListPage, create_course_page_with_state: CreateCoursePage):
        courses_list_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page_with_state.create_course_toolbar_view.check_visible()

        create_course_page_with_state.image_upload_widget.check_visible(is_image_uploaded=False)

        create_course_page_with_state.create_course_form.check_visible(
            title="",
            estimated_time="",
            description="",
            max_score="0",
            min_score="0"
        )
        create_course_page_with_state.create_course_exercises_toolbar_view.check_visible()

        create_course_page_with_state.check_visible_exercises_empty_view()

        create_course_page_with_state.image_upload_widget.upload_preview_image("./testdata/files/image.png")
        create_course_page_with_state.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page_with_state.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page_with_state.create_course_toolbar_view.click_create_course_button()

        courses_list_page_with_state.toolbar_view.check_visible()

        courses_list_page_with_state.course_view.check_visible(
            index= 0,
            title= "Playwright",
            estimated_time= "2 weeks",
            max_score= "100",
            min_score= "10"
        )

    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, courses_list_page_with_state: CoursesListPage, create_course_page_with_state: CreateCoursePage):
        create_course_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        create_course_page_with_state.image_upload_widget.upload_preview_image("./testdata/files/image.png")
        create_course_page_with_state.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page_with_state.create_course_form.fill(
            title="Python",
            estimated_time="4 weeks",
            description="Hello, world!",
            max_score="99",
            min_score="9"
        )
        create_course_page_with_state.create_course_toolbar_view.click_create_course_button()

        courses_list_page_with_state.course_view.check_visible(
            index=0,
            title="Python",
            estimated_time="4 weeks",
            max_score="99",
            min_score="9"
        )

        courses_list_page_with_state.course_view.menu.click_edit(0)

        create_course_page_with_state.create_course_form.fill(
            title="Playwright",
            estimated_time="99 weeks",
            description="Is Best",
            max_score="77",
            min_score="7"
        )
        create_course_page_with_state.create_course_toolbar_view.click_create_course_button()

        courses_list_page_with_state.course_view.check_visible(
            index=0,
            title="Playwright",
            estimated_time="99 weeks",
            max_score="77",
            min_score="7"
        )