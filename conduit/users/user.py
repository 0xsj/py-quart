from dataclasses import dataclass
from typing import Optional
from uuid import UUID


@dataclass
class User:
    id: str
    username: str
    email: str
