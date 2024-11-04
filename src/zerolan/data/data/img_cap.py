from dataclasses import dataclass
from typing import Literal

from dataclasses_json import dataclass_json

from zerolan.data.abs_data import AbsractImageModelQuery, AbstractModelPrediction


@dataclass_json
@dataclass
class ImgCapQuery(AbsractImageModelQuery):
    prompt: str = "There"


@dataclass_json
@dataclass
class ImgCapPrediction(AbstractModelPrediction):
    caption: str
    lang: Literal["zh", "en", "ja"]