import logging
import os
import time
from importlib import import_module
import pygame
from pygame import Rect


maindir = os.path.dirname(os.getcwd())

# Logging
logFormat = '%(asctime)-15s %(levelname)s %(name)s:%(lineno)s\t  %(message)s'
logFilename = maindir+"/logs/"+time.strftime("%Y-%m-%d %Hh %Mm")+".log"
logging.basicConfig(filename=logFilename, filemode='w', level=logging.DEBUG, format=logFormat)


class Game():
    def __init__(self):
        self.logger = logging.getLogger("main")
        self.fullscreen = False
        pygame.init()

    def load(self):
        self.logger.info("Loading game")
        print("Loading game")

        global inputs, graphics, events, globs
        globs = import_module("globals", __name__)
        inputs = import_module("input", __name__).Input()
        graphics = import_module("graphics", __name__)
        events = import_module("events", __name__).Events()


    def run(self):
        self.a = 0
        while True:
            events.loop()
            inputs.loop()
            graphics.loop()
            if inputs.quit():
                break

    def quit(self):
        pass


if __name__ == '__main__':
    game = Game()
    game.load()
    game.run()
    game.quit()
