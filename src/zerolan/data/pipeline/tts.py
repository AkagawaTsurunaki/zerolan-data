from typing import Optional

from zerolan.data.pipeline.abs_data import AbstractModelQuery, AbstractModelPrediction


class TTSQuery(AbstractModelQuery):
    """
    Represents a Text-to-Speech (TTS) query.

    Attributes:
        text: The text to be converted to speech.
        text_language: The language of the input text.
        refer_wav_path: Path to the reference WAV file.
        prompt_text: Text for the reference WAV file.
        prompt_language: The language of the prompt text.
        cut_punc: Use to split the sentences.
    """
    text: str
    text_language: str
    refer_wav_path: str
    prompt_text: str
    prompt_language: str
    cut_punc: Optional[str] = "，。"


class TTSPrediction(AbstractModelPrediction):
    """
    Represents a Text-to-Speech (TTS) result.

    Attributes:
        wave_data: The raw audio data produced by the TTS model.
    """
    wave_data: bytes
    audio_type: str
