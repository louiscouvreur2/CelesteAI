from dataclasses import dataclass

import numpy as np


@dataclass
class ActionState:

    up: bool = False
    left: bool = False
    down: bool = False
    right: bool = False

    jump: bool = False
    grab: bool = False
    dash: bool = False

    def to_numpy(self):

        return np.array(

            [

                self.up,

                self.left,

                self.down,

                self.right,

                self.jump,

                self.grab,

                self.dash,

            ],

            dtype=np.float32,

        )