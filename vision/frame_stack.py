from collections import deque

import numpy as np


class FrameStack:

    def __init__(self, size=8):

        self.frames = deque(maxlen=size)

        self.size = size

    def push(self, frame):

        self.frames.append(frame)

        while len(self.frames) < self.size:
            self.frames.append(frame)

    def get(self):

        return np.stack(self.frames, axis=0)

    def ready(self):

        return len(self.frames) == self.size
