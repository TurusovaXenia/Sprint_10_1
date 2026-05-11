from locators.components.map_block_locators import MapBlockLocators
from pages.base_page import BasePage


class MapBlock(BasePage):
    def are_two_points_visible(self):
        self.wait_until_visible(MapBlockLocators.FROM_DOT)

        return (
                self.is_element_visible(MapBlockLocators.FROM_DOT) and
                self.is_element_visible(MapBlockLocators.TO_DOT)
        )
