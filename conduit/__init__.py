import psycopg2
from quart import Quart, Blueprint
from quart_schema import QuartSchema

app = Quart(__name__)