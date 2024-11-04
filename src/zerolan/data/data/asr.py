from dataclasses import dataclass

from dataclasses_json import dataclass_json

from zerolan.data.abs_data import AbstractModelQuery, AbstractModelPrediction


@dataclass_json
@dataclass
class ASRModelQuery(AbstractModelQuery):
    audio_path: str
    media_type: str = 'wav'
    sample_rate: int = 16000
    channels: int = 1


@dataclass_json
@dataclass
class ASRModelStreamQuery(AbstractModelQuery):
    is_final: bool
    audio_data: bytes
    media_type: str = 'wav'
    sample_rate: int = 16000
    channels: int = 1


@dataclass_json
@dataclass
class ASRModelPrediction(AbstractModelPrediction):
    transcript: str

    def __str__(self):
        return self.transcript