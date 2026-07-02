from enum import Enum, auto


class Action(Enum):
    IDLE = auto()

    LEFT = auto()
    RIGHT = auto()

    UP = auto()
    DOWN = auto()

    JUMP = auto()

    DASH = auto()

    GRAB = auto()

    LEFT_JUMP = auto()
    RIGHT_JUMP = auto()

    LEFT_DASH = auto()
    RIGHT_DASH = auto()

    UP_DASH = auto()
    DOWN_DASH = auto()