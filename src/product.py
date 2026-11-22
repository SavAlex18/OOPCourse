class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
