import json

import pytest
from redis.asyncio import Redis
from redis import exceptions as redis_exeptions
import aiohttp
import pytest_asyncio
# pip install pytest-asyncio
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy import create_engine

from db.models.models import Base



@pytest_asyncio.fixture(scope="function")
async def aiohht_client():
    session = aiohttp.ClientSession()
    yield session
    await session.close()


@pytest_asyncio.fixture(scope="function")
def make_request(aiohht_client):
    async def inner(method, url, params, args=None):
        response = await aiohht_client.request(
            method,
            url,
            json=params,
            params=args
        )
        return response

    return inner

PG_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"
SYNC_PG_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

@pytest_asyncio.fixture(scope="function")
async def test_engine():
    engine =  create_async_engine(PG_URL)
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield engine
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)




@pytest_asyncio.fixture(scope="function")
async def test_session(test_engine):

    async_sesion_factory = sessionmaker(
        test_engine, expire_on_commit=False, class_=AsyncSession
    )
    async with async_sesion_factory() as session:
        yield session