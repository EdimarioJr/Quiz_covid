from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from questions import quiz_questions
from utils import init_game,check_won_game
import globals
def check_main_menu_click(x, y):
     if(x >= globals.center_button and x<= globals.center_button + globals.width_button):
        if(y >= 350 and y <= 350 + globals.height_button):
            init_game()
        elif(y>=400 and y<= 400 + globals.height_button):
            glutDestroyWindow(globals.window)

def check_quiz_click(x,y):
    if(x >= globals.center_button and x<= globals.center_button + globals.width_button):
        if(y >= 350 and y <= 350 + globals.height_button):
            if(quiz_questions[globals.actualQuestion]['right_answer'] == 0):
                globals.actualQuestion+= 1
                check_won_game()
                return
            else:
                globals.lost_game = True
        elif(y>=400 and y<= 400 + globals.height_button):
            if(quiz_questions[globals.actualQuestion]['right_answer'] == 1):
                globals.actualQuestion += 1
                check_won_game()
                return
            else: 
                globals.lost_game = True
        elif(len(quiz_questions[globals.actualQuestion]['alternatives']) == 3):
            if(y>=450 and y<= 450 + globals.height_button):
                if(quiz_questions[globals.actualQuestion]['right_answer'] == 2):
                    globals.actualQuestion +=1
                    check_won_game()
                    return
                else:
                    globals.lost_game = True