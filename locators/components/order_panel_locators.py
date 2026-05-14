from selenium.webdriver.common.by import By


class OrderPanelLocators:
    TARIFFS_LIST = (By.CSS_SELECTOR, "div[class*='tariff-cards'] > div[class*='tcard']")
    TARIFF_CARD_BY_NAME = (By.XPATH, ".//div[text()='{tariff_name}']/ancestor::div[contains(@class, 'tcard')]")
    TARIFF_ICON_BY_NAME = (By.XPATH, ".//div[text()='{tariff_name}']/preceding-sibling::button")
    TARIFF_TITLE = (By.XPATH, ".//div[contains(@class, 'i-floating')]/div[text()='{tariff_name}']")
    TARIFF_DESCRIPTION = (By.XPATH,
                          ".//div[contains(@class, 'i-floating')]/div[text()='{tariff_name}']/following-sibling::div[contains(@class, 'i-dPrefix')]")

    PHONE_FIELD = (By.XPATH, ".//div[text()='Телефон']")
    PAYMENT_METHOD_FIELD = (By.XPATH, ".//div[contains(@class, 'pp-button filled')]/div[text()='Способ оплаты']")
    COMMENT_FIELD = (By.ID, "comment")
    REQUIREMENTS_FIELD = (By.XPATH, ".//div[text()='Требования к заказу']")
    ORDER_TAXI_BUTTON = (By.CSS_SELECTOR, "button[class='smart-button']")
