from selenium.webdriver.common.by import By


class OrderStatusModalLocators:
    MODAL_CONTAINER = (By.CSS_SELECTOR, "div[class='order-body']")
    MODAL_TITLE = (By.CSS_SELECTOR, "div[class='order-body'] div[class='order-header-title']")
    MODAL_TIMER = (By.CSS_SELECTOR, "div[class='order-body'] div[class='order-header-time']")
    PROGRESS_BAR = (By.CSS_SELECTOR, "div[class='order-progress visible']")

    CAR_NUMBER = (By.CSS_SELECTOR, "div[class='number']")
    CAR_ICON = (By.CSS_SELECTOR, "div[class='order-number'] img")

    DRIVER_ICON = (By.CSS_SELECTOR, "div[class='order-button'] img")
    DRIVER_NAME = (By.XPATH, ".//div[@class='order-button']/following-sibling::div")
    DRIVER_RATING = (By.CSS_SELECTOR, "div[class='order-btn-rating']")

    DETAILS_BUTTON = (By.XPATH, ".//div[text()='Детали']/preceding-sibling::button")
    RIDE_PRICE = (By.XPATH, ".//div[text()='Еще про поездку']/following-sibling::div")
    CANCEL_BUTTON = (By.XPATH, ".//div[text()='Отменить']/preceding-sibling::button")
