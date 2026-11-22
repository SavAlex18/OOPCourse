import pytest

from src.category import Category
from src.product import Product


# Рекомендации 2-х ИИ  # autouse=True заставит сбрасывать счетчики ПЕРЕД КАЖДЫМ тестом
@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.category_count = 0
    Category.product_count = 0
    yield


@pytest.fixture
def first_product():
    return Product("Gadget", "Good Gadget", 5, 1)


@pytest.fixture
def second_product():
    return Product("LG TV", "LG TV 23'", 2, 2)


@pytest.fixture
def first_category():
    prod1 = Product("Gadget", "Good Gadget", 5, 1)
    return Category("tv", "tv", [prod1])


@pytest.fixture
def second_category():
    prod1 = Product("Gadget", "Good Gadget", 5, 1)
    prod2 = Product("LG TV", "LG TV 23'", 2, 2)
    return Category("tv", "tv", [prod1, prod2])
