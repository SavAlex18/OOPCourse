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
    """Тест метода add_products"""

    # 1. Проверяем начальное состояние
    # first_category создаётся с 1 продуктом
    assert len(first_category.products) == 1  # Количество товаров в конкретной категории
    assert Category.product_count == 1  # Общее количество товаров во всех категориях

    # 2. Добавляем новый продукт
    first_category.add_product(second_product)

    # 3. Проверяем, что продукт добавился в список конкретной категории
    assert len(first_category.products) == 2
    assert first_category.products[1].name == "LG TV"
    assert first_category.products[1].price == 2

    # 4. Проверяем, что общий счётчик тоже увеличился
    assert Category.product_count == 2


##################
def test_get_products_str(first_category):
    """Проверка форматированной строки товаров."""
    result = first_category.get_products_str
    expected = "Gadget, 5 руб. Остаток: 1 шт.\n"
    assert result == expected


def test_category_products_property(first_category):
    """Проверка, что свойство products возвращает список."""
    products = first_category.products
    assert isinstance(products, list)
    assert len(products) == 1
    assert products[0].name == "Gadget"


def test_get_products_str_empty():
    """Проверка строки для пустой категории."""
    empty_cat = Category("empty", "no products", [])
    assert empty_cat.get_products_str == ""


def test_add_product_edge_cases(first_category):
    """Дополнительные проверки метода add_product."""

    # Проверяем, что добавление None не ломает логику (если нет валидации внутри)
    # Если валидация есть, этот тест упадёт и укажет на необходимость обработки ошибки
    first_category.add_product(None)
    # Здесь нужно смотреть, как поведёт себя код. Если он падает с AttributeError,
    # значит, в add_product нужна проверка if products is not None:

    # Проверка типов
    assert all(isinstance(p, Product) for p in first_category.products)
