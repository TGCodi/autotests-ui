from elements.base_element import BaseElement


class Image(BaseElement):
    def upload_image(self, file: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        return locator.set_input_files(file)