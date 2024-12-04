from typing import Literal, List

from pydantic import BaseModel

from zerolan.data.pipeline.abs_data import AbsractImageModelQuery, AbstractModelPrediction


class PhoneAction(BaseModel):
    env: str = "phone"
    action: Literal['INPUT', 'SWIPE', 'TAP', 'ANSWER', 'ENTER']
    value: str | None = None
    position: list[float] | None = None


class WebAction(BaseModel):
    env: str = "web"
    action: Literal['CLICK', 'INPUT', 'SELECT', 'HOVER',
    'ANSWER', 'ENTER', 'SCROLL', 'SELECT_TEXT', 'COPY']
    value: str | None = None
    position: list[float] | None = None


class ShowUiQuery(AbsractImageModelQuery):
    query: str
    action: PhoneAction | WebAction | None = None
    system_prompt: str | None = None


class ShowUiPrediction(AbstractModelPrediction):
    actions: List[WebAction | PhoneAction]
