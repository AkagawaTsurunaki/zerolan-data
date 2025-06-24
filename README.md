# ZerolanData

![Static Badge](https://img.shields.io/badge/Python-3.1x-blue) ![Static Badge](https://img.shields.io/badge/License-MIT-orange) ![Static Badge](https://img.shields.io/badge/ver-1.5.0-green)

Define data classes used in [**ZerolanLiveRobot**](https://github.com/AkagawaTsurunaki/ZerolanLiveRobot) and [*
*ZerolanCore**](https://github.com/AkagawaTsurunaki/zerolan-core).

All data classes inherits `pydantic.BaseModel` with strict schema validation.

See documentation [here](docs/doc_en.md).
The documentation is automatically generated and is consistent with the comments and annotations in the code.

The project structure is as follows:

```
docs
└─ doc_en.md                # Documentation for zerolan-data.
src
└─ zerolan
   └─ data
      ├─ __init__.py
      ├─ protocol
      │  ├─ protocol.py     # JSON+WebSocket message object
      │  ├─ __init__.py
      ├─ pipeline
      │  ├─ abs_data.py     # Abstract pipeline query and prediction
      │  ├─ asr.py          # Automatic speech recognition
      │  ├─ img_cap.py      # Image capitioning
      │  ├─ llm.py          # Large language model
      │  ├─ milvus.py       # Vector database (Milvus)
      │  ├─ ocr.py          # Optical character recognition
      │  ├─ tts.py          # Text to speech
      │  ├─ vid_cap.py      # Video capitioning
      │  ├─ vla.py          # Vision language action model
      │  └─ __init__.py
      └─ data
         ├─ danmaku.py      # Live-streaming data for Bilibili, YouTube and Twitch
         ├─ prompt.py       # TTS prompt
         ├─ state.py        # Service state
         └─ __init__.py
```

**How to generate documentation?**

Run the following commands:

```shell
cd src/zerolan/data/generator
python doc_gen.py
```
