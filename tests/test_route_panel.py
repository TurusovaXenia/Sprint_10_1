from data import RoutePanelData


class TestRoutePanel:
    def test_panel_appears_with_different_addresses(self, home_page):
        home_page.route_panel.fill_route()

        assert home_page.route_panel.is_panel_displayed(), \
            "Блок с выбором маршрута не отображается на странице"

    def test_panel_appears_with_identical_addresses(self, home_page):
        home_page.route_panel.fill_identical_addresses()

        assert home_page.route_panel.get_route_info_text() == RoutePanelData.SAME_ADDRESS_INFO

    def test_route_info_changes_on_tab_switch(self, home_page):
        home_page.route_panel.fill_route()

        route_info_quick = home_page.route_panel.get_route_info_text()
        home_page.modes_block.click_optimum_tab()

        assert home_page.route_panel.get_route_info_text() != route_info_quick, \
            "Данные о стоимости и времени маршрута не пересчитались после смены таба"