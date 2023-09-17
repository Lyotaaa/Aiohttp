import pydantic
from errors import HttpError
from hashlib import md5


def validate(json_data, model_class):
    try:
        model = model_class(**json_data)
        return model.dict(exclude_none=True)
    except pydantic.ValidationError as err:
        raise HttpError(400, err.errors())


def hash_password(password: str):
    password = password.encode()
    password = md5(password).hexdigest()
    return password


class CreateOwner(pydantic.BaseModel):
    """Валидация данных при создании пользователя"""

    email: str
    password: str

    @pydantic.validator("email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        return value

    @pydantic.validator("password")
    def val_password(cls, value):
        if len(value) < 3:
            raise ValueError("Short password")
        return value


class UpdateOwner(pydantic.BaseModel):
    """Валидация данных при обновлении пользователя"""

    email: str
    password: str

    @pydantic.validator("email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        return value

    @pydantic.validator("password")
    def validate_password(cls, value):
        if len(value) < 3:
            raise ValueError("Short password")
        return value


class CreateAds(pydantic.BaseModel):
    """Валидация данных при создании объявления"""

    title: str
    description: str
    owner_id: int

    @pydantic.validator("title")
    def secure_title(cls, value):
        if 20 < len(value):
            raise ValueError("Long title")
        return value

    @pydantic.validator("description")
    def secure_description(cls, value):
        if len(value) > 30:
            raise ValueError("Long description")
        return value


class UpdateAds(pydantic.BaseModel):
    """Валидация данных при обновлении объявления"""

    title: str
    description: str
    owner_id: int

    @pydantic.validator("title")
    def secure_title(cls, value):
        if 20 < len(value):
            raise ValueError("Long title")
        return value

    @pydantic.validator("description")
    def secure_description(cls, value):
        if len(value) > 30:
            raise ValueError("Long description")
        return value
