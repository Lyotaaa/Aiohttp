from aiohttp import web


if __name__ == "__main__":
    app = web.Application()
    web.run_app(app)