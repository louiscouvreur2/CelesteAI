from environment.actions import Action

from game.controller import Controller


class ActionExecutor:

    def __init__(self):

        self.controller = Controller()

    def execute(self, action: Action):

        if action == Action.IDLE:

            self.controller.execute_idle()

        elif action == Action.LEFT:

            self.controller.execute_left()

        elif action == Action.RIGHT:

            self.controller.execute_right()

        elif action == Action.JUMP:

            self.controller.jump()

        elif action == Action.DASH:

            self.controller.dash()

        elif action == Action.GRAB:

            self.controller.grab()

        else:

            pass