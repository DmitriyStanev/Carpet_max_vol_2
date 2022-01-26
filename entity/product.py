import json

class Product:

    product_list = set()
    products = [x for x in product_list]
    products_db = {}
    product_price_list = {}
    formatted_products_db = {}

    def __init__(self, name, delivery_price, measure_unit):
        self.name = name
        self.delivery_price = delivery_price
        self.measure_unit = measure_unit
        self.product_list.add(self)
        if self.name not in self.product_price_list:
            self.product_price_list[name] = delivery_price

    def __str__(self):
        return f"| {self.name:<20.20s} | {self.delivery_price:<6.2f} | {self.measure_unit:<2.2s} |"

    def print_product_db(self):
        for k, v in self.products_db.items():
            print(f"| {k:<20.20s} | {v:<6.2f} |")

    def get_product_list(self):
        return self.product_list

    def load_goods(self, quantity):
        if self.name in self.products_db:
            self.products_db[self.name] += quantity
        else:
            self.products_db[self.name] = quantity

    def format_db(self):
        for k, v in self.products_db.items():
            self.products_db[k] = float(format(v, '.3f'))

    def rewrite_db(self):
        with open("products_db.txt", "w") as f:
            for item in Product.products_db.items():
                f.write(json.dumps(item))
                f.write('\n')




# # """Products for main dishes"""
# pluma = Product('Pluma Joselito', 32.00, 'kg')
# print(pluma)
# presa = Product('Presa Joselito', 24.00, 'kg')
# kobe = Product('Kobe Beef Wagyu', 1256.00, 'kg')
#
# """Products for salads"""
# tomatoes = Product('Tomatoes', 3, 'kg')
# basil = Product('Basil', 10, 'kg')
# burrata = Product('Burrata', 30, 'kg')
# pesto = Product('Pesto', 20, 'kg')
# avocado = Product('Avocado', 10.00, 'kg')
# fresh_salats = Product('Mix fresh salads', 3, 'kg')
# pine_nuts = Product('Pine nuts', 26, 'kg')
# citrus_dressing = Product('Citrus dressing', 15.00, 'lt')
# mix_fresh_salads = Product('Mix fresh salads', 3, 'kg')
#
# tomatoes.load_goods(4)
# burrata.load_goods(6)
# pesto.load_goods(2)
# basil.load_goods(10)
# avocado.load_goods(10)
# mix_fresh_salads.load_goods(10)
# pine_nuts.load_goods(2)
# citrus_dressing.load_goods(5)
# print(Product.products_db)

# burrata.load_goods(6)
# pine_nuts.load_goods(1)
# print((Product.products_db))

# tomatoes.load_goods(4)
# burrata.load_goods(6)
# pesto.load_goods(2)
# basil.load_goods(10)
# avocado.load_goods(10)
# mix_fresh_salads.load_goods(10)
# pine_nuts.load_goods(2)
# citrus_dressing.load_goods(5)
# Product.rewrite_db(Product)


if __name__ == '__main__':
    pass

    # def print_product_list(list):
    #     for item in list:
    #         print('{}: {} {}.'.format(item.name, Product.products_db[item.name], item.measure_unit))


