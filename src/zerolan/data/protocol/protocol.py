from typing import TypeVar

from pydantic import BaseModel, Field

T = TypeVar('T')


class ZerolanProtocol(BaseModel):
    """
    Represents a message following the Zerolan protocol.
    """
    protocol: str = Field("ZerolanProtocol", description="The name of the protocol.")
    version: str = Field("1.1", description="The version of the protocol.")
    message: str = Field(..., description="A descriptive message.")
    action: str = Field(..., description="The action associated with the message.")
    code: int = Field(..., description="A status code.")
    data: T = Field(..., description="The data payload, which can be of any type.")
