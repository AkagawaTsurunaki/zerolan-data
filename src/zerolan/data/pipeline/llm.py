from pydantic import BaseModel

from zerolan.data.pipeline.abs_data import AbstractModelQuery, AbstractModelPrediction


class RoleEnum(BaseModel):
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

    Attributes:
        role: Who made this conversation.
        content: The content of this conversation.
        metadata: The metadata of this conversation.
    """
    role: str
    content: str
    metadata: str | None = None


class LLMQuery(AbstractModelQuery):
    """
    Query for Large Language Models.

    Attributes:
        text: The content of the query.
        history: Previous conversations.
    """
    text: str
    history: list[Conversation]


class LLMPrediction(AbstractModelPrediction):
    """
    Prediction for Large Language Models.

    Attributes:
        response: The content of the result.
        history: Previous conversations.
    """
    response: str
    history: list[Conversation]
