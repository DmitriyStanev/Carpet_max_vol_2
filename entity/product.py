import uuid


class Product:
    product_list = set()
    product_price_list = {}
    products_db_list = list()
    next_id = 0  # unique id sequence

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id

    def __init__(self, name=None, delivery_price=None, measure_unit=None, quantity=None):
        self.id = str(uuid.uuid1())
        self.name = name
        self.delivery_price = delivery_price
        self.measure_unit = measure_unit
        self.quantity = quantity
        self.product_list.add(self)
        if self.name not in self.product_price_list:
            self.product_price_list[name] = delivery_price

    def __str__(self):
        return f"ID: {self.id} | {self.name} | {self.delivery_price} | {self.measure_unit} |"
