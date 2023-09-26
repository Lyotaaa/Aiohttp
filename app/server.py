from aiohttp import web
from app.auxiliary_functions import context_orm, session_middleware
from app.views import UserView, AdsView

if __name__ == "__main__":
    app = web.Application()
    app.cleanup_ctx.append(context_orm)
    app.middlewares.append(session_middleware)
    app.add_routes(
        [
            web.get("/users/{user_id:\d+}", UserView),
            web.post("/users/", UserView),
            web.patch("/users/{user_id:\d+}", UserView),
            web.delete("/users/{user_id:\d+}", UserView),
            web.get("/ads/{ads_id:\d+}", AdsView),
            web.post("/ads/", AdsView),
            web.patch("/ads/{ads_id:\d+}", AdsView),
            web.delete("/ads/{ads_id:\d+}", AdsView),
        ]
    )
    web.run_app(app)
