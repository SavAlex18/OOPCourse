from src.product import Product


def test_product_init(first_product):
    """Тест инициализации объекта product"""
    assert first_product.name == "Gadget"
    assert first_product.description == "Good Gadget"
    assert first_product.price == 5
    assert first_product.quantity == 1


def test_product_init_and_getter(first_product):
    """Проверка инициализации и работы геттера price."""
    assert first_product.name == "Gadget"
    assert first_product.description == "Good Gadget"
    assert first_product.price == 5  # Читаем через @property
    assert first_product.quantity == 1


def test_product_setter_valid():
    """Проверка установки валидной цены через сеттер."""
    prod = Product("Test", "Desc", 10, 1)
    prod.price = 20
    assert prod.price == 20


def test_product_setter_invalid():
    """Проверка, что сеттер отклоняет нулевую или отрицательную цену."""
    prod = Product("Test", "Desc", 10, 1)

    # Попытка установить 0
    prod.price = 0
    assert prod.price == 10  # Цена не должна измениться

    # Попытка установить отрицательное значение
    prod.price = -5
    assert prod.price == 10  # Цен


def test_new_product_valid():
    """Создание продукта через dict с валидными данными."""
    data = {"name": "Phone", "description": "Smartphone", "price": 500, "quantity": 10}
    prod = Product.new_product(data)

    assert isinstance(prod, Product)
    assert prod.name == "Phone"
    assert prod.price == 500
    assert prod.quantity == 10


def test_new_product_missing_keys():
    """Создание продукта, если в словаре не хватает ключей."""
    data = {"name": "Phone"}  # остальные поля None
    prod = Product.new_product(data)

    assert prod.name == "Phone"
    assert prod.description is None
    assert prod.price is None
    assert prod.quantity is None


def test_product_setter_invalid_message(capsys):
    prod = Product("Test", "Desc", 100, 1)
    prod.price = -10
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
