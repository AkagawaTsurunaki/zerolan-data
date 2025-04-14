from pydantic import Field
from zerolan.data.pipeline.abs_data import AbstractModelQuery, AbstractModelPrediction


class ASRQuery(AbstractModelQuery):
    """
    Represents an Auto-Speech-Recognition (ASR) query.
    """
    audio_path: str = Field(default=None, description="Path to the audio file.")
    media_type: str = Field(default='wav', description="Format of audio data.")
    sample_rate: int = Field(default=16000, description="Sample rate of the audio.")
    channels: int = Field(default=1, description="Number of audio channels.")


class ASRStreamQuery(AbstractModelQuery):
    """
    Represents an Auto-Speech-Recognition (ASR) stream query.
    """
    is_final: bool = Field(default=False, description="Flag indicating if this is the final chunk of audio.")
    audio_data: bytes = Field(default=None, description="Raw audio data bytes.")
    media_type: str = Field(default='wav', description="Format of audio data.")
    sample_rate: int = Field(default=16000, description="Sample rate of the audio.")
    channels: int = Field(default=1, description="Number of audio channels.")


class ASRPrediction(AbstractModelPrediction):
    """
    Represents an Auto-Speech-Recognition (ASR) result.
    """
    transcript: str = Field(default=None, description="Transcribed text from the speech.")
