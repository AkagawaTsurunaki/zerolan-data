from dataclasses import dataclass

from dataclasses_json import dataclass_json

from zerolan.data.abs_data import AbstractModelQuery, AbstractModelPrediction


@dataclass_json
@dataclass
class VidCapQuery(AbstractModelQuery):
    vid_path: str


@dataclass_json
@dataclass
class VidCapPrediction(AbstractModelPrediction):
    caption: str
    lang: str
