from zerolan.data.pipeline.abs_data import AbsractImageModelQuery, AbstractModelPrediction


class ImgCapQuery(AbsractImageModelQuery):
    """
    Query for image captioning model.

    Attributes:
        prompt: The prompt for generating the image caption. Default is "There".
    """
    prompt: str = "There"


class ImgCapPrediction(AbstractModelPrediction):
    """
    Prediction for image captioning model.

    Attributes:
        caption: The image caption result.
        lang: The language of the image caption (depending on your model).
    """
    caption: str
    lang: str
