from src.presentation.interfaces.controller_interface import IController
from src.domain.use_cases.user_register import IUserRegister
from src.schemas.user_schema import UserSchemaIn
from src.domain.entities.user import User


class UserRegisterController(IController):
    def __init__(self, use_case: IUserRegister):
        self.__use_case = use_case

    def handle(self, data: UserSchemaIn) -> dict:
        user_entity = User(**data.model_dump())

        self.__use_case.register(user_entity)

        response = {
            "type": "Users",
            "count": 1,
            "attributes": {
                "first_name": user_entity.first_name,
                "last_name": user_entity.last_name,
                "age": user_entity.age,
            },
        }

        return response
