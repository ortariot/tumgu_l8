from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class ApiConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    project_name: str = "test"
    project_port: int = 8000
    ptoject_host: str = "0.0.0.0"

    pg_user: str = "postgres"
    pg_password: str = "postgres"
    pg_db: str = "postgres"
    pg_port: int = 5432
    pg_host: str = "localhost"

    redis_host: str = "localhost"
    redis_port: int = 6379

    jwt_secret_key: str = 'JWT_SECRET_KEY'
    jwt_algorithm: str = 'JWT_ALGORITHM'

    pg_auth: URL | None = None


settings = ApiConfig()


settings.pg_auth = URL.create(
    "postgresql+asyncpg",
    username=settings.pg_user,
    password=settings.pg_password,
    host=settings.pg_host,
    port=settings.pg_port,
    database=settings.pg_db,
)

if __name__ == "__main__":

    print(settings)
