from typing_extensions import Pattern

import allure
from playwright.sync_api import Page, expect


class BasePage:
    # Конструктор класса, принимающий объект Page
    def __init__(self, page : Page):
        self.page = page    # Присваиваем объект page атрибуту класса


    def visit(self, url: str):
        with allure.step(f'opening "{url}"'):
            self.page.goto(url, wait_until="networkidle")

    def reload(self):   # Метод для перезагрузки страницы
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            self.page.reload(wait_until="domcontentloaded")

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Checking that current url matches pattern "{expected_url.pattern}"'):
            expect(self.page).to_have_url(expected_url)