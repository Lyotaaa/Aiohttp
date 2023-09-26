from pydantic import BaseModel, validator, ValidationError
from typing import Type, Optional
from auxiliary_functions import get_http_error
from aiohttp import web


def validate(json_data, model_class):
    try:
        model = model_class(**json_data)
        return model.dict(exclude_none=True)
    except ValidationError as err:
        raise get_http_error(web.HTTPBadRequest, err.errors()())


class CreateOwner(BaseModel):
    """Валидация данных при создании пользователя"""

    email: str
    password: str

    @validator("email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        return value

    @validator("password")
    def val_password(cls, value):
        if len(value) < 3:
            raise ValueError("Short password")
        return value


class UpdateOwner(BaseModel):
    """Валидация данных при обновлении пользователя"""

    email: str
    password: str

    @validator("email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        return value

    @validator("password")
    def validate_password(cls, value):
        if len(value) < 3:
            raise ValueError("Short password")
        return value


class CreateAds(BaseModel):
    """Валидация данных при создании объявления"""

    title: str
    description: str
    owner_id: int

    @validator("title")
    def secure_title(cls, value):
        if 20 < len(value):
            raise ValueError("Long title")
        return value

    @validator("description")
    def secure_description(cls, value):
        if len(value) > 30:
            raise ValueError("Long description")
        return value


class UpdateAds(BaseModel):
    """Валидация данных при обновлении объявления"""

    title: str
    description: str
    owner_id: int

    @validator("title")
    def secure_title(cls, value):
        if 20 < len(value):
            raise ValueError("Long title")
        return value

    @validator("description")
    def secure_description(cls, value):
        if len(value) > 30:
            raise ValueError("Long description")
        return value
