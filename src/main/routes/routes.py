from fastapi import APIRouter, Depends
from src.schemas.user_schema import UserSchemaFindFirstName
from src.schemas.user_schema import UserSchemaIn
from src.main.composers.user_finder_composer import user_finder_composer
from src.main.composers.user_register_composer import user_register_composer


user_router = APIRouter(prefix="/user")


@user_router.get("/")
def find_user(data: UserSchemaFindFirstName = Depends()):
    controller = user_finder_composer()
    return controller(data)


@user_router.post("/")
def register_user(data: UserSchemaIn):
    controller = user_register_composer()
    return controller(data)
