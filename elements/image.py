import allure
from elements.base_element import BaseElement


class Image(BaseElement):
    @property
    def type_of(self) -> str:
        return "image"

    def upload_image(self, file: str, nth: int = 0, **kwargs):
        with allure.step(f'{self.name} {self.type_of} from "{file}"'):
            locator = self.get_locator(nth, **kwargs)
            return locator.set_input_files(file)