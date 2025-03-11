import os
from uuid import uuid4

from celery import Celery

import requests

celery = Celery('task', broker="redis://localhost:6379")

@celery.task
def get_pictures(urls: list, name: str) -> None:

    dir = name if name else uuid4()

    try:
        os.makedirs(f"pic/{dir}")
    except Exception as e:
        print(f"Никогда не используйте базовый Exception {e}")
    
    for url in urls:

        r = requests.get(url)

        if r.status_code == 200:
            filedump = r.content

        file_name = f"pic/{dir}/{uuid4()}.jpg"
        with open(file_name, "wb") as f:
            f.write(filedump)
            print(f"файл {file_name} записан на диск")
    
    return dir