from PyQt5 import QtWidgets
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sqrt
from cube import *

flag = False
flag2 = False

lightPosition = (-4.0, 2.0, 10.0, 1.0)
lightColor = (1.0, 1.0, 1.0, 1.0)
ambient = (0.5, 0.5, 0.5, 1)


class OpenGLWidget(QtWidgets.QOpenGLWidget):

    def initializeGL(self):
        glClearDepth(1.0)
        glClearColor(0.25, 0.4, 0.88, 1.0)
        # glDepthFunc(GL_LESS)
        # glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        self.cube = Cube()
        #glEnable(GL_CULL_FACE)  # Отрисовывается только видимая сторона плоскости
        glEnable(GL_LIGHTING)  # Включаем расчет освещения
        glEnable(GL_LIGHT0)  # Включаем источник

        glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)  # Разрешаем режим освещенности для двух сторон грани
        # glEnable(GL_COLOR_MATERIAL)  # Разрешаем цвет у материала

    def paintGL(self):
        # Настройка камеры для изометрического вида
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        global ambient, lightPosition, lightColor
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)  # Интенсивность освещения

        glLoadIdentity()

        glLightfv(GL_LIGHT0, GL_POSITION, lightPosition)  # Положение направленного источника света
        glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, (0.0, 0.0, 1.0))  # Его направление
        glLightfv(GL_LIGHT0, GL_SPECULAR, (0.0, 0.0, 0.0, 1.0))  # Интенсивность зеркального света
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightColor)  # Цвет света
        # glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 180.0)  # Угол между осью и стороной конуса, по умолчанию 180 градусов

        # Настройка свойств материала
        # Далее все идет только для внешней части (Front), т.к. только она и отрисовывается
        glMaterialfv(GL_FRONT, GL_DIFFUSE, lightColor)  # Отвечает за рассеивание материалом света с определенным цветом
        glMaterialfv(GL_FRONT, GL_AMBIENT, (0.7, 0.7, 0.7, 1.0))  # Отвечает за затемнение цвета

        dist = sqrt(1 / 3.0)

        gluPerspective(90, 491 / 461, 0.1, 70.0)
        glTranslatef(0, 0, -6)

        gluLookAt(6, 6, 6, 0, 0, 0, 0, 1, 0)
        # gluLookAt(dist, dist, dist, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        glMatrixMode(GL_MODELVIEW)

        # Рисуем координатные оси
        glBegin(GL_LINES)

        glColor3d(1.0, 0.0, 0.0)
        glVertex3d(0.0, 0.0, 0.0)
        glVertex3d(3.0, 0.0, 0.0)

        glColor3d(0.0, 3.0, 0.0)
        glVertex3d(0.0, 0.0, 0.0)
        glVertex3d(0.0, 3.0, 0.0)

        glColor3d(0.0, 0.0, 1.0)
        glVertex3d(0.0, 0.0, 0.0)
        glVertex3d(0.0, 0.0, 3.0)

        # Ось до камеры
        glColor3d(0.5, 1.0, 0.5)
        glVertex3d(0.0, 0.0, 0.0)
        glVertex3d(dist + 6, dist + 6, dist + 6)

        glEnd()

        # Рисуем куб
        glColor3d(0, 1.0, 1.0)
        glColor3f(1, 1, 0)

        self.cube.determineVisibility()
        self.cube.draw_cube(flag, flag2)

        glFlush()
