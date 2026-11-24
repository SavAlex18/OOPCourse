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
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, products: Product):
        if isinstance(products, Product):
            self.__products.append(products)
            Category.product_count += 1

    @property
    def products(self):
        return self.__products

    @property
    def get_products_str(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str
