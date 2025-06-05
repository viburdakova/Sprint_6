import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    @allure.step("Кликнуть на вопрос")
    def click_question(self, number):
        locator = self.format_locator(MainPageLocators.QUESTIONS_LOCATOR, number)
        self.scroll_into_view_and_click(locator, MainPageLocators.QUESTIONS_LOCATOR_TO_SCROLL)

    @allure.step("Получить ответ на вопрос")
    def get_answer_text(self, number):
        locator = self.format_locator(MainPageLocators.ANSWER_LOCATOR, number)
        return self.get_text(locator)

    @allure.step("Кликнуть на верхнюю кнопку")
    def click_order_button_top(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step("Кликнуть на нижнюю кнопку")
    def click_order_button_bottom(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON_HEADER)

