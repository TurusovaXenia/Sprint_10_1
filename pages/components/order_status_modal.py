import re

import allure

from data import OrderStatusModalData
from locators.components import OrderStatusModalLocators
from pages.base_page import BasePage


class OrderStatusModal(BasePage):
    @allure.step("Проверка элементов окна 'Ожидание машины'")
    def verify_waiting_car_modal_elements_and_text(self):
        self.wait_until_visible(OrderStatusModalLocators.MODAL_TITLE)

        with allure.step("Проверка отображения элементов окна"):
            are_elements_visible = (
                    self.is_element_visible_with_wait(OrderStatusModalLocators.MODAL_TITLE) and
                    self.is_element_visible_with_wait(OrderStatusModalLocators.MODAL_TIMER) and
                    self.is_element_visible_with_wait(OrderStatusModalLocators.DETAILS_BUTTON) and
                    self.is_element_visible_with_wait(OrderStatusModalLocators.CANCEL_BUTTON)
            )

        actual_header_text = self.get_header_text()

        with allure.step("Проверка заголовка окна"):
            is_text_correct = actual_header_text == OrderStatusModalData.WAITING_HEADER_TEXT

        return are_elements_visible and is_text_correct

    @allure.step("Получить значение заголовка окна 'Ожидание машины'")
    def get_header_text(self):
        return self.get_text(OrderStatusModalLocators.MODAL_TITLE)

    @allure.step("Проверка заголовка окна 'Совершенный заказ'")
    def is_arrival_header_correct(self):
        actual_text = self.get_header_text()

        pattern = r"^\d+ мин\. и приедет$"
        return bool(re.match(pattern, actual_text))

    @allure.step("Проверка элементов окна 'Совершенный заказ'")
    def verify_completed_order_modal_elements_and_text(self):
        self.wait_until_invisible(OrderStatusModalLocators.PROGRESS_BAR)

        with allure.step("Проверка отображения информации о водителе"):
            is_driver_info_visible = (
                    self.is_element_visible_with_wait(OrderStatusModalLocators.DRIVER_ICON) and
                    self.is_element_visible_with_wait(OrderStatusModalLocators.DRIVER_NAME) and
                    self.is_element_visible_with_wait(OrderStatusModalLocators.DRIVER_RATING)
            )
        with allure.step("Проверка отображения элементов окна"):
            are_elements_visible = (
                    self.is_element_visible_with_wait(OrderStatusModalLocators.MODAL_TITLE) and
                    self.is_element_visible_with_wait(OrderStatusModalLocators.CAR_NUMBER) and
                    self.is_element_visible_with_wait(OrderStatusModalLocators.CAR_ICON) and
                    self.is_element_visible_with_wait(OrderStatusModalLocators.CANCEL_BUTTON) and
                    self.is_element_visible_with_wait(OrderStatusModalLocators.DETAILS_BUTTON) and
                    is_driver_info_visible
            )

        return are_elements_visible and self.is_arrival_header_correct()

    @allure.step("Клик на кнопку 'Детали'")
    def click_details_button(self):
        self.js_click_element(OrderStatusModalLocators.DETAILS_BUTTON)

    @allure.step("Получение стоимости поездки из деталей заказа")
    def get_ride_price(self):
        price = self.get_text(OrderStatusModalLocators.RIDE_PRICE)
        clean_price = re.sub(r"\D", "", price)
        return clean_price

    @allure.step("Клик на кнопку 'Отмена'")
    def click_cancel_button(self):
        self.js_click_element(OrderStatusModalLocators.CANCEL_BUTTON)
        self.wait_until_invisible(OrderStatusModalLocators.MODAL_CONTAINER)

    @allure.step("Проверка закрытия окна 'Ожидание машины'")
    def is_modal_visible(self):
        return self.is_element_visible_now(OrderStatusModalLocators.MODAL_CONTAINER)
