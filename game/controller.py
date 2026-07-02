from input.keyboard import KeyboardController
from input.keys import Keys


class Controller:

    def __init__(self):

        self.keyboard = KeyboardController()

    def release_all(self):

        self.keyboard.release_all()

    def execute_idle(self):

        self.release_all()

    def execute_left(self):

        self.keyboard.press(Keys.LEFT.value)

        self.keyboard.release(Keys.RIGHT.value)

    def execute_right(self):

        self.keyboard.press(Keys.RIGHT.value)

        self.keyboard.release(Keys.LEFT.value)

    def jump(self):

        self.keyboard.tap(Keys.JUMP.value)

    def dash(self):

        self.keyboard.tap(Keys.DASH.value)

    def grab(self):

        self.keyboard.press(Keys.GRAB.value)

    def release_grab(self):

        self.keyboard.release(Keys.GRAB.value)