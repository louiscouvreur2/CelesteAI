from dataclasses import dataclass
from pathlib import Path
import time


@dataclass(slots=True)
class RecordingSession:

    id: str

    path: Path

    start_time: float

    frame_count: int = 0

    action_count: int = 0

    @classmethod
    def create(cls, root: Path):

        session_id = time.strftime("%Y%m%d_%H%M%S")

        folder = root / session_id

        folder.mkdir(parents=True, exist_ok=True)

        (folder / "frames").mkdir()

        return cls(

            id=session_id,

            path=folder,

            start_time=time.perf_counter(),

        )