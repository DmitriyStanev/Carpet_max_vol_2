class User:
    next_id = 0
    all_users = set()

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id

    def __init__(self, name: str, last_name: str, age: int, phone_number: str, log_password: str):
        self.id = self.get_next_id()
        self.name = name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.log_password = log_password
        self.job_position = self.__class__.__name__
        self.all_users.add(self)

    def __str__(self):
        return f"| {self.last_name:<10.10s} | {self.name:<10.10s} | {self.age:<3d} | {self.phone_number:>11.11s} " \
               f"| {self.job_position:>9.9s} | {self.id} |"

