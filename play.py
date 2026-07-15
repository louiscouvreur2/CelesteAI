from engine.application import Application


def main():

    app = Application(
        mode="play",
    )

    app.run()


if __name__ == "__main__":
    main()