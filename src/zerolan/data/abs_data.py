from dataclasses import dataclass

from dataclasses_json import dataclass_json
from pydantic import BaseModel


class AbstractModelQuery(BaseModel):
    id: str


class AbstractModelPrediction(BaseModel):
    id: str


@dataclass_json
@dataclass
class AbsractImageModelQuery(AbstractModelQuery):
    img_path: str | None = None
