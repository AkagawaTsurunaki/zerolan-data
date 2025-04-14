from typing import List

from pydantic import BaseModel, Field
from zerolan.data.pipeline.abs_data import AbsractImageModelQuery, AbstractModelPrediction


class OCRQuery(AbsractImageModelQuery):
    """
    Query for Optical Character Recognition (OCR) model.

    This class inherits from AbsractImageModelQuery and doesn't have any specific attributes defined.
    """
    pass


class Vector2D(BaseModel):
    """
    Represents a two-dimensional vector.
    """
    x: float = Field(..., description="The x-coordinate of the vector.")
    y: float = Field(..., description="The y-coordinate of the vector.")


class Position(BaseModel):
    """
    Represents the position of a region in an image.
    """
    lu: Vector2D = Field(..., description="Left-up corner coordinates.")
    ru: Vector2D = Field(..., description="Right-up corner coordinates.")
    rd: Vector2D = Field(..., description="Right-down corner coordinates.")
    ld: Vector2D = Field(..., description="Left-down corner coordinates.")


class RegionResult(BaseModel):
    """
    Represents the result for a specific region in OCR.
    """
    position: Position = Field(..., description="The position of the detected region.")
    content: str = Field(..., description="The transcribed text from the detected region.")
    confidence: float = Field(..., description="The confidence level of the transcription.")


class OCRPrediction(AbstractModelPrediction):
    """
    Prediction result for Optical Character Recognition model.
    """
    region_results: List[RegionResult] = Field(..., description="List of results for different regions.")
