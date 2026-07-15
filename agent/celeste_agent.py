import time
import keyboard

from capture.capture_manager import CaptureManager
from vision.pipeline import VisionPipeline
from vision.frame_stack import FrameStack

from learning.inference_engine import InferenceEngine
from input.keyboard_output import KeyboardOutput

from agent.debug_overlay import DebugOverlay

from learning.action_filter import ActionFilter

class CelesteAgent:

    def __init__(self):

        self.filter = ActionFilter()

        self.overlay = DebugOverlay()

        self.capture = CaptureManager()

        self.pipeline = VisionPipeline()

        self.stack = FrameStack(size=8)

        self.network = InferenceEngine()

        self.keyboard = KeyboardOutput()

        self.running = False

    def run(self):

        print("===== AI STARTED =====")
        print("F9 : Stop AI")

        self.capture.start()

        self.running = True

        while self.running:

            if keyboard.is_pressed("F9"):
                break

            frame = self.capture.get_frame()

            if frame is None:
                continue

            image = self.pipeline.process(frame.image)

            self.stack.push(image)

            if not self.stack.ready():
                continue

            prediction = self.network.predict(
                self.stack.get()
            )

            prediction = self.filter.process(prediction)

            self.keyboard.send(prediction)

            self.overlay.draw(prediction)

            time.sleep(1 / 60)

        self.keyboard.release_all()

        print("AI stopped.")