from dataclasses import dataclass
from typing import Optional
from user import UserBase


@dataclass
class UserResponse(UserBase):
    token: str
