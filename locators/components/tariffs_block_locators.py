from selenium.webdriver.common.by import By

class TariffsBlockLocators:
    OPTIMUM_TAB = (By.XPATH, ".//div[text()='Оптимальный']")
    YOUR_TAB = (By.XPATH, ".//div[text()='Свой']")