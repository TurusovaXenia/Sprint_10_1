from selenium.webdriver.common.by import By


class OrderPanelLocators:
    TARIFFS_LIST = (By.CSS_SELECTOR, "div[class*='tariff-cards'] > div[class*='tcard']")
    DESCRIPTIONS_LIST = (By.CSS_SELECTOR, "div[class='i-floating']")
