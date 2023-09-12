from aiohttp import web
from .route import routes

async def web_server():
  web_app = web.Application(client_max)
  web_app.add_route(routes)
  return web_app
