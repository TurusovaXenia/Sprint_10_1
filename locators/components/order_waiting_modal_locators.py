from selenium.webdriver.common.by import By


class OrderWaitingModalLocators:
    MODAL_TITLE = (By.CSS_SELECTOR, "div[class='order-body'] div[class='order-header-title']")
    MODAL_TIMER = (By.CSS_SELECTOR, "div[class='order-body'] div[class='order-header-time']")
    DETAILS_BUTTON = (By.XPATH, ".//div[text()='Детали']/preceding-sibling::button")
    CANCEL_BUTTON = (By.XPATH, ".//div[text()='Отменить']/preceding-sibling::button")
