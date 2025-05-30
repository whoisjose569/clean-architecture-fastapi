from .base import HttpError

class HttpNotFoundError(HttpError):
    def __init__(self, message: str = "Not Found"):
        super().__init__(message=message, status_code=404, name="NotFound")