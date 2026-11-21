def test_product_init(first_product):
    """ Тест инициализации объекта product"""
    assert first_product.name == "Gadget"
    assert first_product.description == "Good Gadget"
    assert first_product.price == 5
    assert first_product.quantity == 1
