
from abc import ABC, abstractmethod
class AuthInterface(ABC):
    @abstractmethod
    def get_user(self, flask_request) -> any:
        pass

    @abstractmethod
    def is_logged_in(self, user: any) -> bool:
        pass

    @abstractmethod
    def override_config_for_user(self, user: any, config: dict) -> dict:
        pass

    @abstractmethod
    def login_form(self) -> str:
        pass

    @abstractmethod
    def login_handler(self, flask_request) -> str:
        pass

    @abstractmethod
    def callback_handler(self, flask_request) -> str:
        pass

    @abstractmethod
    def logout_handler(self, flask_request) -> str:
        pass


class NoAuth(AuthInterface):
    def get_user(self, flask_request) -> any:
        return None

    def is_logged_in(self, user: any) -> bool:
        return True

    def override_config_for_user(self, user: any, config: dict) -> dict:
        return config

    def login_form(self) -> str:
        return "Login is not required."

    def login_handler(self, flask_request) -> str:
        return "Login is not required."

    def callback_handler(self, flask_request) -> str:
        return "Callback is not required."

    def logout_handler(self, flask_request) -> str:
        return "Logout is not required."