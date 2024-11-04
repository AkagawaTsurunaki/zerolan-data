from dataclasses import dataclass

from dataclasses_json import dataclass_json

from zerolan.data.abs_data import AbstractModelQuery, AbstractModelPrediction


@dataclass_json
@dataclass
class TTSQuery(AbstractModelQuery):
    text: str
    text_language: str
    refer_wav_path: str
    prompt_text: str
    prompt_language: str


@dataclass_json
@dataclass
class TTSPrediction(AbstractModelPrediction):
    wave_data: bytes
