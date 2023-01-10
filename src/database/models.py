from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int] = 1


class Orders(BaseModelModify):
    datetime: str
    menu_position_id: int
    user_id: int


class Cuisine(BaseModelModify):
    name: str


class Dish(BaseModelModify):
    name: str
    cooking_time: int
    cuisine_id: int


class Menu(BaseModelModify):
    price: int
    dish_id: int


class User(BaseModelModify):
    name: str
    password: str
    post: str


class UserAuth(BaseModel):
    name: str
    password: str

