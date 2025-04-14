from pydantic import Field
from zerolan.data.pipeline.abs_data import AbstractModelQuery, AbstractModelPrediction


class VidCapQuery(AbstractModelQuery):
    """
    Query for video captioning model.
    """
    vid_path: str = Field(..., description="Path to the video file.")


class VidCapPrediction(AbstractModelPrediction):
    """
    Prediction result for video captioning model.
    """
    caption: str = Field(..., description="The generated caption for the video.")
    lang: str = Field(default="en", description="The language of the generated caption (depending on your model).")
