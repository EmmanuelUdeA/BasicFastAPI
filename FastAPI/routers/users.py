from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Entidad user


class User(BaseModel):
    id: int
    name: str
    lname: str
    age: int
    url: str


users_fake = [
    User(id=1, name="Emma", lname="Valbuena", age=22, url="https://hola.com"),
    User(id=2, name="Emme", lname="Valbuena", age=232, url="https://hola.com"),
    User(id=3, name="Emmi", lname="Valbuena", age=212, url="https://hola.com"),
]


@router.get("/usersjson")
async def usersjson():
    return [
        {
            "name": "Emma",
            "lname": "Valbuena",
            "age": "22",
            "url": "https://instagram.com",
        },
        {
            "name": "Emmi",
            "id": 1,
            "lname": "busta",
            "age": 1,
            "url": "https://pet.com",
        },
        {
            "name": "pepe",
            "lname": "orosz",
            "age": "22",
            "url": "https://instagram.com",
        },
    ]


@router.get("/usersclass")
async def usersclass():
    return users_fake


# path
@router.get("/userpath/{id}")
async def user(id: int):
    return search_user(id)


# Query
@router.get("/userquery/")
async def user(id: int):
    return search_user(id)


# PATH PARAMETRO OBLIGATORIO. URL DINAMICO/USER/ID/PALABRAFIJA/OBJETO/CARACTERISTICA

# QUERY PARAMETROS NO SON NECESARIOS PARA LA PETICIÓN


@router.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "El usuario ya existe"}
    else:
        users_fake.append(user)
        return user


@router.put("/user/")
async def user(user: User):
    found = False

    for index, saved_user in enumerate(users_fake):
        if saved_user.id == user.id:
            users_fake[index] = user
            found = True

    if not found:
        return {"error": "No se ha encontrado el usuario"}
    else:
        return user


@router.delete("/user/{id}")
async def user(id: int):
    found = False

    for index, saved_user in enumerate(users_fake):
        if saved_user.id == id:
            del users_fake[index]
    if not found:
        return {"Error": "No se ha encontrado usuario"}


def search_user(id: int):
    user = filter(lambda user: user.id == id, users_fake)
    try:
        return list(user)[0]
    except:
        return {"error": "No se ha encontrado nada"}
