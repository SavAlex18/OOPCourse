
class Product:
    name: str
    description: str
    price: float
    quantity = 0


    def __init__(self, name: str, description: str, price: float) -> None:
        self.name = name
        self.description = description
        self.price = price
        Product.quantity += 1


if __name__ == "__main__":
    product1 = Product('Cadget', 'Good gadjet', '1')
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)


