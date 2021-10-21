from typing import Text
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import globals
from controllers import mouse_controller, keyboard_controller, special_controller
from drawers import draw_main_menu,draw_lose_game,draw_won_game,draw_help_screen,draw_quiz_game

def inicializa ():
    glClearColor(0.0, 0.0, 1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    gluOrtho2D(0.0, globals.width, globals.height, 0.0)

def desenha ():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if(globals.menu_screen):
        draw_main_menu()
    elif(globals.lost_game):
        draw_lose_game()
    elif(globals.won_game):
        draw_won_game()
    elif(globals.help_screen):
        draw_help_screen()
    else:
        draw_quiz_game()
    glutSwapBuffers()
   
def change_background():
    glClearColor(random.randrange(0, 10)/10, 
            random.randrange(0, 10)/10, random.randrange(0, 10)/10, random.randrange(0,10)/10)
    glutPostRedisplay()
   
def quit_game():
   glutDestroyWindow(window)

def dmenu(item):
    menudict[item]()
    return 0
CHANGE_BACKGROUND, QUIT = list(range(2))
menudict ={CHANGE_BACKGROUND: change_background, QUIT: quit_game }

def main():
    global window
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(globals.width, globals.height)
    window = glutCreateWindow("Quiz Covid")
    glutMouseFunc(mouse_controller)
    glutKeyboardFunc(keyboard_controller)
    glutCreateMenu(dmenu)
    glutAddMenuEntry("Mudar Cor de fundo", CHANGE_BACKGROUND)
    glutAddMenuEntry("Terminar programa", QUIT)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    glutSpecialFunc(special_controller)
    glutDisplayFunc(desenha)
    inicializa()
    glutMainLoop()

main()