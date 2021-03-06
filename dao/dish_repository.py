from dao.repository import Repository
from dao.product_repository import ProductRepository
from entity.dish import Dish
from entity.product import Product


class DishRepository(Repository):
    def get_price(self, dish: Dish):
        current_dish = self.find_by_id(dish.id)
        dish_price = 0
        for item, quantity in current_dish.recipe.items():
            dish_price += quantity * Product.product_price_list[item]
        return dish_price

    def make_dish(self, dish: Dish):
        current_dish = self.find_by_id(dish.id)
        for product, quantity in current_dish.recipe.items():
            ProductRepository.products_db[product] -= quantity

