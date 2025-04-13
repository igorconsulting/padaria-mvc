from config import config
import pytest
from model.product import Product

config = config
def test_product_initialization():
    p = Product("  pão francês  ", "  Sal  ", "  2.99  ")
    assert p.name == "pao frances"
    assert p.taste == "sal"
    assert p.price == 2.99

def test_product_invalid_price_raises_error():
    with pytest.raises(ValueError):
        Product("Café", "amargo", "abc")
