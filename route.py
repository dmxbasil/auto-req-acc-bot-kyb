from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=true)
async def root_route_handler(request):
    return web.json_response("dmx_chating") 
