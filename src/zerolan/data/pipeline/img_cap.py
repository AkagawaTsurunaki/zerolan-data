from pydantic import Field
from zerolan.data.pipeline.abs_data import AbsractImageModelQuery, AbstractModelPrediction


class ImgCapQuery(AbsractImageModelQuery):
    """
    Query for image captioning model.
    """
    prompt: str = Field(default="There", description="The prompt for generating the image caption.")


class ImgCapPrediction(AbstractModelPrediction):
    """
    Prediction for image captioning model.
    """
    caption: str = Field(default=None, description="The image caption result.")
    lang: str = Field(default='en', description="The language of the image caption (depending on your model).")
