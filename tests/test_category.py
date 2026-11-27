from src.category import Category
from src.product import Product


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
    """Тест метода add_product"""
    # 1. Проверяем начальное состояние
    assert first_category.products == "Gadget, 5 руб. Остаток: 1 шт.\n"
    assert Category.product_count == 1

    # 2. Добавляем новый продукт
    first_category.add_product(second_product)

    # 3. Проверяем, что продукт добавился в строку
    expected = "Gadget, 5 руб. Остаток: 1 шт.\nLG TV, 2 руб. Остаток: 2 шт.\n"
    assert first_category.products == expected

    # 4. Проверяем, что общий счётчик тоже увеличился
    assert Category.product_count == 2


def test_get_products_str(first_category):
    """Проверка форматированной строки товаров."""
    result = first_category.products
    expected = "Gadget, 5 руб. Остаток: 1 шт.\n"
    assert result == expected


def test_category_products_property(first_category):
    """Проверка, что свойство products возвращает строку, а не список."""
    products = first_category.products
    assert isinstance(products, str)
    assert products == "Gadget, 5 руб. Остаток: 1 шт.\n"


def test_get_products_str_empty():
    """Проверка строки для пустой категории."""
    empty_cat = Category("empty", "no products", [])
    assert empty_cat.products == ""


def test_add_product_edge_cases(first_category):
    """Дополнительные проверки метода add_product."""
    # Проверяем, что добавление None не ломает логику
    first_category.add_product(None)
    # Строка не должна измениться
    assert first_category.products == "Gadget, 5 руб. Остаток: 1 шт.\n"

    # Проверка типов — все элементы в строке соответствуют шаблону
    lines = first_category.products.strip().split('\n')
    for line in lines:
        assert ', ' in line and ' руб. Остаток: ' in line and ' шт.' in line