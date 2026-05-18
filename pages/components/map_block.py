import allure

from locators.components.map_block_locators import MapBlockLocators
from pages.base_page import BasePage


class MapBlock(BasePage):
    @allure.step("Проверка отображения двух точек начала и конца маршрута")
    def are_two_points_visible(self):
        self.wait_until_visible(MapBlockLocators.FROM_DOT)

        return (
                self.is_element_visible_now(MapBlockLocators.FROM_DOT) and
                self.is_element_visible_now(MapBlockLocators.TO_DOT)
        )
