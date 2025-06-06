from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = By.XPATH, "//input[@placeholder='* Имя']"
    SURNAME_INPUT = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADDRESS_INPUT = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_STATION_SELECT = By.XPATH, "//div[@class='select-search']/div[@class='select-search__value']"
    STATION_OPTION = By.XPATH, "//*[@class='Order_Text__2broi' and text()='Сокольники']"
    PHONE_INPUT = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    DATA_INPUT = By.XPATH, "//*[@placeholder='* Когда привезти самокат']"
    RENTAL_PERIOD_DROPDOWN = By.XPATH, "//div[contains(@class, 'Dropdown-placeholder')]"
    RENTAL_OPTIONS_VISIBLE = By.XPATH, "// *[@class='Dropdown-option' and text()='сутки']"
    CONFIRM_BUTTON = By.XPATH, "//*[@id='rcc-confirm-button']"
    EMPTY_CLICK = By.XPATH, "//div[@class='App_App__15LM-']"

