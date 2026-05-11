from selenium.webdriver.common.by import By

class ModesBlockLocators:
    OPTIMUM_TAB = (By.XPATH, ".//div[text()='Оптимальный']")
    YOUR_TAB = (By.XPATH, ".//div[text()='Свой']")