from elements.base_element import BaseElement


class Image(BaseElement):
    def upload_image(self, file: str, **kwargs):
        locator = self.get_locator(**kwargs)
        return locator.set_input_files(file)