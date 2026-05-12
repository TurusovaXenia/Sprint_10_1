from data import TariffsData


class TestOrderPanel:
    def test_order_panel_initial_tariffs_state(self, home_page):
        home_page.route_panel.order_taxi()
        actual_tariffs_state = home_page.order_panel.get_tariffs_state()

        assert actual_tariffs_state == TariffsData.TARIFFS_DEFAULT_STATE, \
            f"Состояние тарифов не соответствует ТЗ! Получено: {actual_tariffs_state}"
