from uuid import uuid4

from pydantic import BaseModel, Field


class AbstractModelQuery(BaseModel):
    """
    Abstract base class representing a model query request.

    This class provides a basic structure for creating model query requests. It includes a unique identifier for the query, which is automatically generated using UUID.

    [!Note]
        The `id` field is automatically generated if not explicitly provided. This ensures that each query has a unique identifier.
    """
    id: str = Field(default=str(uuid4()), description="Unique ID of the query for a model request.")


class AbstractModelPrediction(BaseModel):
    """
    Abstract base class representing a model prediction response.

    This class provides a basic structure for creating model prediction responses. It includes a unique identifier for the prediction, which is automatically generated using UUID.

    [!Note]
        The `id` field is automatically generated if not explicitly provided. This ensures that each query has a unique identifier.
    """
    id: str = Field(default=str(uuid4()), description="Unique ID of the prediction for a model response.")


class AbsractImageModelQuery(AbstractModelQuery):
    """
    Abstract class representing an image model query request.

    This class extends the `AbstractModelQuery` class and adds an `img_path` attribute to specify the image path. The image path can be a local file path or a remote file path.
    """
    img_path: str | None = Field(default=None, description="Image path. \n"
                                                           "[!Note]\n"
                                                           "1. If `image_path` exists in your local machine, will automatically read as binary stream.\n"
                                                           "2. If `image_path` dose not exist in your local machine, then we assume that it must exists in your remote machine (server, etc.)\n")
