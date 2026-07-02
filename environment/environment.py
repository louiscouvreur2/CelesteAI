from __future__ import annotations

from capture.capture_manager import CaptureManager
from capture.frame import Frame

from environment.action_executor import ActionExecutor
from environment.actions import Action
from environment.state import GameState
from environment.step import StepResult


class CelesteEnvironment:

    def __init__(self):

        self.capture = CaptureManager()

        self.executor = ActionExecutor()

    def reset(self):

        self.capture.start()

        frame = self.capture.get_frame()

        while frame is None:
            frame = self.capture.get_frame()

        return self._frame_to_state(frame)

    def close(self):

        self.capture.stop()

    def step(self, action: Action):

        self.executor.execute(action)

        frame = self.capture.get_frame()

        while frame is None:
            frame = self.capture.get_frame()

        state = self._frame_to_state(frame)

        return StepResult(
            state=state,
            reward=0.0,
            done=False,
            info={},
        )

    @staticmethod
    def _frame_to_state(frame: Frame):

        return GameState(
            frame=frame.image,
            frame_id=frame.frame_id,
            timestamp=frame.timestamp,
        )