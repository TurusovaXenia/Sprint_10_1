import pytest

from data import TariffsData


class TestOrderPanel:
    def test_initial_tariffs_state(self, home_page):
        home_page.route_panel.order_taxi()
        actual_tariffs_state = home_page.order_panel.get_tariffs_state()

        assert actual_tariffs_state == TariffsData.TARIFFS_DEFAULT_STATE, \
            f"Состояние тарифов не соответствует ТЗ! Получено: {actual_tariffs_state}"

    @pytest.mark.xfail(reason="Баг - некорректное описание тарифов 'Сонный' и 'Разговорчивый'")
    @pytest.mark.parametrize("tariff_name, expected_description", TariffsData.TARIFFS_DESCRIPTION.items())
    def test_tariff_shows_correct_description_on_hover(self, home_page, tariff_name, expected_description):
        home_page.route_panel.order_taxi()
        home_page.order_panel.click_tariff_card(tariff_name)
        home_page.order_panel.hover_tariff_icon(tariff_name)

        actual_tariff_description = home_page.order_panel.get_tariff_description(tariff_name)
        assert actual_tariff_description == {tariff_name, expected_description}, \
            f"Неверное описания для тарифа {tariff_name} - получено {actual_tariff_description}"

    def test_required_order_fields_are_visible(self, home_page):
        home_page.route_panel.order_taxi()

        assert home_page.order_panel.are_fields_for_order_visible(), \
            "Кнопки для заказа такси отсутствуют"
