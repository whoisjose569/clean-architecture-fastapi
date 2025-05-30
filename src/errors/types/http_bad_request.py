from .base import HttpError

class HttpBadRequestError(HttpError):
    def __init__(self, message: str = "Bad request"):
        super().__init__(message=message, status_code=400, name="BadRequest")
