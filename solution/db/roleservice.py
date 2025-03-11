import asyncio

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from db.models.models import Roles
from core.settings import settings

class RoleService():

    def __init__(self, db_url):
        self.db_url = db_url


    def get_async_session(self) -> AsyncSession:

        engine =  create_async_engine(self.db_url)


        return sessionmaker(
            engine,
            class_ = AsyncSession,
            expire_on_commit=False
        )


    async def add_role(self, name, level):

        session = self.get_async_session()

        role = Roles(name=name, level=level)

        async with session() as db:
            db.add(role)
            await db.commit()

            return role

    async def get_roles(self):

        session = self.get_async_session()

        async with session() as db:

            roles = await db.execute(select(Roles))
            return roles.scalars().all()

    async def get_role(self, id):

        session = self.get_async_session()

        async with session() as db:

            roles = await db.execute(select(Roles).where(Roles.id==id))
            return roles.scalars().one()

    async def update_role(self, id, **kwargs):
        
        session = self.get_async_session()

        async with session() as db:
            role = await db.execute(select(Roles).where(Roles.id == id))

            role = role.scalars().one()


            for key, value in kwargs.items():
                setattr(role, key, value)

            await db.commit()

            return role



role_service = RoleService(settings.pg_auth)



if __name__ == "__main__":
    role_service = RoleService(settings.pg_auth)

    res = role_service.get_roles()

    print(res)
