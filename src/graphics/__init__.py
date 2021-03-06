# Libs
import logging
import pygame
import time, datetime
from importlib import import_module

# Globals
import globals as globs

# The package files
from .cursors import *
from menu import *

from game import GameClient
from game.worldblocks import *
from .baseclasses import Text


logger = logging.getLogger("gfx")

logger.info("Loading graphics")

# Clock for fps and events triggered by frames

pygame.display.init()

# Draw queue
globs.drawqueue = []


def load_menus():
    menus = {}
    menus['main'] = MainMenu()
    menus['settings'] = SettingsMenu()
    menus['characters'] = CharacterMenu()
    menus['characterCreator'] = CreateCharacterMenu()
    menus['multiplayerConnectMenu'] = MultiplayerConnectMenu()
    globs.menus = menus

def loop():
    mode, sub = globs.location.split('.')
    #print(globs.location)
    if mode == "menu":
        if globs.lastlocation != globs.location or globs.redraw:
            globs.menus[sub].drawBackground()
            globs.menus[sub].draw()
            globs.redraw = False
        globs.menus[sub].blit()

    elif mode == "game":
        if globs.lastlocation != globs.location:
            globs.currentgame = GameClient(screen)
            if globs.lastlocation.split('.')[0] != globs.location.split('.')[0]:
                # If first time inGame
                game.load_character()
                #print("Loaded character")
            globs.currentgame.load(sub)

        globs.currentgame.loop()

    if globs.config.get("dev", "fpsmeter") == "True":
        fps_counter()

    if globs.lastlocation != globs.location:
        pygame.display.update()
    if globs.config.get("dev", "dirtyrectdebug") == "True":
        for rect in globs.dirtyrects:
            pygame.draw.rect(globs.screen, (255,0,255), rect, 2)
        pygame.display.update()
    if globs.config.get("dev", "dirtyrects") == "True":
        pygame.display.update(globs.dirtyrects)
    else:
        pygame.display.update()
    globs.dirtyrects = []


def fps_counter():
    globs.fpstext = Text((0,0), str(globs.clock.get_fps())[:2], 30, color=(150,150,150))
    globs.fpstext.blit()

def initialize_screen():
    # Set globs.resolution
    if hasattr(globs, "resolution"):
        pass
    else:
        string = globs.config.get("video", "resolution")
        globs.resolution = globs.config.get("video", "resolution").split('x')
        globs.resolution = map(int, globs.resolution)

    # Check if fullscreen
    if hasattr(globs, "fullscreen"):
        fullscreen = globs.fullscreen
    else:
        string = globs.config.get("video", "fullscreen")
        if string == 'True':
            fullscreen = True
        else:
            fullscreen = False
        globs.fullscreen = fullscreen
    # Inirialize screen
    global screen
    if fullscreen:
        screen = pygame.display.set_mode(globs.resolution, pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(globs.resolution)
    print("Resolution: {}  Fullscreen: {}".format(str(globs.resolution), str(fullscreen)))
    globs.screen = screen

    # Reinitialize menus for new resolution
    load_menus()

def screenshot():
    pygame.image.save(globs.screen, "screenshots/"+time.strftime("%Y-%m-%d %Hh %Mm %Ss")+".png")
    print("Screenshot captured!")

def load_cursor(name):
    cursor = eval(name)()
    compiledCursor = pygame.cursors.compile(cursor.stringcursor, black=cursor.black, white=cursor.white, xor='o')
    pygame.mouse.set_cursor(cursor.size,(4,4),*compiledCursor)

def getFont(name, fontsize):
    fontlocation = globs.cwd + "/data/fonts/" + name + ".ttf"
    return pygame.font.Font(fontlocation, fontsize)

globs.getFont = getFont
globs.initialize_screen = initialize_screen
globs.load_cursor = load_cursor
initialize_screen()
load_cursor("CircleCursor_black")
