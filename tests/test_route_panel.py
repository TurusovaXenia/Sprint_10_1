from data import RoutePanelData


class TestRoutePanel:
    def test_panel_appears_with_different_addresses(self, home_page):
        home_page.route_panel.fill_route()

        assert home_page.route_panel.is_panel_displayed(), \
            "Блок с выбором маршрута не отображается на странице"

    def test_panel_appears_with_identical_addresses(self, home_page):
        home_page.route_panel.fill_identical_addresses()

        assert home_page.route_panel.get_route_info_text() == RoutePanelData.SAME_ADDRESS_INFO

    def test_optimum_tab_active_after_optimum_tab_click(self, home_page):
        home_page.route_panel.fill_route()
        home_page.route_panel.click_optimum_tab()

        assert home_page.route_panel.is_optimum_tab_active(), \
            "Вкладка не активна"

    def test_route_info_changes_on_tab_switch(self, home_page):
        home_page.route_panel.fill_route()

        route_info_quick = home_page.route_panel.get_route_info_text()
        home_page.route_panel.click_optimum_tab()

        assert home_page.route_panel.get_route_info_text() != route_info_quick, \
            "Данные о стоимости и времени маршрута не пересчитались после смены таба"

    def test_your_tab_active_after_your_tab_click(self, home_page):
        home_page.route_panel.fill_route()
        home_page.route_panel.click_your_tab()

        assert home_page.route_panel.is_your_tab_active(), \
            "Вкладка не активна"

    def test_types_of_transportation_become_active_after_your_tab_click(self, home_page):
        home_page.route_panel.fill_route()
        home_page.route_panel.click_your_tab()

        assert home_page.route_panel.are_types_enabled(), \
            "Один или несколько типов маршрута заблокированы (имеют класс disabled)"

    def test_order_taxi_button_active_on_quick_tab(self, home_page):
        home_page.route_panel.fill_route()

        assert home_page.route_panel.is_order_taxi_button_visible(), \
            "Кнопка заказа такси не показывается на странице"

    def test_book_button_active_on_drive_type_tab(self, home_page):
        home_page.route_panel.fill_route()
        home_page.route_panel.click_your_tab()
        home_page.route_panel.click_drive_type()

        assert home_page.route_panel.is_book_button_visible(), \
            "Кнопка бронирования не показывается на странице"
