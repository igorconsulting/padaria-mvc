from config import config
import os
import pytest
from model.product import Product
from repository.product_repository import ProductRepository
config = config

TEST_DB = "data/test_bakery.db"

@pytest.fixture
def repo():
    # Clean test DB
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    return ProductRepository(db_path=TEST_DB)

def test_save_and_retrieve_product(repo):
    product = Product("Bolo", "doce", "9.90")
    repo.save(product)

    products = repo.get_all()
    assert len(products) == 1
    assert products[0].name == "bolo"
    assert products[0].taste == "doce"
    assert products[0].price == 9.90
