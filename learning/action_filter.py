import numpy as np


class ActionFilter:

    def __init__(self):

        self.previous = np.zeros(7, dtype=bool)

        self.dash_cooldown = 0

    def process(self, prediction):

        prediction = prediction.astype(bool)

        # Gauche / Droite incompatibles
        if prediction[1] and prediction[3]:
            prediction[3] = False

        # Haut / Bas incompatibles
        if prediction[0] and prediction[2]:
            prediction[2] = False

        # Dash : un seul appui toutes les 15 frames
        if self.dash_cooldown > 0:

            prediction[6] = False

            self.dash_cooldown -= 1

        elif prediction[6]:

            self.dash_cooldown = 15

        self.previous = prediction.copy()

        return prediction