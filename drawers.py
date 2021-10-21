from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from questions import quiz_questions
import globals
def draw_button_menu(x,y):
    glBegin(GL_LINE_LOOP)
    glVertex3f(x, y, 0)
    glVertex3f(x, y + globals.height_button, 0)
    glVertex3f(x + globals.width_button, y + globals.height_button, 0)
    glVertex3f(x + globals.width_button, y, 0)
    glEnd()

def draw_text(word, x , y):
    glRasterPos2f(x, y)
    for i in word:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(i))

def draw_main_menu():
    draw_text('Quiz COVIDÃO', globals.center_button, 100)
    draw_text('Começar',globals.center_button + 80 ,350 + globals.height_button/1.6)
    draw_text('Sair', globals.center_button + 100,400 + globals.height_button/1.6)
    draw_button_menu(globals.center_button, 350)
    draw_button_menu(globals.center_button, 400)
 
def draw_question(question):
    size = len(question)
    draw_text(question, 100 - size/2, 100)

def draw_alternatives(alternatives):
    height = 350
    for alternative in alternatives:
        size = len(alternative)
        draw_text(alternative, globals.center_button + 100 - size*4, height + globals.height_button/1.6 )
        draw_button_menu(globals.center_button, height)
        height += 50
    
def draw_quiz_game():
    draw_question(quiz_questions[globals.actualQuestion]['question'])
    draw_alternatives(quiz_questions[globals.actualQuestion]['alternatives'])

def draw_lose_game():
    draw_text('Infelizmente você PERDEU!', globals.center_button - 60 , 100)
    draw_text('Recomeçar',globals.center_button + 80 ,350 + globals.height_button/1.6)
    draw_text('Sair', globals.center_button + 100,400 + globals.height_button/1.6)
    draw_button_menu(globals.center_button, 350)
    draw_button_menu(globals.center_button, 400)

def draw_won_game():
    draw_text('Parabéns você ganhou o Quiz COVIDÃO!', globals.center_button - 100, 100)
    draw_text('Recomeçar',globals.center_button + 80 ,350 + globals.height_button/1.6)
    draw_text('Sair', globals.center_button + 100,400 + globals.height_button/1.6)
    draw_button_menu(globals.center_button, 350)
    draw_button_menu(globals.center_button, 400)

    
def draw_help_screen():
    draw_text('Bem vindo a tela de ajuda!', 0, 100)
    draw_text('1 - Você precisa acertar todas as perguntas para ganhar!', 0, 130)
    draw_text('2 - Errou, perdeu!', 0, 160)
    draw_text('3 - As teclas 1,2 e 3 servem também para apertar os botões', 0, 190)
    draw_text('4 - Aperte F1 para ajuda, F2 para Sair e F3 para resetar o jogo', 0, 220)
    draw_text('5 - Aperte ESC ou F3 para resetar', 0, 250)