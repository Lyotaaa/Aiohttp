import typing
import json
from aiohttp import web
from models import engine, Session, User, Base

from sqlalchemy.exc import IntegrityError

app = web.Application()


async def context_orm(app: web.Application):
    print("START")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()
    print("STOP")


@web.middleware
async def session_middleware(request: web.Request, handler):
    async with Session() as session:
        request["session"] = session
        response = await handler(request)
        return response


app.cleanup_ctx.append(context_orm)
app.middlewares.append(session_middleware)


def get_http_error(error_class, description: str):
    return error_class(
        text=json.dumps({"status": "error", "description": description}),
        content_type="application/json",
    )


async def get_user(user_id: int, session: Session):
    user = await session.get(User, user_id)
    if user is None:
        raise get_http_error(web.HTTPNotFound, "User not found")
    return user


async def add_user(user: User, session: Session):
    try:
        session.add(user)
        await session.commit()
    except IntegrityError as er:
        raise get_http_error(web.HTTPConflict, "User already exists")
    return user


class UserView(web.View):
    @property
    def session(self):
        return self.request["session"]

    @property
    def user_id(self):
        return int(self.request.match_info["user_id"])

    async def get(self):
        user = await get_user(self.user_id, self.session)
        return web.json_response(
            {
                "id": user.id,
                "name": user.name,
                "creation_time": user.creation_time.isoformat(),
            }
        )

    async def post(self):
        json_validated = await self.request.json()
        user = User(**json_validated)
        user = await add_user(user, self.session)
        return web.json_response(
            {
                "id": user.id,
            }
        )

    async def patch(self):
        json_validated = await self.request.json()
        user = await get_user(self.user_id, self.session)
        for field, value in json_validated.items():
            setattr(user, field, value)
            user = await add_user(user, self.session)
        return web.json_response(
            {
                "id": user.id,
            }
        )

    async def delete(self):
        user = await get_user(self.user_id, self.session)
        await self.session.delete(user)
        await self.session.commit()
        return web.json_response(
            {
                "status": "success",
            }
        )


app.add_routes(
    [
        web.post("/user", UserView),
        web.get("/user/{user_id:\d+}", UserView),
        web.patch("/user/{user_id:\d+}", UserView),
        web.delete("/user/{user_id:\d+}", UserView),
    ]
)


if __name__ == "__main__":
    web.run_app(app)
