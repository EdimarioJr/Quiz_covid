from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from event_resolvers import check_main_menu_click, check_quiz_click
from utils import reset_game
import globals

def special_controller(key, x, y):
    global help_screen, menu_screen, won_game, lost_game, actualQuestion
    if(key == 1):
        globals.help_screen = True
        globals.menu_screen = False
        globals.won_game = False
        globals.lost_game = False
        globals.actualQuestion = 0
    elif(key == 2):
        glutDestroyWindow(globals.window)
    elif(key == 3):
        reset_game()
    glutPostRedisplay()

def keyboard_controller(key, x, y):
    if(key == b'1'):
        if(globals.menu_screen or globals.lost_game or globals.won_game):
            check_main_menu_click(globals.center_button, 350 )
        else: 
            check_quiz_click(globals.center_button, 350)
    elif(key == b'2'):
        if(globals.menu_screen or globals.lost_game or globals.won_game):
            check_main_menu_click(globals.center_button, 400 )
        else: 
            check_quiz_click(globals.center_button, 400)
    elif(key == b'3'):
        if(globals.menu_screen or globals.lost_game or globals.won_game):
            pass
        else: 
            check_quiz_click(globals.center_button, 450)
    elif(key == b'\x1b'):
        reset_game()
    glutPostRedisplay()

def mouse_controller(button, state, x, y):
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
            if(globals.menu_screen or globals.lost_game or globals.won_game or globals.help_screen):
                check_main_menu_click(x, y)
            else: 
                check_quiz_click(x, y)
    glutPostRedisplay()