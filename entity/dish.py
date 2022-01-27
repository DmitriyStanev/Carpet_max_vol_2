from entity.product import Product

class Dish:
    next_id = 0

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id

    all_dishes = set()

    def __init__(self, dish_name, price, category, recipe):
        self.id = self.get_next_id()
        self.dish_name = dish_name
        self.price = price
        self.category = category
        self.recipe = recipe
        self.all_dishes.add(self)
        self.products_in_recipe = []

    def __str__(self):
        return f"ID: {self.id} | {self.dish_name:} | {self.price:} | {self.category:} |"

    def fullname(self):
        return '{} {} - price {} $ '.format(self.dish_name, self.price)

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