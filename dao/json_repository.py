import json

from dao.repository import Repository
from entity.user import User


class JsonRepository(Repository):
    def __init__(self, db_filename, entity_class):
        super().__init__()
        self.db_filename = db_filename
        self.entity_class = entity_class

    def save(self):
        with open(self.db_filename, "wt", encoding="utf-8") as f:
            json.dump(self.find_all(), f, indent=4, default=dumper)

    def load(self):
        with open(self.db_filename, "rt", encoding="utf-8") as f:
            items = json.load(f, object_hook=object_hook(self.entity_class))  # IIFE
            # users = json.load(f)
            for item in items:
                if isinstance(item, self.entity_class) and item not in self.find_all():
                    self.create(item)

    def load_from_list(self, list_db):
        with open(self.db_filename, "rt", encoding="utf-8") as f:
            # users = json.load(f, object_hook=object_hook(self.entity_class))  # IIFE
            # for user in users:
            #     self.create(user)
            for item in list_db:
                if isinstance(item, self.entity_class) and item not in self.find_all():
                    self.create(item)


# Helpers
def dumper(obj):
    try:
        return obj.to_json()
    except:
        return obj.__dict__


entity_class = None


def object_hook(entity_class): #HOF
    def obj_hook(jsdict):
        obj = entity_class()
        obj.__dict__ = jsdict
        return obj
    return obj_hook
