from pydantic import BaseModel


class TTSPrompt(BaseModel):
    """
    Represents a Text-to-Speech (TTS) prompt.

    Attributes:
        audio_path: Path to the audio file.
        lang: Language enum value for the TTS output.
        sentiment: Sentiment tag of the input text.
        prompt_text: The text to be converted to speech.
    """
    audio_path: str
    lang: str  # Use enumerator.Language
    sentiment: str
    prompt_text: str
