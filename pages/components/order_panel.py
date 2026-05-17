from data import TariffType
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

    def click_tariff_card(self, tariff_name):
        method, xpath_template = OrderPanelLocators.TARIFF_CARD_BY_NAME
        final_xpath = xpath_template.format(tariff_name=tariff_name)
        self.click_element((method, final_xpath))

    def hover_tariff_icon(self, tariff_name):
        method, xpath_template = OrderPanelLocators.TARIFF_ICON_BY_NAME
        final_xpath = xpath_template.format(tariff_name=tariff_name)
        self.hover_over_element((method, final_xpath))

    def get_tariff_description(self, tariff_name):
        method, xpath_template = OrderPanelLocators.TARIFF_TITLE
        final_xpath_title = xpath_template.format(tariff_name=tariff_name)

        method, xpath_template = OrderPanelLocators.TARIFF_DESCRIPTION
        final_xpath_description = xpath_template.format(tariff_name=tariff_name)

        return {
            self.get_text((method, final_xpath_title)),
            self.get_text((method, final_xpath_description))
        }

    def are_fields_for_order_visible(self):
        self.wait_until_visible(OrderPanelLocators.TARIFFS_LIST)

        return (
                self.is_element_visible(OrderPanelLocators.PHONE_FIELD) and
                self.is_element_visible(OrderPanelLocators.PAYMENT_METHOD_FIELD) and
                self.is_element_visible(OrderPanelLocators.COMMENT_FIELD) and
                self.is_element_visible(OrderPanelLocators.REQUIREMENTS_DROPDOWN) and
                self.is_element_visible(OrderPanelLocators.ENTER_NUMBER_AND_ORDER_TAXI_BUTTON)
        )

    def click_requirements_dropdown(self):
        self.click_element(OrderPanelLocators.REQUIREMENTS_DROPDOWN)

    def activate_laptop_option(self):
        self.click_element(OrderPanelLocators.LAPTOP_SWITCHER)

    def click_call_taxi_button(self):
        self.click_element(OrderPanelLocators.ENTER_NUMBER_AND_ORDER_TAXI_BUTTON)

    def complete_taxi_order(self, tariff_name):
        self.click_tariff_card(tariff_name),
        self.click_requirements_dropdown()
        self.activate_laptop_option()
        self.click_call_taxi_button()
