import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        # response = await session.post(
        #     "http://127.0.0.1:8080/user",
        #     json={"name": "user_2", "password": "1234"},
        # )
        # json_data = await response.json()
        # print(response.status)
        # print(json_data)

        # response = await session.get(
        #     "http://127.0.0.1:8080/user/3",
        # )
        # json_data = await response.json()
        # print(response.status)
        # print(json_data)

        # response = await session.patch(
        #     "http://127.0.0.1:8080/user/3",
        #     json={"name": "user_new_name"},
        # )
        # json_data = await response.json()
        # print(response.status)
        # print(json_data)
        #
        # response = await session.get(
        #     "http://127.0.0.1:8080/user/3",
        # )
        # json_data = await response.json()
        # print(response.status)
        # print(json_data)

        response = await session.delete(
            "http://127.0.0.1:8080/user/3",
        )
        json_data = await response.json()
        print(response.status)
        print(json_data)

        response = await session.get(
            "http://127.0.0.1:8080/user/3",
        )
        json_data = await response.json()
        print(response.status)
        print(json_data)


if __name__ == "__main__":
    asyncio.run(main())
