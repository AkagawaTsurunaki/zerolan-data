from zerolan.data.pipeline.abs_data import AbstractModelQuery, AbstractModelPrediction


class ASRQuery(AbstractModelQuery):
    """
    Represents an Auto-Speech-Recognition (ASR) query.

    Attributes:
        audio_path: Path to the audio file.
        media_type: Type of media (default: 'wav').
        sample_rate: Sample rate of the audio (default: 16000 Hz).
        channels: Number of audio channels (default: 1).
    """
    audio_path: str
    media_type: str = 'wav'
    sample_rate: int = 16000
    channels: int = 1


class ASRStreamQuery(AbstractModelQuery):
    """
    Represents an Auto-Speech-Recognition (ASR) stream query.

    Attributes:
        is_final (bool): Flag indicating if this is the final chunk of audio.
        audio_data (bytes): Raw audio data bytes.
        media_type (str): Type of media (default: 'wav').
        sample_rate (int): Sample rate of the audio (default: 16000 Hz).
        channels (int): Number of audio channels (default: 1).
    """
    is_final: bool
    audio_data: bytes
    media_type: str = 'wav'
    sample_rate: int = 16000
    channels: int = 1


class ASRPrediction(AbstractModelPrediction):
    """
    Represents an Auto-Speech-Recognition (ASR) result.

    Attributes:
        transcript: Transcribed text from the speech.
    """
    transcript: str
