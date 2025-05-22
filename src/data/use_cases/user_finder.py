from src.domain.use_cases.user_finder import IUserFinder
from src.domain.repositories.users_repository import IUsersRepository
from src.domain.entities.user import User


class UserFinder(IUserFinder):
    def __init__(self, users_repository: IUsersRepository):
        self.__users_repository = users_repository

    def find(self, first_name: str) -> list[User]:
        users_on_db = self.__users_repository.select_user(first_name)
        if users_on_db == []:
            raise Exception("Usuario não Encontrado")

        return users_on_db
