from learning.dataset_inspector import DatasetInspector
from learning.replay_analyzer import ReplayAnalyzer


def main():

    DatasetInspector().inspect()

    ReplayAnalyzer().analyze()


if __name__ == "__main__":

    main()