from typing import Type


class AlreadyExists(Exception):
    def __init__(self, message: str = "Already Exists "):
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.message}"

    @property
    def error_type(self) -> Type[Exception]:
        return self.__class__
