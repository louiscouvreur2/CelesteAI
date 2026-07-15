import torch

from capture.capture_manager import CaptureManager
from input.keyboard_output import KeyboardOutput
from learning.model_manager import ModelManager
from vision.frame_stack import FrameStack
from vision.pipeline import VisionPipeline


class Player:

    def __init__(self):

        self.capture = CaptureManager()

        self.pipeline = VisionPipeline()

        self.stack = FrameStack()

        self.keyboard = KeyboardOutput()

        self.model = ModelManager().load_latest()

    @torch.no_grad()
    def run(self):

        self.capture.start()

        while True:

            frame = self.capture.get_frame()

            if frame is None:
                continue

            image = self.pipeline.process(frame.image)

            self.stack.push(image)

            state = self.stack.get()

            tensor = (
                torch.tensor(state)
                .unsqueeze(0)
                .float()
            )

            tensor = tensor.permute(0, 1, 4, 2, 3)

            b, f, c, h, w = tensor.shape

            tensor = tensor.reshape(b, f * c, h, w)

            logits = self.model(tensor)

            prediction = (
                torch.sigmoid(logits) > 0.5
            ).cpu().numpy()[0]

            self.keyboard.update(prediction)