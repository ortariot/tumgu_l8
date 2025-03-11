# Вебинар 8. Деплой в docker


## requirements:
```
asyncpg==0.30.0
celery==5.4.0
fastapi==0.115.8
httpx==0.28.1
passlib==1.7.4
psycopg2-binary==2.9.10
pydantic==2.10.6
PyJWT==2.10.1
redis==5.2.1
requests==2.32.3
SQLAlchemy==2.0.38
uvicorn=0.34.0
pydantic_settings=2.8.1
pytest=8.3.5
pytest-asyncio=0.25.3
aiohttp=3.11.13
alembic=1.15.1
```

## to start:

- docker compose up -d


## celery start:

- celery -A tasker.task worker --loglevel=info


## tests start:

- pytest tests/src/ 
