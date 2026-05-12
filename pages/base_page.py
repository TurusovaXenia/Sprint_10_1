from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def go_to_url(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def type_text(self, locator, text):
        self.wait_until_visible(locator)
        self.driver.find_element(*locator).send_keys(text)

    def get_text(self, locator):
        return self.find_element_with_wait(locator).text

    def get_class_attribute(self, locator):
        self.wait_until_visible(locator)
        return self.driver.find_element(*locator).get_attribute("class")

    def find_element_with_wait(self, locator):
        self.wait_until_visible(locator)
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator):
        self.wait.until(EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def wait_until_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_element_visible(self, locator):
        try:
            self.wait_until_visible(locator)
            return True
        except TimeoutException:
            return False

    def is_element_active(self, locator):
        self.find_element_with_wait(locator)
        return "active" in (self.get_class_attribute(locator) or "").split()
