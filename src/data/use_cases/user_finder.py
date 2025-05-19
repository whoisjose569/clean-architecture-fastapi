from src.domain.use_cases.user_finder import IUserFinder
from src.domain.repositories.users_repository import IUsersRepository


class UserFinder(IUserFinder):
    def __init__(self, users_repository: IUsersRepository):
        self.__users_repository = users_repository

    def find(self, first_name: str) -> dict:
        users_on_db = self.__users_repository.select_user(first_name)
        if users_on_db == []:
            raise Exception("Usuario não Encontrado")

        response = {
            "type": "Users",
            "count": len(users_on_db),
            "attributes": [
                {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "age": user.age,
                }
                for user in users_on_db
            ],
        }

        return response
