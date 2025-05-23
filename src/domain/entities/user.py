from typing import Optional


class User:
    def __init__(
        self, first_name: str, last_name: str, age: int, id: Optional[int] = None
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
