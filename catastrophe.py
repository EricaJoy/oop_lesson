import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys
import random
import ast



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

def keyboard_handler():
    answer = ""
    if KEYBOARD[key.A]:
        GAME_BOARD.draw_msg("a")
        answer = answer + "a"
    if KEYBOARD[key.B]:
        GAME_BOARD.draw_msg("b")
        answer = answer + "b"
    if KEYBOARD[key.C]:
        GAME_BOARD.draw_msg("c")
        answer = answer + "c"
    if KEYBOARD[key.D]:
        GAME_BOARD.draw_msg("d")
        answer = answer + "d"
    if KEYBOARD[key.E]:
        GAME_BOARD.draw_msg("e")
        answer = answer + "e"
    if KEYBOARD[key.F]:
        GAME_BOARD.draw_msg("f")
        answer = answer + "f"
    if KEYBOARD[key.G]:
        GAME_BOARD.draw_msg("g")
        answer = answer + "g"
    if KEYBOARD[key.H]:
        GAME_BOARD.draw_msg("h")
        answer = answer + "h"
    if KEYBOARD[key.I]:
        GAME_BOARD.draw_msg("i")
        answer = answer + "i"
    if KEYBOARD[key.J]:
        GAME_BOARD.draw_msg("j")
        answer = answer + "j"
    if KEYBOARD[key.K]:
        GAME_BOARD.draw_msg("k")
        answer = answer + "k"
    if KEYBOARD[key.L]:
        GAME_BOARD.draw_msg("l")
        answer = answer + "l"
    if KEYBOARD[key.M]:
        GAME_BOARD.draw_msg("m")
        answer = answer + "m"
    if KEYBOARD[key.N]:
        GAME_BOARD.draw_msg("n")
        answer = answer + "n"
    if KEYBOARD[key.O]:
        GAME_BOARD.draw_msg("o")
        answer = answer + "o"
    if KEYBOARD[key.P]:
        GAME_BOARD.draw_msg("p")
        answer = answer + "p"
    if KEYBOARD[key.Q]:
        GAME_BOARD.draw_msg("q")
        answer = answer + "q"
    if KEYBOARD[key.R]:
        GAME_BOARD.draw_msg("r")
        answer = answer + "r"
    if KEYBOARD[key.S]:
        GAME_BOARD.draw_msg("s")
        answer = answer + "s"
    if KEYBOARD[key.T]:
        GAME_BOARD.draw_msg("t")
        answer = answer + "t"
    if KEYBOARD[key.U]:
        GAME_BOARD.draw_msg("u")
        answer = answer + "u"
    if KEYBOARD[key.V]:
        GAME_BOARD.draw_msg("v")
        answer = answer + "v"
    if KEYBOARD[key.W]:
        GAME_BOARD.draw_msg("w")
        answer = answer + "w"
    if KEYBOARD[key.X]:
        GAME_BOARD.draw_msg("x")
        answer = answer + "x"
    if KEYBOARD[key.Y]:
        GAME_BOARD.draw_msg("y")
        answer = answer + "y"
    if KEYBOARD[key.Z]:
        GAME_BOARD.draw_msg("z")
        answer = answer + "z"
    if KEYBOARD[key.BACKSPACE]:
        GAME_BOARD.backspace()
    if KEYBOARD[key.ENTER]:
        check_answer()

def check_answer():
    pass

def run_level(current_question):
    #Gets all the cats and the one ralf, on the board
    #directs them to move to random coordinates on the board
    #if they happen to pick the same coordinates, it's ok
    #they just overlap, no big deal. 
    #CAT = [] ##think about throwing this in a list later to make it cleaner
    cats = [Cat(), Cat(), Cat(), Cat(), Cat(), Cat(), Cat(), Cat(), Cat(), Cat()]
    chomp = pyglet.resource.media('hit.wav', streaming=False)


    GAME_BOARD.draw_msg(current_question +"\n >")    




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
                chomp.play()
                del cats[i]
            else: 
                GAME_BOARD.del_el(cat.x, cat.y)
                
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
    levels_file = 'questions.txt'
    levels = open(levels_file, 'r')
    open_level = ast.literal_eval(levels.read())
    

    # This pulls a dictionary from the questions.txt file

    # >> ERICA LOOK HERE. Can you call curr_ans a global?
    questions = open_level["level1"]
    current_question = random.choice(questions.keys())
    current_answer = questions[current_question]


    run_level(current_question)



# for level in levels():
#     run_level(level)



# for i in string.ascii_uppercase:
#     print '    if KEYBOARD[key.'+i+']:'
#     print '        GAME_BOARD.draw_msg("'+i.lower()+'")'
#     print '        answer = answer + "'+i.lower()+'"'