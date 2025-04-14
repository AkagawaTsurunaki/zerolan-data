from enum import Enum

from pydantic import BaseModel, Field


class AppStatusEnum(str, Enum):
    """
    Enum representing the possible statuses of an application.
    """
    RUNNING = "running"
    STOPPED = "stopped"
    INITIALIZING = "initializing"
    UNKNOWN = "unknown"


class ServiceState(BaseModel):
    """
    Represents the state of a service.
    """
    state: str = Field(..., description="The current state of the service.")
    msg: str = Field(..., description="A message describing the state of the service.")


class AppStatus(BaseModel):
    """
    Represents the status of an application.
    """
    status: AppStatusEnum = Field(..., description="The current status of the application.")
