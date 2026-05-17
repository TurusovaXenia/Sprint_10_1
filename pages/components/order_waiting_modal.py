from pages.base_page import BasePage
from locators.components.order_waiting_modal_locators import OrderWaitingModalLocators

class OrderWaitingModal(BasePage):
    def are_all_elements_on_modal_visible(self):
        self.wait_until_visible(OrderWaitingModalLocators.MODAL_TITLE)

        return (
                self.is_element_visible(OrderWaitingModalLocators.MODAL_TITLE) and
                self.is_element_visible(OrderWaitingModalLocators.MODAL_TIMER) and
                self.is_element_visible(OrderWaitingModalLocators.DETAILS_BUTTON) and
                self.is_element_visible(OrderWaitingModalLocators.CANCEL_BUTTON)
        )