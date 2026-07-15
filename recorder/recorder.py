import time

from recorder.dataset_writer import DatasetWriter
from recorder.session import RecordingSession


class Recorder:

    def __init__(self):

        self.writer = DatasetWriter()

        self.session = RecordingSession()

        self.recording = False

    def start(self):

        self.session = RecordingSession()

        self.recording = True

        print("=== RECORD START ===")

    def stop(self):

        self.recording = False

        self.writer.save(self.session)

        print("=== RECORD STOP ===")

    def add(self, frame, action):

        if not self.recording:
            return

        self.session.frames.append(frame)
        self.session.actions.append(
            action.to_numpy()
        )
        self.session.timestamps.append(time.perf_counter())

    @property
    def frame_count(self):

        return len(self.session.frames)