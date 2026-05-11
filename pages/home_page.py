from pages.base_page import BasePage
from pages.components.map_block import MapBlock
from pages.components.route_panel import RoutePanel
from pages.components.tariffs_block import TariffsBlock



class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.route_panel = RoutePanel(driver)
        self.map = MapBlock(driver)
        self.tariff_block = TariffsBlock(driver)
