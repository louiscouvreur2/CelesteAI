from enum import Enum, auto


class EngineState(Enum):

    STOPPED = auto()

    STARTING = auto()

    RUNNING = auto()

    PAUSED = auto()

    STOPPING = auto()