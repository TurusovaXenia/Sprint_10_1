from locators.components.order_panel_locators import OrderPanelLocators
from pages.base_page import BasePage


class OrderPanel(BasePage):
    def get_tariffs_state(self):
        elements = self.find_elements_with_wait(OrderPanelLocators.TARIFFS_LIST)
        states = []
        for element in elements:
            text = element.text.strip().split('\n')[0]
            is_active = "active" in element.get_attribute("class")
            states.append((text, is_active))
        return states
