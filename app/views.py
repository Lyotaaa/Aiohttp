from flask import jsonify, request
from flask.views import MethodView
from errors import HttpError
from validate import (
    validate,
    hash_password,
    CreateOwner,
    UpdateOwner,
    CreateAds,
    UpdateAds,
)
from models import Session, OwnerModel, AdsModel
from sqlalchemy.exc import IntegrityError


def get_owner(session, owner_id):
    owner = session.get(OwnerModel, owner_id)
    if owner is None:
        raise HttpError(404, "User not found")
    return owner


def get_ads(session, ads_id):
    ads = session.get(AdsModel, ads_id)
    if ads is None:
        raise HttpError(404, "Ad no")
    return ads


class OwnerView(MethodView):
    def get(self, owner_id: int):
        with Session() as session:
            owner = get_owner(session, owner_id)
            return jsonify(
                {
                    "id": owner.id,
                    "email": owner.email,
                    "create_time": owner.creation_time,
                }
            )

    def post(self):
        owner_data = validate(request.json, CreateOwner)
        owner_data["password"] = hash_password(owner_data["password"])
        with Session() as session:
            owner = OwnerModel(**owner_data)
            session.add(owner)
            try:
                session.commit()
            except IntegrityError:
                raise HttpError(409, "There is already such a user")
            return jsonify(
                {
                    "id": owner.id,
                    "email": owner.email,
                    "create_time": owner.creation_time,
                }
            )

    def patch(self, owner_id: int):
        owner_data = validate(request.json, UpdateOwner)
        owner_data["password"] = hash_password(owner_data["password"])
        with Session() as session:
            new_owner = get_owner(session, owner_id)
            for field, value in owner_data.items():
                setattr(new_owner, field, value)
            session.add(new_owner)
            try:
                session.commit()
            except IntegrityError:
                raise HttpError(409, "Such a user already exists")
            return jsonify(
                {
                    "id": new_owner.id,
                    "email": new_owner.email,
                    "create_time": new_owner.creation_time,
                }
            )

    def delete(self, owner_id: int):
        with Session() as session:
            owner = get_owner(session, owner_id)
            session.delete(owner)
            session.commit()
            return jsonify({"status": "Successfully!"})


class AdsView(MethodView):
    def get(self, ads_id: int):
        with Session() as session:
            ads = get_ads(session, ads_id)
            return jsonify(
                {
                    "id": ads.id,
                    "title": ads.title,
                    "description": ads.description,
                    # "time": ads.creation_time,
                    "owner": ads.owner_id,
                }
            )

    def post(self):
        ads_data = validate(request.json, CreateAds)
        with Session() as session:
            ads = AdsModel(**ads_data)
            session.add(ads)
            session.commit()
            return jsonify(
                {
                    "id": ads.id,
                    "title": ads.title,
                    "description": ads.description,
                    # "create_time": ads.creation_time,
                    "owner": ads.owner_id,
                }
            )

    def patch(self, ads_id: int):
        ads_data = validate(request.json, UpdateAds)
        with Session() as session:
            new_ads = get_ads(session, ads_id)
            for field, value in ads_data.items():
                setattr(new_ads, field, value)
            session.add(new_ads)
            session.commit()
            return jsonify(
                {
                    "id": new_ads.id,
                    "title": new_ads.title,
                    "description": new_ads.description,
                    # "create_time": new_ads.creation_time,
                    "owner": new_ads.owner_id,
                }
            )

    def delete(self, ads_id: int):
        with Session() as session:
            ads = get_ads(session, ads_id)
            session.delete(ads)
            session.commit()
            return jsonify({"status": "Successfully!"})
