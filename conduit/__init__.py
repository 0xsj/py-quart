# import psycopg2
# from quart import Quart, Blueprint
# from quart_schema import QuartSchema

# app = Quart(__name__)

async def app(scope, receive, send):
    if scope["type"] != "http":
        raise Exception("Only the HTTP protocol is supported")

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            (b'content-type', b'text/plain'),
            (b'content-length', b'5'),
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'hello',
    })
