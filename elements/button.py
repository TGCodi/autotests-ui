import allure
from playwright.sync_api import expect, Locator
from ui_coverage_tool import ActionType

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("BUTTON")


class Button(BaseElement):
    @property
    def type_of(self) -> str:
        return "button"

    def get_locator(self, nth: int = 0,  **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs)

    def get_raw_locator(self, nth: int =0, **kwargs) -> str:
        return f'{super().get_locator(**kwargs)}'

    def check_enabled(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is enabled'

        with allure.step(step):
            logger.info(step)
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_enabled()

        self.track_coverage(ActionType.FILL, nth, **kwargs)

    def check_disabled(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is disabled'

        with allure.step(step):
            logger.info(step)
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_disabled()

        self.track_coverage(ActionType.FILL, nth, **kwargs)
        