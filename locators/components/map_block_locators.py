from selenium.webdriver.common.by import By


class MapBlockLocators:
    FROM_DOT = (By.XPATH, "(.//ymaps[contains(@class, 'route-pin__b')])[1]")
    TO_DOT = (By.XPATH, "(.//ymaps[contains(@class, 'route-pin__b')])[2]")
