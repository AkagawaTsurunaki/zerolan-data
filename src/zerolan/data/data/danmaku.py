from dataclasses import dataclass


@dataclass
class Danmaku:
    uid: str  # User id
    username: str # Who send this danmaku
    msg: str  # Message content
    ts: int  # Timestamp

    def __str__(self):
        return f'[{self.username}]({self.uid}): {self.msg}'