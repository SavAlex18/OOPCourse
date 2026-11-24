class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = value

    @classmethod
    def new_product(cls, prod_new: dict) -> "Product":
        name = prod_new.get("name", None)
        description = prod_new.get("description", None)
        price = prod_new.get("price", None)
        quantity = prod_new.get("quantity", None)
        return Product(name, description, price, quantity)
