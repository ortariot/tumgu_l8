from celery import Celery


client = Celery('task', broker="redis://localhost:6379")

