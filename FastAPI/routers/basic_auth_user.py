from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "Emma": {
        "username": "Emma",
        "full_name": "Emmanuel Bustamante",
        "email": "e1valbuena132@gmail.com",
        "disabled": False,
        "password": "123456",
    },
    "Emma2": {
        "username": "Emma2",
        "full_name": "Emmanuel Bustamante2",
        "email": "e1valbuena2@gmail.com",
        "disabled": True,
        "password": "654321",
    },
    "Emma3": {
        "username": "Emma3",
        "full_name": "Emmanuel3 Bustamante",
        "email": "e1valbuena3@gmail.com",
        "disabled": False,
        "password": "123446",
    },
    "Emma4": {
        "username": "Emma4",
        "full_name": "Emmanuel4 Bustamante",
        "email": "e1valbuena132@gmail.com",
        "disabled": False,
        "password": "123456",
    },
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])


async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion invalida ",
            headers={"www-Authenticate": "Bearer"},
        )
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo"
        )
    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="El usuario no es correcto  ")
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="LA contraseña no es correcto  ")

    return {"access_token": user.username, "token_type": "bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
