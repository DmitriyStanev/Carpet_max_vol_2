

class User:
    next_id = 0

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id

    def __init__(self, name, last_name, age, log_password):
        self.id = self.get_next_id()
        self.name = name
        self.last_name = last_name
        self.age = age
        self.log_password = log_password

    def __str__(self):
        return f"| {self.id} | {self.name} | {self.last_name} | {self.age} "