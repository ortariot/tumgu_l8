import pickle

from redis.asyncio import Redis

from core.settings import settings


cache = Redis(host="localhost", port = 6379)


class MyExeption(Exception):
    pass


class Cache:

    def __init__(self, host, port):
        self.cache = Redis(host=host, port = port)


    async def add(
        self, key=None, value=None, expire=None, **kwargs
    ):

        if key and value:
            await self.cache.set(key, pickle.dumps(value), expire)
        elif kwargs:
            for key, value in kwargs.items():
                await self.cache.set(key, value, expire)
        else:
            raise MyExeption("broken arguments")

    
    async def get(self, key: str):
        data = await self.cache.get(key) 
        return pickle.loads(data) if data else None

    
    async def delete(self, key: str):
        await self.cache.delete(key)


cache = Cache(settings.redis_host, settings.redis_port)

