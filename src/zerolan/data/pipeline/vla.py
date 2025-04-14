from typing import Literal, List, Union

from pydantic import BaseModel, Field

from zerolan.data.pipeline.abs_data import AbsractImageModelQuery, AbstractModelPrediction


class PhoneAction(BaseModel):
    """
    Represents an action to be performed on a phone environment.
    """
    env: str = Field("phone", frozen=True, description="The environment where the action is performed.")
    action: Literal['INPUT', 'SWIPE', 'TAP', 'ANSWER', 'ENTER'] = Field(..., description="The type of action to be performed.")
    value: str | None = Field(None, description="The value associated with the action (optional).")
    position: List[float] | None = Field(None, description="The position coordinates for the action (optional).")


class WebAction(BaseModel):
    """
    Represents an action to be performed on a web environment.
    """
    env: str = Field("web", frozen=True, description="The environment where the action is performed.")
    action: Literal['CLICK', 'INPUT', 'SELECT', 'HOVER', 'ANSWER', 'ENTER', 'SCROLL', 'SELECT_TEXT', 'COPY'] = Field(..., description="The type of action to be performed.")
    value: str | None = Field(None, description="The value associated with the action (optional).")
    position: List[float] | None = Field(None, description="The position coordinates for the action (optional).")


class ShowUiQuery(AbsractImageModelQuery):
    """
    Represents a query for the Show UI model.
    """
    query: str = Field(..., description="The main query string.")
    env: Literal["web", "phone"] | None = Field(None, description="The environment for the query (optional).")
    system_prompt: str | None = Field(None, description="The system prompt for the query (optional; None for default system prompt).")
    history: List[Union[WebAction, PhoneAction]] = Field([], description="The history of actions performed.")


class ShowUiPrediction(AbstractModelPrediction):
    """
    Represents a prediction result from the Show UI model.
    """
    actions: List[Union[WebAction, PhoneAction]] = Field(..., description="The list of actions predicted by the model.")
