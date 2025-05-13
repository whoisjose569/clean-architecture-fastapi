from abc import ABC, abstractmethod
from src.domain.entities.user import User


class IUsersRepository(ABC):

    @abstractmethod
    def insert_user(self, first_name: str, last_name: str, age: int):
        pass

    @abstractmethod
    def select_user(self, first_name: str) -> list[User]:
        pass
