from pathlib import Path

from capture.frame import Frame

from recorder.metadata import MetadataWriter
from recorder.session import RecordingSession
from recorder.writer import FrameWriter


class Recorder:

    def __init__(self):

        self.root = Path("recordings")

        self.root.mkdir(exist_ok=True)

        self.recording = False

        self.session = None

    def start(self):

        self.session = RecordingSession.create(self.root)

        self.writer = FrameWriter(

            self.session.path / "frames"

        )

        self.recording = True

        print("=== RECORD START ===")

    def stop(self):

        MetadataWriter().write(self.session)

        self.recording = False

        print("=== RECORD STOP ===")

    def record(self, frame: Frame):

        if not self.recording:

            return

        self.writer.write(frame)

        self.session.frame_count += 1