from typing import Text
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from questions import quiz_questions
import random
import time
width = 700
height = 700
center_button = width/2 - 75
height_button = 40
width_button = 200
menu_screen = True
help_screen = False
exit_game = False
window = None
actualQuestion = 0
lost_game = False
won_game = False


def draw_button_menu(x,y):
    glBegin(GL_LINE_LOOP)
    glVertex3f(x, y, 0)
    glVertex3f(x, y + height_button, 0)
    glVertex3f(x + width_button, y + height_button, 0)
    glVertex3f(x + width_button, y, 0)
    glEnd()

def draw_text(word, x , y):
    glRasterPos2f(x, y)
    for i in word:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(i))

def draw_main_menu():
    draw_text('Quiz COVIDÃO', center_button, 100)
    draw_text('Começar',center_button + 30 ,350 + height_button/1.6)
    draw_text('Sair', center_button + 55,400 + height_button/1.6)
    draw_button_menu(center_button, 350)
    draw_button_menu(center_button, 400)
 
def draw_question(question):
    draw_text(question, 0, 100)

def draw_alternatives(alternatives):
    height = 350
    for alternative in alternatives:
        draw_text(alternative, center_button, height + height_button/1.6 )
        draw_button_menu(center_button, height)
        height += 50
    
def draw_quiz_game():
    draw_question(quiz_questions[actualQuestion]['question'])
    draw_alternatives(quiz_questions[actualQuestion]['alternatives'])

def check_main_menu_click(x, y):
     global menu_screen
     global lost_game
     global won_game
     global actualQuestion
     if(x >= center_button and x<= center_button + width_button):
        if(y >= 350 and y <= 350 + height_button):
            init_game()
        elif(y>=400 and y<= 400 + height_button):
            glutDestroyWindow(window)

def check_quiz_click(x,y):
    global actualQuestion, lost_game, click
    if(x >= center_button and x<= center_button + width_button):
        if(y >= 350 and y <= 350 + height_button):
            if(quiz_questions[actualQuestion]['right_answer'] == 0):
                actualQuestion+= 1
                check_won_game()
                return
            else:
                lost_game = True
        elif(y>=400 and y<= 400 + height_button):
            if(quiz_questions[actualQuestion]['right_answer'] == 1):
                actualQuestion += 1
                check_won_game()
                return
            else: 
                lost_game = True
        elif(len(quiz_questions[actualQuestion]['alternatives']) == 3):
            if(y>=450 and y<= 450 + height_button):
                if(quiz_questions[actualQuestion]['right_answer'] == 2):
                    actualQuestion +=1
                    check_won_game()
                    return
                else:
                    lost_game = True
    

def check_won_game():
    global won_game
    if(actualQuestion == len(quiz_questions)):
        won_game = True

def draw_lose_game():
    draw_text('Infelizmente você PERDEU!', center_button, 100)
    draw_text('Recomeçar',center_button + 30 ,350 + height_button/1.6)
    draw_text('Sair', center_button + 55,400 + height_button/1.6)
    draw_button_menu(center_button, 350)
    draw_button_menu(center_button, 400)

def draw_won_game():
    draw_text('Parabéns você ganhou o Quiz COVIDÃO!', center_button, 100)
    draw_text('Recomeçar',center_button + 30 ,350 + height_button/1.6)
    draw_text('Sair', center_button + 55,400 + height_button/1.6)
    draw_button_menu(center_button, 350)
    draw_button_menu(center_button, 400)

def mouse_controller(button, state, x, y):
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
            if(menu_screen or lost_game or won_game or help_screen):
                check_main_menu_click(x, y)
            else: 
                check_quiz_click(x, y)
    glutPostRedisplay()

def init_game():
    global menu_screen, lost_game, won_game, actualQuestion, help_screen
    menu_screen = False
    lost_game = False
    won_game = False
    actualQuestion = 0
    help_screen = False

def reset_game():
    global menu_screen, lost_game, won_game, actualQuestion, help_screen
    menu_screen = True
    lost_game = False
    won_game = False
    actualQuestion = 0
    help_screen = False

def keyboard_controller(key, x, y):
    if(key == b'1'):
        if(menu_screen or lost_game or won_game):
            check_main_menu_click(center_button, 350 )
        else: 
            check_quiz_click(center_button, 350)
    elif(key == b'2'):
        if(menu_screen or lost_game or won_game):
            check_main_menu_click(center_button, 400 )
        else: 
            check_quiz_click(center_button, 400)
    elif(key == b'3'):
        if(menu_screen or lost_game or won_game):
            pass
        else: 
            check_quiz_click(center_button, 450)
    elif(key == b'\x1b'):
        reset_game()
    glutPostRedisplay()
    
def draw_help_screen():
    draw_text('Bem vindo a tela de ajuda!', 0, 100)
    draw_text('1 - Você precisa acertar todas as perguntas para ganhar!', 0, 130)
    draw_text('2 - Errou, perdeu!', 0, 160)
    draw_text('3 - As teclas 1,2 e 3 servem também para apertar os botões', 0, 190)
    draw_text('4 - Aperte F1 para ajuda, F2 para Sair e F3 para resetar o jogo', 0, 220)
    draw_text('5 - Aperte ESC ou F3 para resetar', 0, 250)

def special_controller(key, x, y):
    global help_screen, menu_screen, won_game, lost_game, actualQuestion
    if(key == 1):
        help_screen = True
        menu_screen = False
        won_game = False
        lost_game = False
        actualQuestion = 0
    elif(key == 2):
        glutDestroyWindow(window)
    elif(key == 3):
        reset_game()
    glutPostRedisplay()


def inicializa ():
    glClearColor(0.0, 0.0, 1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    gluOrtho2D(0.0, width, height, 0.0)

def desenha ():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if(menu_screen):
        draw_main_menu()
    elif(lost_game):
        draw_lose_game()
    elif(won_game):
        draw_won_game()
    elif(help_screen):
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
    glutInitWindowSize(width, height)
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