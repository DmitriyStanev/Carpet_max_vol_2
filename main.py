from entity.product import Product
from entity.dish import Dish
from dao.product_repository import ProductRepository
from dao.dish_repository import DishRepository
from dao.user_repository import UserRepository
from controller.login_controller import LoginController
from entity.user import User
from view.main_menu_commands import RegisterCommand, LoginCommand, LogoutCommand, GetLoggedUserCommand
from view.menu import MenuItem, Menu


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


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

    # products_repo = ProductRepository()
    # for item in Product.product_list:
    #     products_repo.create(item)
    #
    # for item in products_repo.find_all():
    #     products_repo.load_goods(item, 10)
    # products_repo.rewrite_db()
    #
    # """Creating Salads"""
    # burrata = Dish('Burrata', 17.99, 'SALAD', {'Tomatoes': 0.500, 'Basil': 0.020, 'Burrata': 0.100, 'Pesto': 0.030})
    # mixta = Dish('Mixta', 12.99, 'SALAD', {'Avocado': 0.200, 'Mix fresh salads': 0.100, 'Pine nuts': 0.050,
    #                                        'Citrus dressing': 0.050})
    # guacamole = Dish('Guacamole', 17.99, 'SALAD', {'Tomatoes': 0.050, 'Avocado': 0.200, 'Garlic': 0.010,
    #                                                'Olive oil': 0.050})
    #
    # dishes = (burrata, mixta, guacamole)
    #
    # dish_repo = DishRepository()
    # for dish in dishes:
    #     dish_repo.create(dish)
    #
    # dish_repo.make_dish(burrata)
    # products_repo.print_product_db()

    """Creating users"""
    vasya = User('Vasiliy', 'Rogov', 34, '0980000000', '4444', 'WAITER')
    andruha = User('Andrey', 'Larin', 46, '0984444444', '131313', 'MANAGER')
    for user in enumerate(User.all_users()):
        print(user)



    """Adding created users to UserRepository"""
    users = (vasya, andruha)
    users_repo = UserRepository("Users.json", User)

    # for prod in Product.product_list:
    #     print(prod)

    product_repo = ProductRepository("Products.json", Product)
    # product_repo.load()
    # product_repo.load_from_list(Product.product_list)
    # product_repo.save()
    pesto = Product('Pesto', 7777, 'kg')
    product_repo.load()
    product_repo.create(pesto)
    product_repo.save()
    # product_repo.load_goods_json(pesto, 111.0)
    print("Item exists: ", product_repo.exist(pesto))
    pesto = Product('Pesto', 8888, 'kg')
    for item in product_repo.find_all():
        print(item)
    # for item in product_repo.items.keys():
    #     print(product_repo.items[item.id])



    # print(product_repo.items)
    # product_repo.create(pesto)
    # print(product_repo.find_by_id(pesto))
    # print("Item exists: ", product_repo.exist(pesto))
    # product_repo.load()
    # product_repo.load_from_list(Product.product_list)
    # product_repo.save()
    # # product_repo.load()
    # # product_repo.load_from_list(Product.product_list)
    # product_repo.save()
    # for user in users:
    #     users_repo.create(user)

    # entity_class = Product
    # list_db = Product.product_list
    # with open("Products.json", "rt", encoding="utf-8") as f:
    #     # users = json.load(f, object_hook=object_hook(self.entity_class))  # IIFE
    #     # for user in users:
    #     #     self.create(user)
    #     for item in list_db:
    #         print(f"Item is instance Product: {isinstance(item, entity_class)}")
    #         print(f"Item is in this file already: {item in product_repo.find_all()}")
    #         if isinstance(item, entity_class) and item not in f:
    #             product_repo.create(item)

    # users_repo.print_all_users()
    # entity_class = User
    # users_repo.load()
    # for user in users_repo.find_all():
    #     print(user)
    # print("Find by password ------------> ", users_repo.find_by_password("4444"))
    # print(users_repo.find_all())
    # users_repo.load_from_list(users)
    # for user in users_repo.find_all():
    #     print(user)
    # users_repo.save()

    login_controller = LoginController(users_repo)

    # MAIN_MENU_ITEMS = [
    #     MenuItem("Register new user", RegisterCommand(login_controller)),
    #     MenuItem("Login", LoginCommand(login_controller)),
    #     MenuItem("Logout", LogoutCommand(login_controller)),
    #     MenuItem("Show logged user", GetLoggedUserCommand(login_controller)),
    # ]
    # main_menu = Menu(MAIN_MENU_ITEMS)
    # main_menu.show()
    # print("Good bye!")

    # for user in users:
    #     users_repo.create(user)
    # users_repo.print_all_users()

    # login_controller = LoginController(users_repo)
    # tolik = User('Anatoliy', 'Dukalis', 42, '0981111111', '3333', 'WAITER')
    # login_controller.add_user(tolik)
    # users_repo.print_all_users()

    # print('-' * 100)
    # print('-' * 100)
    # while True:
    #     inp = input("These are the options: Login | Logout | Get current user | Exit"
    #                 "\nType in what would like to do HERE: -> ")
    #     input_options = ('Login'.lower(), 'Logout'.lower(), 'Get current user'.lower(), 'Exit'.lower())
    #     print('-' * 30)
    #     if inp == 'Login'.lower():
    #         password = input("Enter user password: ")
    #         login_controller.login(password)
    #         print('-' * 30)
    #     elif inp == 'Logout'.lower():
    #         login_controller.logout()
    #         print('-' * 30)
    #     elif inp == 'Get current user'.lower() or inp == 'get_current_user':
    #         login_controller.get_logged_user()
    #         print('-' * 30)
    #     elif inp not in input_options:
    #         print(f"{BColors.WARNING}Look, kid, I'm far away from Skynet yet, so I am not able to read your mind. "
    #               f"\nSo can you, PLEASE, type in the option from the menu,{BColors.ENDC}"
    #               f"{BColors.BOLD}{BColors.FAIL} or you're too SLOW???{BColors.ENDC}")
    #         print('-' * 30)
    #     elif inp == 'Exit'.lower():
    #         print(f"{BColors.OKBLUE}{BColors.BOLD}I hope you enjoyed the DEMO. Have a nice day!{BColors.ENDC}")
    #         break
