import uvicorn
from fastapi import FastAPI


from core.settings import settings

# from api.v1.user import user_router
from api.v1.role import role_router

# from api.v1.auth import auth_router
# from api.v1.background import background_router

app = FastAPI(
    title=settings.project_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    )

# app.include_router(user_router, prefix="/api/v1/users")
app.include_router(role_router, prefix="/api/v1/roles")
# app.include_router(auth_router, prefix="/api/v1/auth")
# app.include_router(background_router, prefix="/api/v1/pics")


if __name__ == "__main__":
    print(settings)
    uvicorn.run(
        "main:app",
        host=settings.ptoject_host,
        port=settings.project_port,
        reload=True,
    )

