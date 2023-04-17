from dataclasses import dataclass
from typing import Optional


@dataclass
class RegisterUser:
    username: str
    email: str
    password: str


@dataclass
class UpdateUser:
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
