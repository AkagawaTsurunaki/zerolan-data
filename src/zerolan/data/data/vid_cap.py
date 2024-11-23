from zerolan.data.abs_data import AbstractModelQuery, AbstractModelPrediction


class VidCapQuery(AbstractModelQuery):
    """
    Query for video captioning model.

    Attributes:
        vid_path: Path to the video file.
    """
    vid_path: str


class VidCapPrediction(AbstractModelPrediction):
    """
    Prediction result for video captioning model.

    Attributes:
        caption: The generated caption for the video.
        lang: The language of the generated caption (depending on your model).
    """
    caption: str
    lang: str
