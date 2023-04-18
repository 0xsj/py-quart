import dataclasses
import json
import traceback
from dataclasses import dataclass
from http import HTTPStatus
from typing import List
from quart import Quart, Response
from utils import not_found, already_exists


@dataclass
class _ErrorResponseBody:
    body: List[str]


@dataclass
class _ErrorResponse:
    error: _ErrorResponseBody
