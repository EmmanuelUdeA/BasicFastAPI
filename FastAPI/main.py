from fastapi import FastAPI
from routers import products, users, basic_auth_user, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()


# routers
app.include_router(products.router)
app.include_router(users.router)

app.include_router(basic_auth_user.router)
app.include_router(jwt_auth_users.router)

app.include_router(users_db.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/url")
async def root():
    return {"url_curso": "https://www.python.org"}
