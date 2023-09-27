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

if __name__ == "__main__":
    asyncio.run(post_user("35", "1234"))
    # asyncio.run(get_user(1))