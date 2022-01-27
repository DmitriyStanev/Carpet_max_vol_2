class Product:
    product_list = set()
    next_id = 0  # unique id sequence

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id

    def __init__(self, name: str, delivery_price: float, measure_unit: str):
        self.id = self.get_next_id()
        self.name = name
        self.delivery_price = delivery_price
        self.measure_unit = measure_unit
        self.product_list.add(self)

    def __str__(self):
        return f"ID: {self.id} | {self.name} | {self.delivery_price} | {self.measure_unit} |"
