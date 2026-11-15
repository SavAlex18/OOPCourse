import pytest

from src.product import Product
from src.category import Category

@pytest.fixture
def first_product():
    return Product("Gadget", "Good Gadget", 5, 1)

@pytest.fixture
def second_product():
    return Product("LG TV", "LG TV 23'", 2, 2)

# @pytest.fixture
# def first_category():

