from dao.user_repository import UserRepository
from entity.user import User


class LoginController:
    current_user = None

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def add_user(self, user: User):
        self.user_repo.create(user)

    def get_logged_user(self):
        if self.current_user:
            print(f"| {'Last name':<10.10s} | {'Name':<10.10s} | {'Age'} | {'Phone':>11.11s} "
                  f"| {'Position':>9.9s} | {'ID'} |")
            print(self.current_user)
        else:
            print(f"So tell me, hoh there can be a logged user, if you didn't log in yet??? \n"
                  f"Current user: {self.current_user}")

    def login(self, password: str):
        user_exists = False
        for user in self.user_repo.find_all():
            if password == user.log_password:
                user_exists = True
                greeting_string = f"User {user.name} successfully logged in."
                print("*" * len(greeting_string))
                print(greeting_string)
                print("*" * len(greeting_string))
                self.current_user = user
                return user
        if not user_exists:
            error_string = 'There is no such user or the password is not correct.' \
                           '\nTalk with your manager to register you to the system or try to enter the password again:'
        print("*" * int(len(error_string) / 2))
        print(error_string)
        print("*" * int(len(error_string) / 2))
        # if not user_exists:
        #     return InvalidUsernameOrPasswordException

    def logout(self):
        if self.current_user:
            good_bye_string = f"Bye-bye,  {self.current_user.name}. Come back to work soon!!!"
            print("*" * len(good_bye_string))
            print(good_bye_string)
            print("*" * len(good_bye_string))
            self.current_user = None
        else:
            print('Nobody is logged in, how can NOBODY log OUT??? Are you stupid?')


class InvalidUsernameOrPasswordException(Exception):
    print('InvalidUsernameOrPasswordException')




