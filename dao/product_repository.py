import json
from dao.json_repository import JsonRepository
from entity.product import Product
from util.fun_util import find


class ProductRepository(JsonRepository):
    products_db = {}
    # products_db_list = list()

    def find_prod_by_name(self, name: str) -> Product or None:  # | None:
        prod_list = self.find_all()
        results = find(lambda prod: prod.name == name, prod_list)
        return results

    def load_goods(self, product: Product, quantity: float):
        if product.name in self.products_db:
            self.products_db[product.name] += quantity
        else:
            self.products_db[product.name] = quantity

    def load_goods_json(self, product: Product, quantity: float):
        for item in self.items.values():
            if product.name == item.name:
                item['quantity'] += quantity

    def print_product_db(self):
        for item, quantity in self.products_db.items():
            print(f"Product: {item} | Quantity: {quantity}")

    def rewrite_db(self):
        with open("products_db.json", "w") as f:
            for item in self.products_db.items():
                f.write(json.dumps(item))
                f.write('\n')

    def exist(self, item):
        if isinstance(item, Product):
            for product in self.items.values():
                if product.name == item.name:
                    return True
        else:
            return item.id in self.items.keys()