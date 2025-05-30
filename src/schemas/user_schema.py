from pydantic import BaseModel, field_validator
from src.errors.types import HttpBadRequestError
import re


class UserSchemaIn(BaseModel):
    first_name: str
    last_name: str
    age: int

    @field_validator("first_name", "last_name")
    @classmethod
    def only_letters(cls, value: str):
        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", value):
            raise HttpBadRequestError("Only letters and spaces are allowed")
        return value


class UserSchemaFindFirstName(BaseModel):
    first_name: str

    @field_validator("first_name")
    @classmethod
    def only_letters(cls, value: str):
        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", value):
            raise HttpBadRequestError("Only letters and spaces are allowed")
        return value
