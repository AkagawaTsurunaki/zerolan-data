from typing import TypeVar

from pydantic import BaseModel

T = TypeVar('T')


class ZerolanProtocol(BaseModel):
    protocol: str = "ZerolanProtocol"
    version: str = "1.1"
    message: str
    action: str
    code: int
    data: T
