from pydantic import BaseModel


class Danmaku(BaseModel):
    """
    Represents a danmaku entity from live-streaming.

    Attributes:
        uid: The unique identifier of the user who sent this danmaku (depending on the platform).
        username: The name or handle of the user who sent this danmaku.
        content: The content message of the danmaku.
        ts: The timestamp of when the danmaku was sent.
    """
    uid: str
    username: str
    content: str
    ts: int


class SuperChat(Danmaku):
    """
    Represents a Super Chat message from live-streaming.

    Attributes:
        money: The money sent by the user (depending on the platform).
    """
    money: str
