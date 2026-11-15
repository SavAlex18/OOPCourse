from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(products)

    def add_products(self, products: Product):
        self.products.append(products)
        # Category.product_count += 1


if __name__ == "__main__":
    cat1 = Category("tv", "tv", [])
    product1 = Product("Gadget", "Good Gadget", 5, 1)
    cat1.add_products(product1)
    print(cat1.name)
    print(cat1.description)
    print(cat1.products)
