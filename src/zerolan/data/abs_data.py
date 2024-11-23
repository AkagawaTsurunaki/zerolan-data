from dataclasses import dataclass
from uuid import uuid4

from dataclasses_json import dataclass_json
from pydantic import BaseModel


class AbstractModelQuery(BaseModel):
    id: str = str(uuid4())


class AbstractModelPrediction(BaseModel):
    id: str = str(uuid4())


@dataclass_json
@dataclass
class AbsractImageModelQuery(AbstractModelQuery):
    img_path: str | None = None
