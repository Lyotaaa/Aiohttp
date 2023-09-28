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

        ###


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


if __name__ == "__main__":
    # asyncio.run(post_user("new_user", "qwerty"))
    # asyncio.run(get_user(1))
    # asyncio.run(patch_user(1, name=None, password=None)) #
    asyncio.run(delete_user(4))
