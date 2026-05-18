import allure

from data import Address
from locators.components.route_panel_locators import RoutePanelLocators
from pages.base_page import BasePage


class RoutePanel(BasePage):
    @allure.step("Заполнить поле 'Откуда'")
    def fill_from_field(self, from_address):
        self.type_text(RoutePanelLocators.FROM_INPUT, from_address)

    @allure.step("Заполнить поле 'Куда'")
    def fill_to_field(self, to_address):
        self.type_text(RoutePanelLocators.TO_INPUT, to_address)

    @allure.step("Заполнить маршрут поездки")
    def fill_route(self):
        self.fill_from_field(Address.FROM_ADDRESS)
        self.fill_to_field(Address.TO_ADDRESS)

    @allure.step("Ввести одинаковые адреса для поездки")
    def fill_identical_addresses(self):
        self.fill_from_field(Address.FROM_ADDRESS)
        self.fill_to_field(Address.FROM_ADDRESS)

    @allure.step("Проверка отрисовки блока с выбором маршрута")
    def is_panel_displayed(self):
        return self.is_element_visible_with_wait(RoutePanelLocators.RESULT_PANEL)

    @allure.step("Получить информацию о поездке")
    def get_route_info_text(self):
        return {
            self.get_text(RoutePanelLocators.TYPE_AND_TIME_LABEL),
            self.get_text(RoutePanelLocators.PRICE_LABEL)
        }

    @allure.step("Клик на вкладку 'Оптимальный'")
    def click_optimum_tab(self):
        self.click_element(RoutePanelLocators.OPTIMUM_TAB)

    @allure.step("Проверка активности вкладки 'Оптимальный'")
    def is_optimum_tab_active(self):
        return self.is_element_active(RoutePanelLocators.OPTIMUM_TAB)

    @allure.step("Клик на вкладку 'Свой'")
    def click_your_tab(self):
        self.click_element(RoutePanelLocators.YOUR_TAB)

    @allure.step("Проверка активности вкладки 'Свой'")
    def is_your_tab_active(self):
        return self.is_element_active(RoutePanelLocators.YOUR_TAB)

    @allure.step("Проверка активности всех типов передвижения'")
    def are_types_enabled(self):
        elements = self.find_elements_with_wait(RoutePanelLocators.TYPES_LIST)
        if not elements:
            return False

        for element in elements:
            classes = element.get_attribute("class")
            if "disabled" in classes.split():
                return False
        return True

    @allure.step("Проверка отображения кнопки 'Вызвать такси'")
    def is_order_taxi_button_visible(self):
        return self.is_element_visible_with_wait(RoutePanelLocators.ORDER_TAXI_BUTTON)

    @allure.step("Клик типа передвижения 'Драйв'")
    def click_drive_type(self):
        self.click_element(RoutePanelLocators.TYPE_DRIVE_BUTTON)

    @allure.step("Проверка отображения кнопки 'Забронировать'")
    def is_book_button_visible(self):
        return self.is_element_visible_now(RoutePanelLocators.BOOK_BUTTON)

    @allure.step("Клик кнопки 'Вызвать такси'")
    def click_order_taxi_button(self):
        self.click_element(RoutePanelLocators.ORDER_TAXI_BUTTON)

    @allure.step("Заполнить маршрут и клик на кнопку 'Заказать такси'")
    def order_taxi(self):
        self.fill_route()
        self.click_order_taxi_button()
