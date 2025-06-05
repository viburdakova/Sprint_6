from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTIONS_LOCATOR = By.XPATH, '//*[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]'
    QUESTIONS_LOCATOR_TO_SCROLL = By.XPATH, '//div[@class="accordion__item"]'
    ORDER_BUTTON_DOWN_1 = By.XPATH, "/html/body/div/div/div/div[4]/div[2]/div[5]/button"
    ORDER_BUTTON_DOWN_2 = By.XPATH, "/html/body/div/div/div[2]/div[3]/button[2]"
    ORDER_BUTTON_HEADER = By.XPATH, "/html/body/div/div/div/div[1]/div[2]/button[1]"
    LOGO_SCOOTER = By.XPATH, "/html/body/div/div/div[1]/div[1]/a[2]/img"
    LOGO_YANDEX = By.XPATH, "/html/body/div/div/div/div[1]/div[1]/a[1]/img"
    ORDER_BUTTON_YES = By.XPATH, "/html/body/div/div/div[2]/div[5]/div[2]/button[2]"
    ORDER_SUCCESS = By.XPATH, "/html/body/div/div/div[2]/div[5]/div[1]"
    ORDER_OPEN = By.XPATH, '/html/body/div/div/div[2]/div[5]/div[2]/button'
