from config import config
import pytest
from control.product_controller import ProductController

config = config

class MockProductView:
    def input_product_data(self):
        return "Bolo de Fubá", "Doce", "5.50"

    def show_message(self, message):
        self.last_message = message

    def show_products(self, products):
        self.last_products = products

@pytest.fixture
def controller():
    c = ProductController()
    c.view = MockProductView()  # substitui a view real
    return c

def test_register_product_success(controller):
    controller.register_product()
    assert controller.view.last_message == "Product registered successfully!"
