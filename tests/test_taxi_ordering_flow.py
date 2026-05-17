from data import TariffType


class TestTaxiOrderingFlow:
    def test_successful_taxi_order_workable_tariff(self, home_page):
        home_page.route_panel.order_taxi()
        home_page.order_panel.click_tariff_card(TariffType.WORKABLE)
        home_page.order_panel.click_requirements_dropdown()
        home_page.order_panel.activate_laptop_option()
        home_page.order_panel.click_call_taxi_button()

        assert home_page.order_waiting_modal.are_all_elements_on_modal_visible(), \
            "Не все элементы по ТЗ отображаются в модальном окне"
