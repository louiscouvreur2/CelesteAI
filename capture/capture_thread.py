import time

from PySide6.QtCore import QThread

from capture import frame
from capture.capture_manager import CaptureManager
from capture.frame_converter import FrameConverter

from vision.pipeline import VisionPipeline
from vision.frame_stack import FrameStack

from recorder.recorder import Recorder
from input.key_state import KeyState
import keyboard

class CaptureThread(QThread):

    def __init__(self, signals):

        self.keys = KeyState()

        self.recorder = Recorder()

        self.previous_f8 = False

        super().__init__()

        self.signals = signals

        self.capture = CaptureManager()

        self.running = True

        self.pipeline = VisionPipeline()

        self.stack = FrameStack()

    def run(self):

        self.capture.start()

        last = time.perf_counter()

        frames = 0

        while self.running:

            frame = self.capture.get_frame()

            if frame is None:
                continue

            processed = self.pipeline.process(frame.image)

            keys = self.keys.get()

            action = keys

            pressed = keyboard.is_pressed("F8")

            if pressed and not self.previous_f8:

                if self.recorder.recording:

                    self.recorder.stop()

                else:

                    self.recorder.start()

            self.previous_f8 = pressed

            self.stack.push(processed)

            self.recorder.add(
                self.stack.get(),
                action,
            )

            image = FrameConverter.to_qimage(frame.image)

            self.signals.frame_ready.emit(image)

            frames += 1

            now = time.perf_counter()

            if now - last >= 1:

                self.signals.fps_updated.emit(frames)

                frames = 0

                last = now

        self.capture.stop()

    def stop(self):

        self.running = False