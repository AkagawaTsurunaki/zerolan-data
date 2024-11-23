from typing import List

from pydantic import BaseModel
from zerolan.data.abs_data import AbsractImageModelQuery, AbstractModelPrediction


class OCRQuery(AbsractImageModelQuery):
    """
    Query for Optical Character Recognition (OCR) model.

    This class inherits from AbsractImageModelQuery and doesn't have any specific attributes defined.
    """
    pass


class Vector2D(BaseModel):
    """
    Represents a two-dimensional vector.

    Attributes:
        x: The x-coordinate of the vector.
        y: The y-coordinate of the vector.
    """
    x: float
    y: float


class Position(BaseModel):
    """
    Represents the position of a region in an image.

    Attributes:
        lu: Left-up corner coordinates.
        ru: Right-up corner coordinates.
        rd: Right-down corner coordinates.
        ld: Left-down corner coordinates.
    """
    lu: Vector2D
    ru: Vector2D
    rd: Vector2D
    ld: Vector2D


class RegionResult(BaseModel):
    """
    Represents the result for a specific region in OCR.

    Attributes:
        position: The position of the detected region.
        content: The transcribed text from the detected region.
        confidence: The confidence level of the transcription.
    """
    position: Position
    content: str
    confidence: float


class OCRPrediction(AbstractModelPrediction):
    """
    Prediction result for Optical Character Recognition model.

    Attributes:
        region_results: List of results for different regions.
    """
    region_results: List[RegionResult]
