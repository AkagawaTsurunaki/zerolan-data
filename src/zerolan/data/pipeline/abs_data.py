from uuid import uuid4

from pydantic import BaseModel


class AbstractModelQuery(BaseModel):
    id: str = str(uuid4())


class AbstractModelPrediction(BaseModel):
    id: str = str(uuid4())


class AbsractImageModelQuery(AbstractModelQuery):
    img_path: str | None = None
