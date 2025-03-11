import os
import asyncio

from uuid import uuid4
import time

from httpx import AsyncClient # pip install httpx
from redis.asyncio import Redis

cache = Redis(host="localhost", port = 6379)


URL1 = "https://www.ixbt.com/img/n1/news/2023/6/4/IMG_0826_large.JPG"
URL2 = "https://www.ixbt.com/img/n1/news/2023/6/4/IMG_0828_large.JPG"
URL3 = "https://www.ixbt.com/img/n1/news/2023/6/4/IMG_0829_large.JPG"
URL4 = "https://s3.stroi-news.ru/img/batareya-na-lodzhii-dizain-krasivo-37.jpg"
URL5 = "https://s3.stroi-news.ru/img/batareya-na-lodzhii-dizain-krasivo-47.jpg"
URL6 = "https://s3.stroi-news.ru/img/batareya-na-lodzhii-dizain-krasivo-14.jpg"
URL7 = "https://s3.stroi-news.ru/img/batareya-na-lodzhii-dizain-krasivo-33.jpg"
URL8 = "https://s3.stroi-news.ru/img/batareya-na-lodzhii-dizain-krasivo-43.jpg"
URL9 = "https://s3.stroi-news.ru/img/batareya-na-lodzhii-dizain-krasivo-13.jpg"
URL0 = "https://s3.stroi-news.ru/img/batareya-na-lodzhii-dizain-krasivo-56.png"


url = [URL1, URL2, URL3, URL5, URL6, URL7, URL8, URL9, URL0]


async def get_pictures(urls: list, name: str) -> None:

    dir = name if name else uuid4()

    os.makedirs(f"pic/{dir}")
    
    for url in urls:

        filedump = await cache.get(url)

        if filedump:
            print("Берём картинку из кеша")
        else:
            print("Берём картинку из сети")     
            async with AsyncClient() as client:
                r = await client.get(url)

            if r.status_code == 200:
                filedump = r.content
                await cache.set(name=url, value=filedump, ex=60)   

        file_name = f"pic/{dir}/{uuid4()}.jpg"

        with open(file_name, "wb") as f:
            f.write(filedump)
            print(f"файл {file_name} записан на диск")
    
    return dir


async def runner():


    tm1 = time.time()

    name = f"folder-{uuid4()}"
    await get_pictures(url, name)
    tm2 = time.time()
    print(tm2 - tm1)


if __name__ == "__main__":

    asyncio.run(runner())
