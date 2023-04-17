from http import HTTPStatus
from quart import Blueprint, current_app, request
from quart_schema import validate_request, validate_response

users_blueprint = Blueprint("users", __name__, url_prefix="/api")


@users_blueprint.post(rule="/users")
async def register_user():
    pass


async def login():
    pass


async def get_current():
    pass


async def update():
    pass
