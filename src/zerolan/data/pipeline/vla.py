from typing import Literal

from pydantic import BaseModel

from zerolan.data.pipeline.abs_data import AbsractImageModelQuery, AbstractModelPrediction


class PhoneAction(BaseModel):
    env: str = "phone"
    action: Literal['INPUT', 'SWIPE', 'TAP', 'ANSWER', 'ENTER']
    value: str | None = None


class WebAction(BaseModel):
    env: str = "web"
    action: Literal['CLICK', 'INPUT', 'SELECT', 'HOVER',
    'ANSWER', 'ENTER', 'SCROLL', 'SELECT_TEXT', 'COPY']
    value: str | None = None


class ShowUiQuery(AbsractImageModelQuery):
    query: str
    action: PhoneAction | WebAction | None
    system_prompt: str | None = None


class ShowUiPrediction(AbstractModelPrediction):
    action: Literal['CLICK', 'INPUT', 'SELECT', 'HOVER',
    'ANSWER', 'ENTER', 'SCROLL', 'SELECT_TEXT', 'COPY']
    click_xy: list[float]
