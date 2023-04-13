from dataclasses import dataclass
from typing import Optional
from uuid import UUID


@dataclass
class UserBase:
    id: UUID
    username: str
    email: str
    bio: Optional[str]
