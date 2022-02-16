from controller.login_controller import LoginController
from entity.user import User
from exception import credentials_exception
from exception.credentials_exception import CredentialsException
from view.menu import Command, MenuItem


class LoginCommand(Command):
    def __init__(self, login_controller: LoginController):
        self.login_controller = login_controller

    def run(self) -> str:
        # username = input("Enter username:")
        password = input("Enter password:")
        try:
            user = self.login_controller.login(password)
        except CredentialsException as ex:
            return str(ex)
        return f"Hello, {user.name} {user.last_name} [{user.role}]!"


class LogoutCommand(Command):
    def __init__(self, login_controller: LoginController):
        self.login_controller = login_controller

    def run(self) -> str:
        self.login_controller.logout()
        return f"You have successfully logged out."


class GetLoggedUserCommand(Command):
    def __init__(self, login_controller: LoginController):
        self.login_controller = login_controller

    def run(self) -> str:
        user = self.login_controller.get_logged_user()
        if user is not None:
            return f"You are logged as: {user.name} {user.last_name} [{user.role}]."
        else:
            return "No user logged in."


class RegisterCommand(Command):
    def __init__(self, login_controller: LoginController):
        self.login_controller = login_controller

    def run(self) -> str:
        first_name = input("Enter first name:")
        last_name = input("Enter last name:")
        age = input("Enter yor age:")
        phone_number = input("Enter yor phone number:")
        password = input("Enter password:")
        role = input("Enter your Role:")
        user = self.login_controller.add_user(User(first_name, last_name, int(age), phone_number, password, role))
        return f"You are successfully registered as: {user.name} {user.last_name} [{user.role}]."
