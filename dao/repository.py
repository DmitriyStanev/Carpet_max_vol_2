import uuid

from entity.product import Product


class Repository:
    def __init__(self):
        self.items = {}

    def create(self, item):
        if not self.exist(item):
            item.id = str(uuid.uuid1())
            self.items[item.id] = item
        return item

    def update(self, item):
        if item.id not in self.items:
            return None
        self.items[item.id] = item
        return item

    def delete_by_id(self, id):
        if id in self.items:
            old = self.items[id]
        else:
            return None
        del self.items[id]
        return old

    def find_all(self):
        return list(self.items.values())

    def find_by_id(self, item):
        if item.id not in self.items:
            return None
        return self.items[item.id]

    def find_by_name(self, name):
        if name not in self.items:
            return None
        return self.items[name]

    def count(self):
        return len(self.items)

    def exist(self, item):
        if isinstance(item, Product):
            for product in self.items.values():
                if product.name == item.name:
                    return True
        else:
            return item.id in self.items.keys()
