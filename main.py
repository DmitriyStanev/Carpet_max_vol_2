from entity.dish import Dish
from entity.product import Product
from user_items.users import User


if __name__ == '__main__':

    """Creating products for the menu"""

    """Products for main dishes"""
    pluma = Product('Pluma Joselito', 32.00, 'kg')
    presa = Product('Presa Joselito', 24.00, 'kg')
    kobe = Product('Kobe Beef Wagyu', 1256.00, 'kg')

    """Products for salads"""
    tomatoes = Product('Tomatoes', 3, 'kg')
    basil = Product('Basil', 10, 'kg')
    burrata = Product('Burrata', 30, 'kg')
    pesto = Product('Pesto', 20, 'kg')
    avocado = Product('Avocado', 10.00, 'kg')
    fresh_salads = Product('Mix fresh salads', 3, 'kg')
    pine_nuts = Product('Pine nuts', 26, 'kg')
    citrus_dressing = Product('Citrus dressing', 15.00, 'lt')
    garlic = Product('Garlic', 20.00, 'kg')
    olive_oil = Product('Olive oil', 30.00, 'lt')

    """Loading products to warehouse"""
    tomatoes.load_goods(10)
    burrata.load_goods(10)
    pesto.load_goods(10)
    basil.load_goods(10)
    avocado.load_goods(10)
    fresh_salads.load_goods(10)
    pine_nuts.load_goods(10)
    citrus_dressing.load_goods(10)
    garlic.load_goods(10)
    olive_oil.load_goods(10)

    """Creating Salads"""
    burrata = Dish('Burrata', 17.99, 'SALAD', {'Tomatoes': 0.400, 'Basil': 0.020, 'Burrata': 0.100, 'Pesto': 0.030})
    mixta = Dish('Mixta', 12.99, 'SALAD', {'Avocado': 0.200, 'Mix fresh salads': 0.100, 'Pine nuts': 0.050, 'Citrus dressing': 0.050})
    guacamole = Dish('Guacamole', 17.99, 'SALAD', {'Tomatoes': 0.050, 'Avocado': 0.200, 'Garlic': 0.010, 'Olive oil': 0.050})

    """Creating users"""

    vasya = User('Vasiliy', 'Rogov', 43, '1111')
    print(vasya)

    # for item, quantity in Product.products_db.items():
    #     print(item, '--->', quantity)
    #
    #
    # print('==================================================================================')
    #
    for item in Product.products_db:
        print(item)
    #
    # print('==================================================================================')
    #
    # for item, quantity in Product.products_db.items():
    #     print(item, '--->', quantity)


    print(Product.products_db)
    burrata.make_dish()
    burrata.make_dish()
    burrata.make_dish()
    burrata.make_dish()
    burrata.make_dish()
    print(Product.products_db)
    print('==================================================================================')
    Product.format_db(Product)
    print(Product.products_db)
    print('==================================================================================')
    guacamole.make_dish()
    mixta.make_dish()
    guacamole.make_dish()
    mixta.make_dish()
    guacamole.make_dish()
    mixta.make_dish()
    print(Product.products_db)
    Product.print_product_db(Product)
    Product.rewrite_db(Product)

    for dish in Dish.all_dishes:
        print(dish)