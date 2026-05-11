from pages.base_page import BasePage
from locators.components.tariffs_block_locators import TariffsBlockLocators


class TariffsBlock(BasePage):
    def click_optimum_tab(self):
        self.click_element(TariffsBlockLocators.OPTIMUM_TAB)

    def click_your_tab(self):
        self.click_element(TariffsBlockLocators.YOUR_TAB)

    def is_optimum_tab_active(self):
        classes = self.get_class_attribute(TariffsBlockLocators.OPTIMUM_TAB)
        return "active" in classes.split()

