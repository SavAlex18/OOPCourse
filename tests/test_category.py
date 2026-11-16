from src.category import Category


def test_category(first_category):
    assert first_category.description == "tv"
    assert first_category.name == "tv"
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_category_two_prod(second_category):
    assert second_category.description == "tv"
    assert second_category.name == "tv"
    assert Category.category_count == 1
    assert Category.product_count == 2
