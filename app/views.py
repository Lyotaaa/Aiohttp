from aiohttp import web
from auxiliary_functions import hash_password, get_http_error, get_ads, get_user
from validate import (
    validate,
    CreateOwner,
    UpdateOwner,
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
    def owner_id(self):
        return int(self.request.match_info["owner_id"])

    def get(self):
        pass

    def post(self):
        pass

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
