from data import Address
from locators.components.route_panel_locators import RoutePanelLocators
from pages.base_page import BasePage


class RoutePanel(BasePage):
    def fill_from_field(self, from_address):
        self.type_text(RoutePanelLocators.FROM_INPUT, from_address)

    def fill_to_field(self, to_address):
        self.type_text(RoutePanelLocators.TO_INPUT, to_address)

    def fill_route(self):
        self.fill_from_field(Address.FROM_ADDRESS)
        self.fill_to_field(Address.TO_ADDRESS)

    def fill_identical_addresses(self):
        self.fill_from_field(Address.FROM_ADDRESS)
        self.fill_to_field(Address.FROM_ADDRESS)

    def is_panel_displayed(self):
        return self.is_element_visible(RoutePanelLocators.ORDER_TAXI_BUTTON)

    def get_route_info_text(self):
        return {
            self.get_text(RoutePanelLocators.TYPE_AND_TIME_LABEL),
            self.get_text(RoutePanelLocators.PRICE_LABEL)
        }

    def click_optimum_tab(self):
        self.click_element(RoutePanelLocators.OPTIMUM_TAB)

    def is_optimum_tab_active(self):
        return self.is_element_active(RoutePanelLocators.OPTIMUM_TAB)

    def click_your_tab(self):
        self.click_element(RoutePanelLocators.YOUR_TAB)

    def is_your_tab_active(self):
        return self.is_element_active(RoutePanelLocators.YOUR_TAB)

    def are_types_enabled(self):
        elements = self.find_elements_with_wait(RoutePanelLocators.TYPES_LIST)
        if not elements:
            return False

        for element in elements:
            classes = element.get_attribute("class")
            if "disabled" in classes.split():
                return False
        return True

    def is_order_taxi_button_visible(self):
        return self.is_element_visible(RoutePanelLocators.ORDER_TAXI_BUTTON)

    def click_drive_type(self):
        self.click_element(RoutePanelLocators.TYPE_DRIVE_BUTTON)

    def is_book_button_visible(self):
        return self.is_element_visible(RoutePanelLocators.BOOK_BUTTON)

    def click_order_taxi_button(self):
        self.click_element(RoutePanelLocators.ORDER_TAXI_BUTTON)

    def order_taxi(self):
        self.fill_route()
        self.click_order_taxi_button()
