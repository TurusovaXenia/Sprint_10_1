class TestRouteMap:
    def test_route_points_visibility_on_map(self, home_page):
        home_page.route_panel.fill_route()

        assert home_page.map.are_two_points_visible(), \
            "Точки начала и конца маршрута не отображаются на странице"
