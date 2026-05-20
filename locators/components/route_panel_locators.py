from selenium.webdriver.common.by import By


class RoutePanelLocators:
    FROM_INPUT = (By.CSS_SELECTOR, "input[id='from']")
    TO_INPUT = (By.CSS_SELECTOR, "input[id='to']")

    OPTIMUM_TAB = (By.XPATH, ".//div[text()='Оптимальный']")
    QUICK_TAB = (By.XPATH, ".//div[text()='Быстрый']")
    YOUR_TAB = (By.XPATH, ".//div[text()='Свой']")

    TYPES_LIST = (By.CSS_SELECTOR, "div[class='types-container'] > div[class*='type']")
    TYPE_DRIVE_BUTTON = (By.CSS_SELECTOR, "div[class*='type drive']")

    ORDER_TAXI_BUTTON = (By.XPATH, ".//button[text()='Вызвать такси']")
    BOOK_BUTTON = (By.XPATH, ".//button[text()='Забронировать']")

    RESULT_PANEL = (By.CSS_SELECTOR, "div[class='results-text']")
    TYPE_AND_TIME_LABEL = (By.CSS_SELECTOR, "div[class='results-text'] > div[class='text']")
    PRICE_LABEL = (By.CSS_SELECTOR, "div[class='results-text'] > div[class='duration']")
