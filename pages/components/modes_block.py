from pages.base_page import BasePage
from locators.components.modes_block_locators import ModesBlockLocators


class ModesBlock(BasePage):
    def click_optimum_tab(self):
        self.click_element(ModesBlockLocators.OPTIMUM_TAB)

    def click_your_tab(self):
        self.click_element(ModesBlockLocators.YOUR_TAB)

    def is_optimum_tab_active(self):
        classes = self.get_class_attribute(ModesBlockLocators.OPTIMUM_TAB)
        return "active" in classes.split()

