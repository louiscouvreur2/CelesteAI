import keyboard

from learning.actions import ActionState

class KeyState:

        def get(self):

            return ActionState(

                up=keyboard.is_pressed("z"),

                left=keyboard.is_pressed("q"),

                down=keyboard.is_pressed("s"),

                right=keyboard.is_pressed("d"),

                jump=keyboard.is_pressed("space"),

                grab=keyboard.is_pressed("j"),

                dash=keyboard.is_pressed("k"),

            )