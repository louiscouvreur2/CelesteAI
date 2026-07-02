import pydirectinput


class KeyboardController:

    def press(self, key: str):

        pydirectinput.keyDown(key)

    def release(self, key: str):

        pydirectinput.keyUp(key)

    def tap(self, key: str):

        pydirectinput.press(key)

    def release_all(self):

        for key in [
            "q",
            "d",
            "z",
            "s",
            "space",
            "j",
            "k",
        ]:
            pydirectinput.keyUp(key)