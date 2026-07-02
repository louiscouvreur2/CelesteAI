from core.paths import create_directories
from core.logger import setup_logger
from core.version import PROJECT_NAME, VERSION


def main():

    create_directories()

    logger = setup_logger()

    logger.info("--------------------------------------")
    logger.info(f"{PROJECT_NAME} {VERSION}")
    logger.info("Initialisation...")
    logger.info("Projet créé avec succès.")
    logger.info("--------------------------------------")


if __name__ == "__main__":
    main()