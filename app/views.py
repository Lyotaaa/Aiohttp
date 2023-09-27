from aiohttp import web
from auxiliary_functions import hash_password, get_http_error, get_ads, get_user, add_user
from validate import (
    validate,
    CreateUser,
    UpdateUser,
    CreateAds,
    UpdateAds,
)
from config_db import Session
from models import User, Ads
import requests


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
        json_data = await self.request.json()
        json_validated = validate(json_data, CreateUser)
        user_password = json_validated.get("password")
        hashed_password = hash_password(user_password)
        json_validated["password"] = hashed_password
        new_user = User(**json_validated)
        user = await add_user(new_user, self.session)
        return web.json_response(
            {
                "id": user.id,
                "name": user.name,
                "password": user.password,
                "creation_time": user.creation_time.isoformat(),
            }
        )


    def patch(self, owner_id: int):
        pass

    def delete(self, owner_id: int):
        pass


class AdsView(web.View):
    @property
    def session(self):
        return self.request["session"]

    @property
    def ads_id(self):
        return int(self.request.match_info["ads_id"])

    def get(self):
        pass

    def post(self):
        pass

    def patch(self, ads_id: int):
        pass

    def delete(self, ads_id: int):
        pass
