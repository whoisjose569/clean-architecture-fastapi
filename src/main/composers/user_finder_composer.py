from src.presentation.controllers.user_finder_controller import UserFinderController
from src.data.use_cases.user_finder import UserFinder
from src.infra.db.repositories.users_repository import UserRepository


def user_finder_composer():
    repository = UserRepository()
    use_case = UserFinder(repository)
    controller = UserFinderController(use_case)

    return controller.handle
