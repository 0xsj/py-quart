from quart import Quart, Blueprint, render_template, websocket
from quart_schema import QuartSchema
from .users import UserService, users_blueprint
from .config import config
import psycopg

app = Quart(__name__)

QuartSchema(
    app=app
)

app.config.from_object(config)


@app.route("/")
async def hello():
    return await render_template("test.html")


@app.route("/api")
async def json():
    return {"foo": "baz"}


@app.websocket("/ws")
async def ws():
    while True:
        await websocket.send("Foo")
        await websocket.send({"fooz": "baz"})


@app.before_serving
async def startup():
    print("startup func")
    app.aconn = await psycopg.AsyncConnection.connect(app.config["DB_URL"])
    user_service = UserService(conn=app.conn)

    app.user_service = user_service

    app.register_blueprint(blueprint=users_blueprint)


@app.after_serving
async def shutdown():
    print("shutting down...")
