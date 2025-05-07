from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.models.users import Users


class UserRepository:

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
