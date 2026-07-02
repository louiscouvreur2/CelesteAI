import logging

from core.paths import LOGS

LOG_FILE = LOGS / "celeste_ai.log"


def setup_logger():

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )

    return logging.getLogger("CelesteAI")