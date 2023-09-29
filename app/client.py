import asyncio
import aiohttp
from pprint import pprint


async def post_user(name: str, password: str):
    async with aiohttp.ClientSession() as session:
        response = await session.post(
            "http://127.0.0.1:8080/users/",
            json={
                "name": name,
                "password": password,
            },
        )
        json_data = await response.json()
        print(response.status)
        pprint(json_data)


async def get_user(id):
    async with aiohttp.ClientSession() as session:
        response = await session.get(
            f"http://127.0.0.1:8080/users/{id}",
        )
        json_data = await response.json()
        print(response.status)
        pprint(json_data)


async def patch_user(id, name=None, password=None):
    async with aiohttp.ClientSession() as session:
        if name is not None and password is None:
            response = await session.patch(
                f"http://127.0.0.1:8080/users/{id}",
                json={"name": name},
            )
        elif name is None and password is not None:
            response = await session.patch(
                f"http://127.0.0.1:8080/users/{id}",
                json={"password": password},
            )
        else:
            response = await session.patch(
                f"http://127.0.0.1:8080/users/{id}",
                json={
                    "name": name,
                    "password": password,
                },
            )
        json_data = await response.json()
        print(response.status)
        pprint(json_data)


async def delete_user(id):
    async with aiohttp.ClientSession() as session:
        response = await session.delete(
            f"http://127.0.0.1:8080/users/{id}",
        )
        json_data = await response.json()
        print(response.status)
        pprint(json_data)


async def post_ads(title: str, description: str, user_id: str):
    async with aiohttp.ClientSession() as session:
        response = await session.post(
            "http://127.0.0.1:8080/ads/",
            json={
                "title": title,
                "description": description,
                "user_id": user_id,
            },
        )
        json_data = await response.json()
        print(response.status)
        pprint(json_data)


async def get_ads(id: int):
    async with aiohttp.ClientSession() as session:
        response = await session.get(
            f"http://127.0.0.1:8080/ads/{id}",
        )
        json_data = await response.json()
        print(response.status)
        pprint(json_data)


async def patch_ads(ads_id, user_id, title=None, description=None):
    async with aiohttp.ClientSession() as session:
        if title is not None and description is None:
            response = await session.patch(
                f"http://127.0.0.1:8080/ads/{ads_id}",
                json={
                    "title": title,
                    "user_id": user_id,
                },
            )
        elif title is None and description is not None:
            response = await session.patch(
                f"http://127.0.0.1:8080/ads/{ads_id}",
                json={
                    "description": description,
                    "user_id": user_id,
                },
            )
        else:
            response = await session.patch(
                f"http://127.0.0.1:8080/ads/{ads_id}",
                json={
                    "title": title,
                    "description": description,
                    "user_id": user_id,
                },
            )
        json_data = await response.json()
        print(response.status)
        pprint(json_data)


async def delete_ads(ads_id):
    async with aiohttp.ClientSession() as session:
        response = await session.delete(
            f"http://127.0.0.1:8080/ads/{ads_id}",
        )
        json_data = await response.json()
        print(response.status)
        pprint(json_data)


if __name__ == "__main__":
    """Проверка пользователя"""
    asyncio.run(post_user("User", "qwerty"))
    asyncio.run(get_user(1))
    asyncio.run(patch_user(1, name="New user", password="12345"))  #
    asyncio.run(delete_user(1))
    """Проверка объявления"""
    # asyncio.run(post_user("User", "qwerty"))
    # asyncio.run(post_ads("Title", "description", "1"))
    # asyncio.run(get_ads(1))
    # asyncio.run(patch_ads(ads_id=1, user_id=1, title="New_Title", description="New_Description"))
    # asyncio.run(delete_ads(1))
    # asyncio.run(delete_user(1))
