class TestTariffsBlock:
    def test_optimum_tab_active_after_optimum_button(self, home_page):
        home_page.route_panel.fill_route()
        home_page.tariff_block.click_optimum_tab()

        assert home_page.tariff_block.is_optimum_tab_active(), \
            "Вкладка не активна"
