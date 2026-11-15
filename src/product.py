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


if __name__ == "__main__":
    product1 = Product("Gadget", "Good Gadget", 5, 1)
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)
