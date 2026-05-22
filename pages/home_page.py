from pages.base_page import BasePage
from pages.components import MapBlock
from pages.components import OrderPanel
from pages.components import OrderStatusModal
from pages.components import RoutePanel


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.route_panel = RoutePanel(driver)
        self.map = MapBlock(driver)
        self.order_panel = OrderPanel(driver)
        self.order_status_modal = OrderStatusModal(driver)
