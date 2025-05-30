from fastapi.responses import JSONResponse
from fastapi import Request
from .types.base import HttpError

async def http_error_handler(request: Request, exc: HttpError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.name,
            "message": exc.message
        },
    )