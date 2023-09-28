from aiohttp import web
from auxiliary_functions import hash_password, get_ads, get_user, add_user, add_ads
from validate import (
    validate,
    CreateUser,
    UpdateUser,
    CreateAds,
    UpdateAds,
)
from models import User, Ads


class UserView(web.View):
    @property
    def session(self):
        return self.request["session"]

    @property
    def user_id(self):
        return int(self.request.match_info["user_id"])

    async def post(self):
        json_data = await self.request.json()
        json_validated = validate(json_data, CreateUser)
        json_validated["password"] = hash_password(json_validated.get("password"))
        new_user = User(**json_validated)
        user = await add_user(new_user, self.session)
        print(user)
        return web.json_response(
            {
                "id": user.id,
                "name": user.name,
                "password": user.password,
                "creation_time": user.creation_time.isoformat(),
            }
        )

    async def get(self):
        user = await get_user(self.user_id, self.session)
        return web.json_response(
            {
                "id": user.id,
                "name": user.name,
                "creation_time": user.creation_time.isoformat(),
            }
        )

    async def patch(self):
        json_data = await self.request.json()
        json_validated = validate(json_data, UpdateUser)
        if "password" in json_validated:
            json_validated["password"] = hash_password(json_validated.get("password"))
        update_user = await get_user(self.user_id, self.session)
        for field, value in json_validated.items():
            setattr(update_user, field, value)
        user = await add_user(update_user, self.session)
        return web.json_response(
            {
                "id": user.id,
                "name": user.name,
                "password": user.password,
                "creation_time": user.creation_time.isoformat(),
            }
        )

    async def delete(self):
        user = await get_user(self.user_id, self.session)
        await self.session.delete(user)
        await self.session.commit()
        return web.json_response(
            {
                "Status": "Successfully",
            }
        )


class AdsView(web.View):
    @property
    def session(self):
        return self.request["session"]

    @property
    def ads_id(self):
        return int(self.request.match_info["ads_id"])

    async def post(self):
        json_data = await self.request.json()
        json_validated = validate(json_data, CreateAds)
        new_ads = Ads(**json_validated)
        ads = await add_ads(new_ads, self.session)
        return web.json_response(
            {
                "id": ads.id,
                "user_id": ads.user_id,
                "title": ads.title,
                "description": ads.description,
                "creation_time": ads.creation_time.isoformat(),
            }
        )

    async def get(self):
        ads = await get_ads(self.ads_id, self.session)
        return web.json_response(
            {
                "id": ads.id,
                "user_id": ads.user_id,
                "title": ads.title,
                "description": ads.description,
                "creation_time": ads.creation_time.isoformat(),
            }
        )

    async def patch(self):
        json_data = await self.request.json()
        json_validated = validate(json_data, UpdateAds)
        update_ads = await get_ads(self.ads_id, self.session)
        for field, value in json_validated.items():
            setattr(update_ads, field, value)
        ads = await add_ads(update_ads, self.session)
        return web.json_response(
            {
                "id": ads.id,
                "user_id": ads.user_id,
                "title": ads.title,
                "description": ads.description,
                "creation_time": ads.creation_time.isoformat(),
            }
        )

    async def delete(self):
        ads = await get_ads(self.ads_id, self.session)
        await self.session.delete(ads)
        await self.session.commit()
        return web.json_response(
            {
                "Status": "Successfully",
            }
        )
