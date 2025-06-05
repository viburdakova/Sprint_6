
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from data.data import DZEN_URL
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):

    @allure.step("Заполнить первую страницу формы")
    def fill_first_page(self, data):
        self.add_text_element(OrderPageLocators.NAME_INPUT, data['name'])
        self.add_text_element(OrderPageLocators.SURNAME_INPUT, data['surname'])
        self.add_text_element(OrderPageLocators.ADDRESS_INPUT, data['address'])
        self.click_to_element(OrderPageLocators.METRO_STATION_SELECT)
        self.click_to_element(OrderPageLocators.STATION_OPTION)
        self.add_text_element(OrderPageLocators.PHONE_INPUT, data['phone'])
        self.click_to_element(OrderPageLocators.CONFIRM_BUTTON)
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить вторую страницу формы")
    def fill_second_page(self, data):
        self.wait_for_element(OrderPageLocators.DATA_INPUT)
        self.click_to_element(OrderPageLocators.DATA_INPUT)
        self.add_text_element(OrderPageLocators.DATA_INPUT, data['data'])
        self.wait_for_element(OrderPageLocators.DATA_INPUT)
        self.click_to_element(OrderPageLocators.EMPTY_CLICK)
        self.wait_for_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click_to_element(OrderPageLocators.RENTAL_OPTIONS_VISIBLE)
        self.click_to_element(MainPageLocators.ORDER_BUTTON_DOWN_2)
        self.click_to_element(MainPageLocators.ORDER_BUTTON_YES)

    @allure.step("Проверить успешное оформление заказа")
    def check_success_order(self):
        return self.wait_for_element(MainPageLocators.ORDER_SUCCESS).is_displayed()

    @allure.step("Открыть статус заказа")
    def open_order(self):
        self.driver.find_element(*MainPageLocators.ORDER_OPEN).click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("track?t"))

    @allure.step("Перейти на главную через логотип Самоката")
    def go_to_scooter_main_page(self):
        self.click_to_element(MainPageLocators.LOGO_SCOOTER)
        WebDriverWait(self.driver, 5).until(EC.url_contains("qa-scooter."))

    @allure.step("Перейти в Дзен через логотип Яндекса")
    def go_to_yandex_dzen(self):
        current_windows = self.driver.window_handles
        self.click_to_element(MainPageLocators.LOGO_YANDEX)

        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.window_handles) > len(current_windows))

        new_window = [handle for handle in self.driver.window_handles
                      if handle not in current_windows][0]
        self.driver.switch_to.window(new_window)

        WebDriverWait(self.driver, 15).until(
            EC.url_contains("dzen.ru"))