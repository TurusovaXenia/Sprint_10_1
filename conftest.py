import allure
import pytest
from selenium import webdriver

import urls
from pages.home_page import HomePage


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def home_page(driver):
    page = HomePage(driver)
    with allure.step("Открыть сервис 'Яндекс.Маршруты'"):
        page.go_to_url(urls.HOME_PAGE_URL)

    return page
