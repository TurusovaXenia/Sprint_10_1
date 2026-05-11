from selenium.common import TimeoutException

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
        try:
            self.wait_until_visible(RoutePanelLocators.RESULT_PANEL)
            return True
        except TimeoutException:
            return False

    def get_route_info_text(self):
        return (
            self.get_text(RoutePanelLocators.TYPE_AND_TIME_LABEL),
            self.get_text(RoutePanelLocators.PRICE_LABEL)
        )

    def get_route_info_on_tab_switch(self):
        self.wait_until_visible(RoutePanelLocators.RESULT_PANEL)

        route_info_quick = self.get_route_info_text()
        self.click_optimum_tab()
        route_info_optimum = self.get_route_info_text()
        return route_info_quick != route_info_optimum
