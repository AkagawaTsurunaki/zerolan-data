from enum import Enum

from pydantic import BaseModel, Field
from zerolan.data.pipeline.abs_data import AbstractModelQuery, AbstractModelPrediction


class RoleEnum(str, Enum):
    """
    The role that made this conversation.
    """
    system = "system"
    user = "user"
    assistant = "assistant"
    function = "function"


class Conversation(BaseModel):
    """
    Message containing information about a conversation.
    Like Langchain Message.
    """
    role: str = Field(default=RoleEnum.user, description="The role of this conversation. See `RoleEnum`.")
    content: str = Field(default=None, description="The content of this conversation.")
    metadata: str | None = Field(default=None, description="The metadata of this conversation.")


class LLMQuery(AbstractModelQuery):
    """
    Query for Large Language Models.
    """
    text: str = Field(default=None, description="The content of the query.")
    history: list[Conversation] = Field(default_factory=list, description="The history of previous conversations.")


class LLMPrediction(AbstractModelPrediction):
    """
    Prediction for Large Language Models.
    """
    response: str = Field(default=None, description="The content of the result.")
    history: list[Conversation] = Field(default_factory=list, description="The history of previous conversations. The current response included.")
