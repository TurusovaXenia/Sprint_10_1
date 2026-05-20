import allure


@allure.suite("Отрисовка маршрута")
class TestRouteMap:
    @allure.title("Проверка отображения двух точек начала и конца маршрута")
    def test_route_points_visibility_on_map(self, home_page):
        home_page.route_panel.fill_route_with_default_values()

        assert home_page.map.are_two_points_visible(), \
            "Точки начала и конца маршрута не отображаются на странице"
