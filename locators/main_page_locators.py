from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTIONS_LOCATOR = By.XPATH, "//*[@id='accordion__heading-{}']"
    ANSWER_LOCATOR = By.XPATH, "//*[@id='accordion__panel-{}']"
    QUESTIONS_LOCATOR_TO_SCROLL = By.XPATH, "//div[@class='accordion__item']"
    ORDER_BUTTON_DOWN_1 = By.XPATH, "// *[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    ORDER_BUTTON_HEADER = By.XPATH, "// *[@class='Button_Button__ra12g']"
    LOGO_SCOOTER = By.XPATH, "//*[@alt='Scooter']"
    LOGO_YANDEX = By.XPATH, "//*[@href='//yandex.ru']"
    ORDER_BUTTON_DOWN_2 = By.XPATH, "// *[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    ORDER_BUTTON_YES = By.XPATH, "//*[text()='Да']"
    ORDER_SUCCESS = By.XPATH, "//*[text()='Заказ оформлен']"
    ORDER_OPEN = By.XPATH, "//*[text()='Посмотреть статус']"
