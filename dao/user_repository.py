from dao.json_repository import JsonRepository
from entity.user import User
from util.fun_util import find


class UserRepository(JsonRepository):
    def find_by_username(self, username: str) -> User or None:  # | None:
        users_list = self.find_all()
        results = find(lambda user: user.username == username, users_list)
        return results

    def find_by_password(self, log_password: str) -> User or None:  # | None:
        users_list = self.find_all()
        results = find(lambda user: user.log_password == log_password, users_list)
        return results

    # def print_all_users(self):
    #     print('_' * 64)
    #     print(f"| {'Last name':<10.10s} | {'Name':<10.10s} | {'Age'} | {'Phone':>11.11s} "
    #           f"| {'Position':>9.9s} | {'ID'} |")
    #     print('‾' * 64)
    #     for user in self.find_all():
    #         print(user)

        # def find_by_password(self, password):
        #     if password not in self.items:
        #         return None
        #     return self.items[id]
