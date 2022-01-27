from entity.product import Product
from dao.product_repository import ProductRepository






if __name__ == "__main__":
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

    products_repo = ProductRepository()
    for item in Product.product_list:
        products_repo.create(item)

    for item in products_repo.find_all():
        products_repo.load_goods(item, 10)

    for item, quantity in products_repo.products_db.items():
        print(f"Product: {item} | Quantity: {quantity}")

