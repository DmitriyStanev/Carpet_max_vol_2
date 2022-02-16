from dao.user_repository import UserRepository
from entity.user import User
from exception.credentials_exception import CredentialsException

"""Login controller should not print anything. It should just return statements."""


class LoginController:
    _current_user = None

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def add_user(self, user: User) -> User:
        # TODO validate user
        created = self.user_repo.create(user)
        self.user_repo.save()
        return created

    def login(self, password: str) -> User:
        user = self.user_repo.find_by_password(password)
        if user is not None and user.log_password == password:
            self._current_user = user
            return user
        raise CredentialsException("Invalid username or password. Try again...")

    def get_logged_user(self):
        return self._current_user

    def logout(self):
        self._current_user = None

    # def login(self, password: str):
    #     user_exists = False
    #     for user in self.user_repo.find_all():
    #         if password == user.log_password:
    #             user_exists = True
    #             greeting_string = f"User {user.name} successfully logged in."
    #             print("*" * len(greeting_string))
    #             print(greeting_string)
    #             print("*" * len(greeting_string))
    #             self._current_user = user
    #             return user
    #     if not user_exists:
    #         # raise InvalidUsernameOrPasswordException
    #         error_string = 'There is no such user or the password is not correct.' \
    #                        '\nTalk with your manager to register you to the system or try to enter the password again:'
    #         print("*" * int(len(error_string) / 2))
    #         print(error_string)
    #         print("*" * int(len(error_string) / 2))
    #     # if not user_exists:
    #     #     return InvalidUsernameOrPasswordException

    # def get_logged_user(self):
    #     if self._current_user:
    #         print(f"| {'Last name':<10.10s} | {'Name':<10.10s} | {'Age'} | {'Phone':>11.11s} "
    #               f"| {'Position':>9.9s} | {'ID'} |")
    #         print(self._current_user)
    #     else:
    #         print(f"So tell me, hoh there can be a logged user, if you didn't log in yet??? \n"
    #               f"Current user: {self._current_user}")

    # def logout(self):
    #     if self._current_user:
    #         good_bye_string = f"Bye-bye,  {self._current_user.name}. Come back to work soon!!!"
    #         print("*" * len(good_bye_string))
    #         print(good_bye_string)
    #         print("*" * len(good_bye_string))
    #         self._current_user = None
    #     else:
    #         print('Nobody is logged in, how can NOBODY log OUT??? Are you stupid?')

# class InvalidUsernameOrPasswordException(Exception):
#     # super(InvalidUsernameOrPasswordException, self).()
#     print('InvalidUsernameOrPasswordException')




