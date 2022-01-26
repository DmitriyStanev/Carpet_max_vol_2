from entity.product import Product

class Dish:

    all_dishes = []

    def __init__(self, dish_name, price, category, recipe):
        self.dish_name = dish_name
        self.price = price
        self.category = category
        self.recipe = recipe
        self.all_dishes.append(self)
        self.products_in_recipe = []

    def __str__(self):
        return f"| {self.dish_name:<20.20s} | {self.price:<6.2f} | {self.category:<10.10s} |"

    def fullname(self):
        return '{} {} - price {} $ '.format(self.dish_name, self.price)

    def get_recipe(self):
        return self.recipe

    def print_recipe(self):
        print('{} {} : {} $'.format(self.category, self.dish_name, self.price))
        print('Products used: ')
        for product, quantity in self.recipe.items():
            print('{} - {} kg'.format(product, quantity))
            self.products_in_recipe.append(product)

    def fullname(self):
        return '{} {} - price {} $ '.format(self.category, self.dish_name, self.price)

    def make_dish(self):
        for product, quantity in self.recipe.items():
            Product.products_db[product] -= quantity
        Product.format_db(Product)
        Product.rewrite_db(Product)

    def count_dish_price(self):
        dish_price = 0
        for item, quantity in self.recipe.items():
            dish_price += quantity * Product.product_price_list[item]
        return dish_price


# if __name__ == '__main__':
#
#     burrata = Dish('Burrata', 17.99, 'SALAD', {'Tomatoes': 0.400, 'Basil': 0.020, 'Burrata': 0.200, 'Pesto': 0.030})
#     mixta = Dish('Mixta', 12.99, 'SALAD', {'Avocado': 0.200, 'Mix fresh salads': 0.100, 'Pine nuts': 0.050,
#                                            'Citrus dressing': 0.050})
#
#     # print(mixta.fullname())
#     # mixta.get_recipe()
#
#     def print_product_list(list):
#         for item in list:
#             print('{}: {} {}.'.format(item.name, Product.products_db[item.name], item.measure_unit))
#
#
#
#     print_product_list(Product.product_list)