from entity.product import Product
from dao.product_repository import ProductRepository

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
        return f"ID: {self.id} | {self.dish_name} | {self.price} | {self.category} |"

    def print_recipe(self):
        print('{} {} : {} $'.format(self.category, self.dish_name, self.price))
        print('Products used: ')
        for product, quantity in self.recipe.items():
            print('{} - {} kg'.format(product, quantity))
            self.products_in_recipe.append(product)

    # def make_dish(self):
    #     for product, quantity in self.recipe.items():
    #         ProductRepository.products_db[product] -= quantity
    #     # ProductRepository.rewrite_db(Product)



