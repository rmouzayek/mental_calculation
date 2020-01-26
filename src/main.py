import logging

from controller import Controller


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename='mental_calculations.log')
    new_game = Controller()
    new_game.run()