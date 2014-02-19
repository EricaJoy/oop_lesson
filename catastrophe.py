import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys
import random



#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 8
GAME_HEIGHT = 8

#### Put class definitions here ####

class Cat(GameElement):
    IMAGE = "Cat"
    SOLID = True
    x,y = 0,0

class Bush(GameElement):
    IMAGE = "ShortTree"
    SOLID = True

class Ralf(GameElement):
    IMAGE = "Horns"
    SOLID = False
####   End class definitions    ####

def run_level():
    #Gets all the cats and the one ralf, on the board
    #directs them to move to random coordinates on the board
    #if they happen to pick the same coordinates, it's ok
    #they just overlap, no big deal. 
    #CAT = [] ##think about throwing this in a list later to make it cleaner
    cats = [Cat(), Cat(), Cat(), Cat(), Cat(), Cat(), Cat(), Cat(), Cat(), Cat()]





    for cat in cats:
        cat.x, cat.y = random.randint(0,7), random.randint(0,7)
        GAME_BOARD.register(cat)
        GAME_BOARD.set_el(cat.x, cat.y, cat)

    RALF = Ralf()
    GAME_BOARD.register(RALF)
    GAME_BOARD.set_el(random.randint(0,7), random.randint(0,7), RALF)


    # Loop for the timer
    #figuring out this timer thing
    #and causing movement increments 
    def update(dt):

        # Move the cats around
        i = 0
        for cat in cats:
            if RALF.x == cat.x and RALF.y == cat.y:
                GAME_BOARD.draw_msg("CHOMP!")
                del cats[i]
            else: 
                GAME_BOARD.del_el(cat.x, cat.y)
                GAME_BOARD.erase_msg()
            i += 1


        for cat in cats:
            GAME_BOARD.set_el(random.randint(0,7), random.randint(0,7), cat)
        # End move the cats around

        # Move RALF around
        GAME_BOARD.del_el(RALF.x, RALF.y)
        GAME_BOARD.set_el(random.randint(0,7), random.randint(0,7), RALF)
        # End move RALF around
    pyglet.clock.schedule_interval(update,1)


    # Ralf randomly appears to eat cats
    # Compare Ralf x,y to all cats x,y
    # If Ralf x,y = cat x,y, Ralf eats the cat
    #  (cat disappaers from square, Ralf appears)
    # GAME_BOARD.del_el(CAT.x, CAT.y)
    # Else Ralf just appears on random x,y location

def initialize():
    """Put game initialization code here"""

    # global PLAYER
    # PLAYER = Character()
    # GAME_BOARD.register(PLAYER)
    # GAME_BOARD.set_el(2, 2, PLAYER)
    # print PLAYER

    run_level()
# for level in levels():
#     run_level(level)