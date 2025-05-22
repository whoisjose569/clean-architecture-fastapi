from src.presentation.interfaces.controller_interface import IController
from src.domain.use_cases.user_finder import IUserFinder
from src.schemas.user_schema import UserSchemaFindFirstName


class UserFinderController(IController):
    def __init__(self, use_case: IUserFinder):
        self.__use_case = use_case

    def handle(self, data: UserSchemaFindFirstName) -> dict:
        users = self.__use_case.find(data.first_name)

        response = {
            "type": "Users",
            "count": len(users),
            "attributes": [
                {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "age": user.age,
                }
                for user in users
            ],
        }
        return response
