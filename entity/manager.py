from entity.user import User
from entity.waiter import Waiter


class Manager(User):
    next_id = 0

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id
    # def __init__(self,  name: str, last_name: str, age: int, phone_number: str, log_password: str, gender):
    #     super().__init__(name: str, last_name: str, age: int, phone_number: str, log_password: str):
    #     # User.__init__(self,  name: str, last_name: str, age: int, phone_number: str, log_password: str)
    #     self.gender = "Male"

    # def create_waiter(self, waiter: Waiter):

