from dataclasses import dataclass
from enum import Enum

from dataclasses_json import dataclass_json

class AppStatusEnum(Enum):
    RUNNING = "running"
    STOPPED = "stopped"
    INITIALIZING = "initializing"
    UNKNOWN = "unknown"


@dataclass_json
@dataclass
class ServiceState:
    state: AppStatusEnum
    msg: str


@dataclass
class AppStatus:
    status: str