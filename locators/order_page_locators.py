from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = By.XPATH, "//input[@placeholder='* Имя']"
    SURNAME_INPUT = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADDRESS_INPUT = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_STATION_SELECT = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/div/div/input")
    STATION_OPTION = (By.XPATH, "//div[@class='select-search__select']")
    PHONE_INPUT = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    DATA_INPUT = By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div/div/input"
    DATA = By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]"
    RENTAL_PERIOD_DROPDOWN = By.XPATH, "//div[contains(@class, 'Dropdown-placeholder')]"
    RENTAL_OPTIONS_VISIBLE = By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[1]"
    CONFIRM_BUTTON = By.XPATH, "//*[@id='rcc-confirm-button']"
    EMPTY_CLICK = By.XPATH, "//div[@class='App_App__15LM-']"

