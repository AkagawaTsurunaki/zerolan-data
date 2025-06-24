from pydantic import BaseModel, Field


class Danmaku(BaseModel):
    """
    Represents a danmaku entity from live-streaming.
    """
    uid: str = Field(...,
                     description="The unique identifier of the user who sent this danmaku (depending on the platform).")
    username: str = Field(..., description="The name or handle of the user who sent this danmaku.")
    content: str = Field(..., description="The content of the danmaku.")
    ts: int = Field(..., description="The timestamp of when the danmaku was sent.")


class SuperChat(Danmaku):
    """
    Represents a Super Chat message from live-streaming.
    """
    money: str = Field(..., description="The money sent by the user (depending on the platform).")


class Gift(BaseModel):
    uid: str = Field(description="Sender ID.")
    username: str = Field(description="Sender username.")
    gift_name: str = Field(description="Gift name.")
    num: int = Field(description="Number of gifts.")
