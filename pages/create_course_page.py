from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Заголовок и кнопка создания курса
        self.CREATE_COURSE_TITLE = page.get_by_test_id('create-course-toolbar-title-text')
        self.CREATE_COURSE_BUTTON = page.get_by_test_id('create-course-toolbar-create-course-button')

        # Картинка предпросмотра и блок предпросмотра картинки курса
        self.PREVIEW_IMAGE = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')
        self.PREVIEW_EMPTY_VIEW_ICON = page.get_by_test_id('create-course-preview-empty-view-icon')
        self.PREVIEW_EMPTY_VIEW_TITLE = page.get_by_test_id('create-course-preview-empty-view-title-text')
        self.PREVIEW_EMPTY_VIEW_DESCRIPTION = page.get_by_test_id('create-course-preview-empty-view-description-text')

        # Кнопка загрузки, удаления картинки предпросмотра курса и блок с информацией о загружаемой картинке
        self.PREVIEW_IMAGE_UPLOAD_ICON = page.get_by_test_id('create-course-preview-image-upload-widget-info-icon')
        self.PREVIEW_IMAGE_UPLOAD_TITLE = page.get_by_test_id(
            'create-course-preview-image-upload-widget-info-title-text')
        self.PREVIEW_IMAGE_UPLOAD_DESCRIPTION = page.get_by_test_id(
            'create-course-preview-image-upload-widget-info-description-text'
        )
        self.PREVIEW_IMAGE_UPLOAD_BUTTON = page.get_by_test_id(
            'create-course-preview-image-upload-widget-upload-button'
        )
        self.PREVIEW_IMAGE_REMOVE_BUTTON = page.get_by_test_id(
            'create-course-preview-image-upload-widget-remove-button'
        )
        self.PREVIEW_IMAGE_UPLOAD_INPUT = page.get_by_test_id('create-course-preview-image-upload-widget-input')

        # Форма создания курса
        self.CREATE_COURSE_TITLE_INPUT = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.CREATE_COURSE_ESTIMATED_TIME_INPUT = (
            page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        )
        self.CREATE_COURSE_DESCRIPTION_TEXTAREA = (
            page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        )
        self.CREATE_COURSE_MAX_SCORE_INPUT = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.CREATE_COURSE_MIN_SCORE_INPUT = page.get_by_test_id('create-course-form-min-score-input').locator('input')

        # Заголовок и кнопка создания задания
        self.EXERCISES_TITLE = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.CREATE_EXERCISE_BUTTON = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

        # Блок, который отображется, когда в курсе нет заданий
        self.EXERCISES_EMPTY_VIEW_ICON = page.get_by_test_id('create-course-exercises-empty-view-icon')
        self.EXERCISES_EMPTY_VIEW_TITLE = page.get_by_test_id('create-course-exercises-empty-view-title-text')
        self.EXERCISES_EMPTY_VIEW_DESCRIPTION = page.get_by_test_id(
            'create-course-exercises-empty-view-description-text'
        )

    def check_visible_create_course_title(self):
        expect(self.CREATE_COURSE_TITLE).to_be_visible()
        expect(self.CREATE_COURSE_TITLE).to_have_text('Create course')

    def click_create_course_button(self):
        self.CREATE_COURSE_BUTTON.click()

    def check_visible_create_course_button(self):
        expect(self.CREATE_COURSE_BUTTON).to_be_visible()

    def check_disabled_create_course_button(self):
        expect(self.CREATE_COURSE_BUTTON).to_be_disabled()

    def check_visible_image_preview_empty_view(self):
        expect(self.PREVIEW_EMPTY_VIEW_ICON).to_be_visible()

        expect(self.PREVIEW_EMPTY_VIEW_TITLE).to_be_visible()
        expect(self.PREVIEW_EMPTY_VIEW_TITLE).to_have_text('No image selected')

        expect(self.PREVIEW_EMPTY_VIEW_DESCRIPTION).to_be_visible()
        expect(self.PREVIEW_EMPTY_VIEW_DESCRIPTION).to_have_text(
            'Preview of selected image will be displayed here'
        )

    def check_visible_image_upload_view(self, is_image_uploaded: bool = False):
        expect(self.PREVIEW_IMAGE_UPLOAD_ICON).to_be_visible()

        expect(self.PREVIEW_IMAGE_UPLOAD_TITLE).to_be_visible()
        expect(self.PREVIEW_IMAGE_UPLOAD_TITLE).to_have_text(
            'Tap on "Upload image" button to select file'
        )

        expect(self.PREVIEW_IMAGE_UPLOAD_DESCRIPTION).to_be_visible()
        expect(self.PREVIEW_IMAGE_UPLOAD_DESCRIPTION).to_have_text('Recommended file size 540X300')

        expect(self.PREVIEW_IMAGE_UPLOAD_BUTTON).to_be_visible()

        if is_image_uploaded:
            expect(self.PREVIEW_IMAGE_REMOVE_BUTTON).to_be_visible()

    def click_remove_image_button(self):
        self.PREVIEW_IMAGE_REMOVE_BUTTON.click()

    def check_visible_preview_image(self):
        expect(self.PREVIEW_IMAGE).to_be_visible()

    def upload_preview_image(self, file: str):
        self.PREVIEW_IMAGE_UPLOAD_INPUT.set_input_files(file)

    def check_visible_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        expect(self.CREATE_COURSE_TITLE_INPUT).to_be_visible()
        expect(self.CREATE_COURSE_TITLE_INPUT).to_have_value(title)

        expect(self.CREATE_COURSE_ESTIMATED_TIME_INPUT).to_be_visible()
        expect(self.CREATE_COURSE_ESTIMATED_TIME_INPUT).to_have_value(estimated_time)

        expect(self.CREATE_COURSE_DESCRIPTION_TEXTAREA).to_be_visible()
        expect(self.CREATE_COURSE_DESCRIPTION_TEXTAREA).to_have_value(description)

        expect(self.CREATE_COURSE_MAX_SCORE_INPUT).to_be_visible()
        expect(self.CREATE_COURSE_MAX_SCORE_INPUT).to_have_value(max_score)

        expect(self.CREATE_COURSE_MIN_SCORE_INPUT).to_be_visible()
        expect(self.CREATE_COURSE_MIN_SCORE_INPUT).to_have_value(min_score)

    def fill_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.CREATE_COURSE_TITLE_INPUT.fill(title)
        expect(self.CREATE_COURSE_TITLE_INPUT).to_have_value(title)

        self.CREATE_COURSE_ESTIMATED_TIME_INPUT.fill(estimated_time)
        expect(self.CREATE_COURSE_ESTIMATED_TIME_INPUT).to_have_value(estimated_time)

        self.CREATE_COURSE_DESCRIPTION_TEXTAREA.fill(description)
        expect(self.CREATE_COURSE_DESCRIPTION_TEXTAREA).to_have_value(description)

        self.CREATE_COURSE_MAX_SCORE_INPUT.fill(max_score)
        expect(self.CREATE_COURSE_MAX_SCORE_INPUT).to_have_value(max_score)

        self.CREATE_COURSE_MIN_SCORE_INPUT.fill(min_score)
        expect(self.CREATE_COURSE_MIN_SCORE_INPUT).to_have_value(min_score)

    def check_visible_exercises_title(self):
        expect(self.EXERCISES_TITLE).to_be_visible()
        expect(self.EXERCISES_TITLE).to_have_text('Exercises')

    def check_visible_create_exercise_button(self):
        expect(self.CREATE_EXERCISE_BUTTON).to_be_visible()

    def click_create_exercise_button(self):
        self.CREATE_EXERCISE_BUTTON.click()

    def check_visible_exercises_empty_view(self):
        expect(self.EXERCISES_EMPTY_VIEW_ICON).to_be_visible()

        expect(self.EXERCISES_EMPTY_VIEW_TITLE).to_be_visible()
        expect(self.EXERCISES_EMPTY_VIEW_TITLE).to_have_text('There is no exercises')

        expect(self.EXERCISES_EMPTY_VIEW_DESCRIPTION).to_be_visible()
        expect(self.EXERCISES_EMPTY_VIEW_DESCRIPTION).to_have_text(
            'Click on "Create exercise" button to create new exercise'
        )

    def click_delete_exercise_button(self, index: int):
        delete_exercise_button = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-delete-exercise-button"
        )
        delete_exercise_button.click()

    def check_visible_create_exercise_form(self, index: int, title: str, description: str):
        exercise_subtitle = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-subtitle-text"
        )
        exercise_title_input = self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        )
        exercise_description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        )

        expect(exercise_subtitle).to_be_visible()
        expect(exercise_subtitle).to_have_text(f"#{index + 1} Exercise")

        expect(exercise_title_input).to_be_visible()
        expect(exercise_title_input).to_have_value(title)

        expect(exercise_description_input).to_be_visible()
        expect(exercise_description_input).to_have_value(description)

    def fill_create_exercise_form(self, index: int, title: str, description: str):
        exercise_title_input = self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        )
        exercise_description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        )

        exercise_title_input.fill(title)
        expect(exercise_title_input).to_have_value(title)

        exercise_description_input.fill(description)
        expect(exercise_description_input).to_have_value(description)