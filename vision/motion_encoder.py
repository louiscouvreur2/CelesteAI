import numpy as np


class MotionEncoder:

    @staticmethod
    def encode(frames):

        """
        Entrée :
            (8, H, W, 3)

        Sortie :
            (15, H, W)

        8 images niveaux de gris
        +
        7 cartes de mouvement
        """

        gray = []

        for frame in frames:

            g = frame.mean(axis=2)

            gray.append(g)

        gray = np.asarray(gray, dtype=np.float32)

        motion = []

        for i in range(len(gray) - 1):

            diff = np.abs(

                gray[i + 1] - gray[i]

            )

            motion.append(diff)

        motion = np.asarray(

            motion,

            dtype=np.float32,

        )

        return np.concatenate(

            [

                gray,

                motion,

            ],

            axis=0,

        )