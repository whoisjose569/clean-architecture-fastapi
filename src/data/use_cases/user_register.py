from src.domain.use_cases.user_register import IUserRegister
from src.domain.repositories.users_repository import IUsersRepository
from src.domain.entities.user import User


class UserRegister(IUserRegister):
    def __init__(self, user_repository: IUsersRepository):
        self.__user_repository = user_repository

    def register(self, user: User) -> None:
        self.__user_repository.insert_user(
            first_name=user.first_name, last_name=user.last_name, age=user.age
        )
