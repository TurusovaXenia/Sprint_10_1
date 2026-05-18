import re

import allure

from locators.components.order_panel_locators import OrderPanelLocators
from pages.base_page import BasePage


class OrderPanel(BasePage):
    @allure.step("Получить тариф и его статус")
    def get_tariffs_state(self):
        elements = self.find_elements_with_wait(OrderPanelLocators.TARIFFS_LIST)
        states = []
        for element in elements:
            text = element.text.strip().split('\n')[0]
            is_active = "active" in element.get_attribute("class")
            states.append((text, is_active))
        return states

    @allure.step("Выбрать тарифный план: '{tariff_name}'")
    def click_tariff_card(self, tariff_name):
        method, xpath_template = OrderPanelLocators.TARIFF_CARD_BY_NAME
        final_xpath = xpath_template.format(tariff_name=tariff_name)
        self.click_element((method, final_xpath))

    @allure.step("Навести мышку на иконку тарифа '{tariff_name}'")
    def hover_tariff_icon(self, tariff_name):
        method, xpath_template = OrderPanelLocators.TARIFF_ICON_BY_NAME
        final_xpath = xpath_template.format(tariff_name=tariff_name)
        self.hover_over_element((method, final_xpath))

    @allure.step("Получить описание тарифа '{tariff_name}'")
    def get_tariff_description(self, tariff_name):
        method, xpath_template = OrderPanelLocators.TARIFF_TITLE
        final_xpath_title = xpath_template.format(tariff_name=tariff_name)

        method, xpath_template = OrderPanelLocators.TARIFF_DESCRIPTION
        final_xpath_description = xpath_template.format(tariff_name=tariff_name)

        return {
            self.get_text((method, final_xpath_title)),
            self.get_text((method, final_xpath_description))
        }

    @allure.step("Получить цену тарифа '{tariff_name}'")
    def get_tariff_price(self, tariff_name):
        method, xpath_template = OrderPanelLocators.TARIFF_PRICE
        final_xpath = xpath_template.format(tariff_name=tariff_name)
        price = self.get_text((method, final_xpath))

        clean_price = re.sub(r"\D", "", price)
        return clean_price

    @allure.step("Проверка отображения элементов для заказа такси")
    def are_fields_for_order_visible(self):
        self.wait_until_visible(OrderPanelLocators.TARIFFS_LIST)

        return (
                self.is_element_visible_now(OrderPanelLocators.PHONE_FIELD) and
                self.is_element_visible_now(OrderPanelLocators.PAYMENT_METHOD_FIELD) and
                self.is_element_visible_now(OrderPanelLocators.COMMENT_FIELD) and
                self.is_element_visible_now(OrderPanelLocators.REQUIREMENTS_DROPDOWN) and
                self.is_element_visible_now(OrderPanelLocators.ENTER_NUMBER_AND_ORDER_TAXI_BUTTON)
        )

    @allure.step("Клик на выпадающий список 'Требования к заказу'")
    def click_requirements_dropdown(self):
        self.click_element(OrderPanelLocators.REQUIREMENTS_DROPDOWN)

    @allure.step("Добавить опцию 'Столик для ноутбука'")
    def activate_laptop_option(self):
        self.click_element(OrderPanelLocators.LAPTOP_SWITCHER)

    @allure.step("Клик по кнопке 'Ввести номер и заказать'")
    def click_confirm_order_button(self):
        self.click_element(OrderPanelLocators.ENTER_NUMBER_AND_ORDER_TAXI_BUTTON)
