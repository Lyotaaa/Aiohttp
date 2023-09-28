from pydantic import BaseModel, validator, ValidationError
from typing import Optional
from auxiliary_functions import get_http_error
from aiohttp import web


def validate(json_data: dict, model_class):
    try:
        model = model_class(**json_data)
        return model.dict(exclude_none=True)
    except ValidationError as err:
        raise get_http_error(web.HTTPBadRequest, err.errors())


class CreateUser(BaseModel):
    """Валидация данных при создании пользователя"""

    name: str
    password: str

    @validator("name")
    def validate_name(cls, value):
        if len(value) > 10:
            raise get_http_error(web.HTTPBadRequest, "Long name")
            # raise ValueError("Long name")
        return value

    @validator("password")
    def validate_password(cls, value):
        if len(value) < 2:
            raise get_http_error(web.HTTPBadRequest, "Short password")
            # raise ValueError("Short password")
        return value


class UpdateUser(BaseModel):
    """Валидация данных при обновлении пользователя"""

    name: Optional[str] = None
    password: Optional[str] = None

    @validator("name")
    def validate_name(cls, value):
        if value is not None:
            if len(value) > 10:
                raise get_http_error(web.HTTPBadRequest, "Long name")
        return value

    @validator("password")
    def validate_password(cls, value):
        if value is not None:
            if len(value) < 2:
                raise get_http_error(web.HTTPBadRequest, "Short password")
        return value


class CreateAds(BaseModel):
    """Валидация данных при создании объявления"""

    title: str
    description: str
    user_id: int

    @validator("title")
    def validate_title(cls, value):
        if 10 < len(value):
            raise get_http_error(web.HTTPBadRequest, "Long title")
            # raise ValueError("Long title")
        return value

    @validator("description")
    def validate_description(cls, value):
        if len(value) > 15:
            raise get_http_error(web.HTTPBadRequest, "Long description")
            # raise ValueError("Long description")
        return value


class UpdateAds(BaseModel):
    """Валидация данных при обновлении объявления"""

    title: Optional[str] = None
    description: Optional[str] = None
    user_id: int

    @validator("title")
    def validate_title(cls, value):
        if value is not None:
            if 10 < len(value):
                raise get_http_error(web.HTTPBadRequest, "Long title")
            # raise ValueError("Long title")
        return value

    @validator("description")
    def validate_description(cls, value):
        if value is not None:
            if len(value) > 15:
                raise get_http_error(web.HTTPBadRequest, "Long description")
            # raise ValueError("Long description")
        return value
