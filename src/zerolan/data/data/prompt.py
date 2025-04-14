from pydantic import BaseModel, Field


class TTSPrompt(BaseModel):
    """
    Represents a Text-to-Speech (TTS) prompt.
    """
    audio_path: str = Field(..., description="Path to the audio file.")
    lang: str = Field(..., description="Language enum value for the TTS output. Use enumerator `Language`.")
    sentiment: str = Field(..., description="Sentiment tag of the input text.")
    prompt_text: str = Field(..., description="Text to be converted to speech.")
