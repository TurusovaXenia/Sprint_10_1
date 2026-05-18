import re

from data import OrderStatusModalData
from locators.components.order_status_modal_locators import OrderStatusModalLocators
from pages.base_page import BasePage


class OrderStatusModal(BasePage):
    def verify_waiting_car_modal_elements_and_text(self):
        self.wait_until_visible(OrderStatusModalLocators.MODAL_TITLE)

        is_visible = (
                self.is_element_visible_with_wait(OrderStatusModalLocators.MODAL_TITLE) and
                self.is_element_visible_with_wait(OrderStatusModalLocators.MODAL_TIMER) and
                self.is_element_visible_with_wait(OrderStatusModalLocators.DETAILS_BUTTON) and
                self.is_element_visible_with_wait(OrderStatusModalLocators.CANCEL_BUTTON)
        )

        actual_header_text = self.get_header_text()
        is_text_correct = actual_header_text == OrderStatusModalData.WAITING_HEADER_TEXT
        return is_visible and is_text_correct

    def get_header_text(self):
        return self.get_text(OrderStatusModalLocators.MODAL_TITLE)

    def is_arrival_header_correct(self):
        actual_text = self.get_header_text()

        pattern = r"^\d+ мин\. и приедет$"
        return bool(re.match(pattern, actual_text))

    def verify_completed_order_modal_elements_and_text(self):
        self.wait_until_invisible(OrderStatusModalLocators.PROGRESS_BAR)

        is_driver_info_visible = (
                self.is_element_visible_with_wait(OrderStatusModalLocators.DRIVER_ICON) and
                self.is_element_visible_with_wait(OrderStatusModalLocators.DRIVER_NAME) and
                self.is_element_visible_with_wait(OrderStatusModalLocators.DRIVER_RATING)
        )

        are_elements_visible = (
                self.is_element_visible_with_wait(OrderStatusModalLocators.MODAL_TITLE) and
                self.is_element_visible_with_wait(OrderStatusModalLocators.CAR_NUMBER) and
                self.is_element_visible_with_wait(OrderStatusModalLocators.CAR_ICON) and
                self.is_element_visible_with_wait(OrderStatusModalLocators.CANCEL_BUTTON) and
                self.is_element_visible_with_wait(OrderStatusModalLocators.DETAILS_BUTTON) and
                is_driver_info_visible
        )

        return are_elements_visible and self.is_arrival_header_correct()

    def click_details_button(self):
        self.js_click_element(OrderStatusModalLocators.DETAILS_BUTTON)

    def get_ride_price(self):
        price = self.get_text(OrderStatusModalLocators.RIDE_PRICE)
        clean_price = re.sub(r"\D", "", price)
        return clean_price

    def click_cancel_button(self):
        self.js_click_element(OrderStatusModalLocators.CANCEL_BUTTON)
        self.wait_until_invisible(OrderStatusModalLocators.MODAL_CONTAINER)

    def is_modal_visible(self):
        return self.is_element_visible_now(OrderStatusModalLocators.MODAL_CONTAINER)
