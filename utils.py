from questions import quiz_questions
import globals
def check_won_game():
    if(globals.actualQuestion == len(quiz_questions)):
        globals.won_game = True

def init_game():
    globals.menu_screen = False
    globals.lost_game = False
    globals.won_game = False
    globals.actualQuestion = 0
    globals.help_screen = False

def reset_game():
    globals.menu_screen = True
    globals.lost_game = False
    globals.won_game = False
    globals.actualQuestion = 0
    globals.help_screen = False
