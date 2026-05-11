from selenium.webdriver.common.by import By


class RoutePanelLocators:
    FROM_INPUT = (By.CSS_SELECTOR, "input[id='from']")
    TO_INPUT = (By.CSS_SELECTOR, "input[id='to']")

    RESULT_PANEL = (By.CSS_SELECTOR, "div[class='results-text']")
    TYPE_AND_TIME_LABEL = (By.CSS_SELECTOR, "div[class='results-text'] > div[class='text']")
    PRICE_LABEL = (By.CSS_SELECTOR, "div[class='results-text'] > div[class='duration']")
