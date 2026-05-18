from pages.base_page import BasePage
from pages.components.map_block import MapBlock
from pages.components.order_panel import OrderPanel
from pages.components.order_status_modal import OrderStatusModal
from pages.components.route_panel import RoutePanel


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.route_panel = RoutePanel(driver)
        self.map = MapBlock(driver)
        self.order_panel = OrderPanel(driver)
        self.order_status_modal = OrderStatusModal(driver)
