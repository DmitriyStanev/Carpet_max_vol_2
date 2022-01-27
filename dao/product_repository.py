from dao.repository import Repository
from entity.product import Product
import json


class ProductRepository(Repository):
    products_db = {}

    def load_goods(self, product: Product, quantity: float):
        if product.name in self.products_db:
            self.products_db[product.name] += quantity
        else:
            self.products_db[product.name] = quantity

    def print_product_db(self):
        for item, quantity in self.products_db.items():
            return f"Product: {item} | Quantity: {quantity}"

    def rewrite_db(self):
        with open("products_db.txt", "w") as f:
            for item in self.products_db.items():
                f.write(json.dumps(item))
                f.write('\n')

