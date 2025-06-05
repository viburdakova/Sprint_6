import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from data import data
from data.data import MAIN_URL, ORDER_URL
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture(scope="function")
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.go_to_url(data.MAIN_URL)
    return page

@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    return  page