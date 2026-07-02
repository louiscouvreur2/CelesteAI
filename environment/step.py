from dataclasses import dataclass

from environment.state import GameState


@dataclass(slots=True)
class StepResult:
    """
    Résultat d'un step de l'environnement.
    """

    state: GameState

    reward: float

    done: bool

    info: dict