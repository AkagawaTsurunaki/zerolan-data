from enum import Enum

from pydantic import BaseModel


class AppStatusEnum(str, Enum):
    RUNNING = "running"
    STOPPED = "stopped"
    INITIALIZING = "initializing"
    UNKNOWN = "unknown"


class ServiceState(BaseModel):
    state: str
    msg: str


class AppStatus(BaseModel):
    status: str
