import allure
import pytest


from data import data
from locators.main_page_locators import MainPageLocators
from conftest import main_page, order_page, driver



class TestOrderPage:

    @pytest.mark.parametrize(
        'order_button_locator, order_data',
        [
            (MainPageLocators.ORDER_BUTTON_HEADER, data.ORDER_DATA_1),
            (MainPageLocators.ORDER_BUTTON_DOWN_1, data.ORDER_DATA_2)
        ]
    )
    def test_order_creation(self, main_page, order_page, order_button_locator, order_data):

        with allure.step("Открыть форму заказа"):
            main_page.scroll_into_view_and_click(order_button_locator, order_button_locator)

        with allure.step("Заполнить первую страницу формы"):
            order_page.fill_first_page(order_data)

        with allure.step("Заполнить вторую страницу формы"):
            order_page.fill_second_page(order_data)

        with allure.step("Проверить успешное оформление"):
            assert order_page.check_success_order()

        with allure.step("Открыть статус заказа"):
            order_page.open_order()

        with allure.step("Перейти на главную страницу"):
            order_page.go_to_scooter_main_page()

        with allure.step("Перейти на страницу Яндекс Дзена"):
            order_page.go_to_yandex_dzen()
