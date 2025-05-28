import pytest
from playwright.sync_api import expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    # Переходим на страницу с курсом
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    # проверяем наличие и текст заголовка "Courses"
    title_text = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(title_text).to_be_visible()
    expect(title_text).to_contain_text('Courses')

    # проверяем иконку папки
    title_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(title_icon).to_be_visible()

    # проверяем текст блока "There is no results"
    empty_view_title_locator = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_view_title_locator).to_contain_text('There is no results')

    # проверяем описание блока "There is no results"
    empty_view_description_locator = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_view_description_locator).to_contain_text(
        'Results from the load test pipeline will be displayed here')




