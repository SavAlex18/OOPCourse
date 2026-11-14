from product import Product

class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products = []
        Category.category_count += 1

    def add_products(self, products: Product):
        self.products.append(products)
        Category.product_count += 1






if __name__ == "__main__":
    cat1 = Category("tv","tv")
    product1 = Product('Cadget', 'Good gadjet', '1')
    cat1.add_products(product1)
    print(cat1.name)
    print(cat1.description)
    print(cat1.products)






