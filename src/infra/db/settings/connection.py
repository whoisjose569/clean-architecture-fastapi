import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = os.getenv("DATABASE_URL")
        self.__engine = self.__create_database_engine()

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine
