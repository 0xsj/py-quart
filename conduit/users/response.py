from dataclasses import dataclass
from typing import Optional
from user import User


@dataclass
class UserResponse(User):
    token: str
