from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.models.users import Users
from src.domain.repositories.users_repository import IUsersRepository
from src.domain.entities.user import User


class UserRepository(IUsersRepository):

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        with DBConnectionHandler() as database:
            try:
                new_registry = Users(
                    first_name=first_name, last_name=last_name, age=age
                )
                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_user(cls, first_name: str) -> list[User]:
        with DBConnectionHandler() as database:
            try:
                registry_on_db = (
                    database.session.query(Users)
                    .filter(Users.first_name == first_name)
                    .all()
                )
                return registry_on_db
            except Exception as exception:
                database.session.rollback()
                raise exception
