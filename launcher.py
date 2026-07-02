from core.logger import setup_logger
from core.paths import create_directories
from core.version import PROJECT_NAME, VERSION

from capture.window import find_celeste_window

from capture.capture import ScreenCapture
from capture.viewer import Viewer


def main():

    create_directories()

    logger = setup_logger()

    logger.info("=========================================")
    logger.info(f"{PROJECT_NAME} {VERSION}")
    logger.info("Starting CelesteAI...")
    logger.info("=========================================")

    window = find_celeste_window()

    if window is None:
        logger.warning("Celeste n'a pas été trouvé.")
        logger.warning("Lance le jeu puis redémarre CelesteAI.")
        return

    logger.info("Fenêtre détectée")
    logger.info(f"Titre : {window.title}")
    logger.info(f"Résolution : {window.width}x{window.height}")

    capture = ScreenCapture(window)

    viewer = Viewer(capture)

    logger.info("Ouverture du viewer...")

    viewer.run()

if __name__ == "__main__":
    main()


