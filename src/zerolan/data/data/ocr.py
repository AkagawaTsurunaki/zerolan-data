from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from zerolan.data.abs_data import AbsractImageModelQuery, AbstractModelPrediction


@dataclass_json
@dataclass
class OCRQuery(AbsractImageModelQuery):
    pass


@dataclass_json
@dataclass
class Vector2D:
    x: float
    y: float


@dataclass_json
@dataclass
class Position:
    lu: Vector2D  # Left up
    ru: Vector2D  # Right up
    rd: Vector2D  # Right down
    ld: Vector2D  # Left down


@dataclass_json
@dataclass
class RegionResult:
    position: Position
    content: str
    confidence: float


@dataclass_json
@dataclass
class OCRPrediction(AbstractModelPrediction):
    region_results: List[RegionResult]

    def unfold_as_str(self) -> str:
        result = ""
        for region_result in self.region_results:
            result += region_result.content + "\n"
        return result
