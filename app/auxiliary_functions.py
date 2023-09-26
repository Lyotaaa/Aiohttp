import json
from hashlib import md5
from aiohttp import web
from app.config_db import engine, Base, Session
from app.models import User, Ads
from sqlalchemy.exc import IntegrityError


async def context_orm(app: web.Application):
    print("START")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.creat_all)
    yield
    await engine.despose()
    print("STOP")


@web.middleware
async def session_middleware(request: web.Request, handler):
    async with Session() as session:
        request["session"] = session
        response = await handler(request)
        return response


def hash_password(password: str):
    password = password.encode()
    password = md5(password).hexdigest()
    return password


def get_http_error(error_class, description: str):
    return error_class(
        text=json.dumps(
            {"status": "error", "description": description},
            content_type="application/json",
        )
    )


async def get_user(user_id: int, session: Session):
    user = await session.get(User, user_id)
    if user is None:
        raise get_http_error(web.HTTPNotFound, "user not found")
    return user


async def get_ads(ads_id: int, session: Session):
    ads = await session.get(Ads, ads_id)
    if ads is None:
        raise get_http_error(web.HTTPNotFound, "Ads not found")
    return ads


async def add_user(user: User, session: Session):
    try:
        session.add(user)
        await session.commit()
    except IntegrityError as er:
        raise get_http_error(web.HTTPConflict, "User already exists")


async def add_ads(ads: Ads, session: Session):
    try:
        session.add(ads)
        await session.commit()
    except IntegrityError as er:
        raise get_http_error(web.HTTPConflict, "Ads already exists")
