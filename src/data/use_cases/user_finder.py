from src.domain.use_cases.user_finder import IUserFinder
from src.domain.repositories.users_repository import IUsersRepository


class UserFinder(IUserFinder):
    def __init__(self, users_repository: IUsersRepository):
        self.__users_repository = users_repository

    def find(self, first_name: str) -> dict:
        pass
