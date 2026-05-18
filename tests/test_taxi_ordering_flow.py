from data import TariffType


class TestTaxiOrderingFlow:
    def test_successful_order_workable_tariff_with_laptop_waiting_car_modal_matches_spec(self, home_page):
        home_page.route_panel.order_taxi()
        home_page.order_panel.click_tariff_card(TariffType.WORKABLE)
        home_page.order_panel.click_requirements_dropdown()
        home_page.order_panel.activate_laptop_option()
        home_page.order_panel.click_confirm_order_button()

        assert home_page.order_status_modal.verify_waiting_car_modal_elements_and_text(), \
            "Окно ожидания машины не соответствует требованиям ТЗ (ошибка в элементах или тексте заголовка)"

    def test_successful_order_workable_tariff_with_laptop_completed_modal_matches_spec(self, home_page):
        home_page.route_panel.order_taxi()
        home_page.order_panel.click_tariff_card(TariffType.WORKABLE)
        home_page.order_panel.click_requirements_dropdown()
        home_page.order_panel.activate_laptop_option()
        home_page.order_panel.click_confirm_order_button()

        assert home_page.order_status_modal.verify_completed_order_modal_elements_and_text(), \
            "Окно совершенного заказа не соответствует требованиям ТЗ (ошибка в элементах или тексте заголовка)"

    def test_tariff_price_matches_order_details(self, home_page):
        home_page.route_panel.order_taxi()
        home_page.order_panel.click_tariff_card(TariffType.WORKABLE)
        tariff_price = home_page.order_panel.get_tariff_price(TariffType.WORKABLE)

        home_page.order_panel.click_requirements_dropdown()
        home_page.order_panel.activate_laptop_option()
        home_page.order_panel.click_confirm_order_button()

        home_page.order_status_modal.click_details_button()

        assert home_page.order_status_modal.get_ride_price() == tariff_price

    def test_click_cancel_button_closes_modal(self, home_page):
        home_page.route_panel.order_taxi()
        home_page.order_panel.click_tariff_card(TariffType.WORKABLE)

        home_page.order_panel.click_requirements_dropdown()
        home_page.order_panel.activate_laptop_option()
        home_page.order_panel.click_confirm_order_button()

        home_page.order_status_modal.click_cancel_button()

        assert home_page.order_status_modal.is_modal_visible() == False, \
            "Окно не закрылось"
