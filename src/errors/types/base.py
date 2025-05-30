class HttpError(Exception):
    def __init__(self, message: str, status_code: int, name: str = "HttpError"):
        self.message = message
        self.status_code = status_code
        self.name = name
        super().__init__(message)