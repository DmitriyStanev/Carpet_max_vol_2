from dao.repository import Repository


class UserRepository(Repository):
    def print_all_users(self):
        print('_' * 64)
        print(f"| {'Last name':<10.10s} | {'Name':<10.10s} | {'Age'} | {'Phone':>11.11s} "
              f"| {'Position':>9.9s} | {'ID'} |")
        print('‾' * 64)
        for user in self.find_all():
            print(user)

        # def find_by_password(self, password):
        #     if password not in self.items:
        #         return None
        #     return self.items[id]
