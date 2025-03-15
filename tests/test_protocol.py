from pydantic import BaseModel

from src.zerolan.data.protocol.protocol import ZerolanProtocol


class _A(BaseModel):
    name: str = "A"


def test_protocol():
    z = ZerolanProtocol(message="5445", action="assa", code=545, data={"name": "AkagawaTsurunaki", "msg": "Ciallo!"})
    print(z)
    print(z.model_dump_json())
    z = ZerolanProtocol(message="5445", action="assa", code=545, data=[{"id": 1, "name": "A"}, {"id": 2, "name": "B"}])
    print(z)
    print(z.model_dump_json())
    z = ZerolanProtocol(message="5445", action="assa", code=545, data=[_A(name="LL"), {"id": 2, "name": "B"}])
    print(z)
    print(z.model_dump_json())
