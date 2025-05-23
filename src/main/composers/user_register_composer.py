from src.presentation.controllers.user_register_controller import UserRegisterController
from src.data.use_cases.user_register import UserRegister
from src.infra.db.repositories.users_repository import UserRepository


def user_register_composer():
    repository = UserRepository()
    use_case = UserRegister(repository)
    controller = UserRegisterController(use_case)

    return controller.handle
