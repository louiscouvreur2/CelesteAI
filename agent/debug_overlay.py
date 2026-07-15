import time


class DebugOverlay:

    def __init__(self):

        self.last = time.perf_counter()

        self.frames = 0

        self.fps = 0

    def update(self):

        self.frames += 1

        now = time.perf_counter()

        if now - self.last >= 1:

            self.fps = self.frames

            self.frames = 0

            self.last = now

    def draw(self, prediction):

        self.update()

        print(
            "\033[2J\033[H",
            end=""
        )

        names = [

            "Up",

            "Left",

            "Down",

            "Right",

            "Jump",

            "Grab",

            "Dash",

        ]

        print("====== CELESTE AI ======")

        print()

        print("FPS :", self.fps)

        print()

        for name, value in zip(

            names,

            prediction,

        ):

            print(f"{name:>6} : {int(value)}")

        print()

        print("F9 -> STOP")