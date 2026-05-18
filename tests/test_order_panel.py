import allure
import pytest

from conftest import home_page
from data import TariffsData


@allure.suite("Панель выбора тарифов")
class TestOrderPanel:
    @allure.title("Проверка отображения тарифов в панели")
    def test_initial_tariffs_state(self, home_page):
        home_page.route_panel.order_taxi()
        actual_tariffs_state = home_page.order_panel.get_tariffs_state()

        with allure.step("Сравнить полученное состояние тарифов и ожидаемое"):
            assert actual_tariffs_state == TariffsData.TARIFFS_DEFAULT_STATE, \
                f"Состояние тарифов не соответствует ТЗ! Получено: {actual_tariffs_state}"

    @pytest.mark.xfail(reason="Баг - некорректное описание тарифов 'Сонный' и 'Разговорчивый'")
    @pytest.mark.parametrize("tariff_name, expected_description", TariffsData.TARIFFS_DESCRIPTION.items())
    @allure.title("Проверка описаний для каждого тарифа")
    def test_tariff_shows_correct_description_on_hover(self, home_page, tariff_name, expected_description):
        home_page.route_panel.order_taxi()
        home_page.order_panel.click_tariff_card(tariff_name)
        home_page.order_panel.hover_tariff_icon(tariff_name)

        actual_tariff_description = home_page.order_panel.get_tariff_description(tariff_name)
        with allure.step("Сравнить полученное описание для тарифа и ожидаемое"):
            assert actual_tariff_description == {tariff_name, expected_description}, \
                f"Неверное описания для тарифа {tariff_name} - получено {actual_tariff_description}"

    @allure.title("Проверка отображения нужных полей для заказа такси")
    def test_required_order_fields_are_visible(self, home_page):
        home_page.route_panel.order_taxi()

        assert home_page.order_panel.are_fields_for_order_visible(), \
            "Кнопки для заказа такси отсутствуют"
