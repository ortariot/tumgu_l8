from http import HTTPStatus
import json # orjson

from fastapi import APIRouter

from db.models.models import Roles
from db.roleservice import role_service

from schemes.scheme import Role, ResponseRole
from db.cacheservice import cache


role_router = APIRouter()


@role_router.post("/create_role/", status_code=HTTPStatus.ACCEPTED)
async def create_role(input: Role):
    role = await role_service.add_role(input.name, input.level)

    return role


@role_router.get(
    "/get_role/{id}",
    status_code=HTTPStatus.OK,
    response_model=ResponseRole
)
async def get_role(id: int):

    role = await cache.get(id)
    if role:
        print("взято из кеша")
        return json.loads(role)

    result = await role_service.get_role(int(id))
    to_cache = result.to_dict()

    await cache.add(id, json.dumps(to_cache), expire=30)

    return result


@role_router.patch("/update_filds_role/{id}", status_code=HTTPStatus.ACCEPTED)
async def update_role(id: int, input: Role):

    # чтобы избежать инвалидации кеша
    await cache.delete(id)

    return await role_service.update_role(id, **input.model_dump())


@role_router.get("/get_roles/", status_code=HTTPStatus.OK)
async def get_roles():
    return await role_service.get_roles()