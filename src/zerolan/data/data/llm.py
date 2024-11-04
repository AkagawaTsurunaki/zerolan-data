from dataclasses import dataclass
from enum import Enum
from dataclasses_json import dataclass_json

from zerolan.data.abs_data import AbstractModelQuery, AbstractModelPrediction


class RoleEnum(Enum):
    system = "system"
    user = "user"
    assistant = "assistant"


@dataclass_json
@dataclass
class Conversation:
    role: RoleEnum
    content: str
    metadata: str | None = None


@dataclass_json
@dataclass
class LLMQuery(AbstractModelQuery):
    text: str
    history: list[Conversation]


@dataclass_json
@dataclass
class LLMPrediction(AbstractModelPrediction):
    response: str
    history: list[Conversation]