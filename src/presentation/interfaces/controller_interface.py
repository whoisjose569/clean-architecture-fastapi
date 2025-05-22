from abc import ABC, abstractmethod
from pydantic import BaseModel


class IController(ABC):

    @abstractmethod
    def handle(self, data: BaseModel) -> dict:
        pass
