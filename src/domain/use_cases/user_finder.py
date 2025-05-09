from abc import ABC, abstractmethod


class IUserFinder(ABC):

    @abstractmethod
    def find(self, first_name: str) -> dict:
        pass
