from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class AbstractModelQuery:
    ...


@dataclass_json
@dataclass
class AbstractModelPrediction:
    ...


@dataclass_json
@dataclass
class AbsractImageModelQuery(AbstractModelQuery):
    img_path: str | None = None
