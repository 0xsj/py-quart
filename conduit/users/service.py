import psycopg2
from typing import Optional
from .user import User


class UserService:
    def __init__(self, conn: psycopg2.AsyncConnection):
        self._conn = conn
        self.users_table = "users"

    async def create_user(self, user: User) -> Optional[int]:
        """"create a new user under the db"""
        pass

    async def get_user(self, user: User) -> Optional[int]:
        """"create a new user under the db"""
        pass

    async def update_user(self, user: User) -> Optional[int]:
        """"create a new user under the db"""
        pass

    async def delete_user(self, user: User) -> Optional[int]:
        """"create a new user under the db"""
        pass

    async def search_user(self, user: User) -> Optional[int]:
        """"create a new user under the db"""
        pass

    async def get_all_user(self, user: User) -> Optional[int]:
        """"create a new user under the db"""
        pass
