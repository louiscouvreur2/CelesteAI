import keyboard


class KeyboardOutput:

    KEYS = [
        "z",
        "q",
        "s",
        "d",
        "space",
        "j",
        "k",
    ]

    def send(self, prediction):

        for key, pressed in zip(
            self.KEYS,
            prediction,
        ):

            if pressed:

                keyboard.press(key)

            else:

                keyboard.release(key)

    def release_all(self):

        for key in self.KEYS:

            keyboard.release(key)