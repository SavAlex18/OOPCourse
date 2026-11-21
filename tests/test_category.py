from src.category import Category


def test_category(first_category):
    """Тест инициализации категорий"""
    assert first_category.description == "tv"
    assert first_category.name == "tv"
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_category_two_prod(second_category):
    assert second_category.description == "tv"
    assert second_category.name == "tv"
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_add_product(first_category, second_product):
    """Тест метода add_products"""

    # 1. Проверяем начальное состояние
    # first_category создаётся с 1 продуктом
    assert len(first_category.products) == 1  # Количество товаров в конкретной категории
    assert Category.product_count == 1  # Общее количество товаров во всех категориях

    # 2. Добавляем новый продукт
    first_category.add_products(second_product)

    # 3. Проверяем, что продукт добавился в список конкретной категории
    assert len(first_category.products) == 2
    assert first_category.products[1].name == "LG TV"
    assert first_category.products[1].price == 2

    # 4. Проверяем, что общий счётчик тоже увеличился
    assert Category.product_count == 2
