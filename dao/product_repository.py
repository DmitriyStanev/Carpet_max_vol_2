from dao.repository import Repository
from entity.product import Product


class ProductRepository(Repository):
    products_db = {}

    def load_goods(self, product: Product, quantity: float):
        if product.name in self.products_db:
            self.products_db[product.name] += quantity
        else:
            self.products_db[product.name] = quantity

    def print_product_db(self):
        for k, v in self.products_db.items():
            return f"Product: {k} | Quantity: {v}"

