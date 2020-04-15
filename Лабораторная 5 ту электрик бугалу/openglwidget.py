from PyQt5 import QtWidgets
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sqrt
from cube import *

flag = False
flag2 = False

class OpenGLWidget(QtWidgets.QOpenGLWidget):


    def initializeGL(self):
        glClearDepth(1.0)
        # glDepthFunc(GL_LESS)
        # glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        self.cube = Cube()




    def paintGL(self):
        # Настройка камеры для изометрического вида
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        dist = sqrt(1 / 3.0)

        gluPerspective(90, 491/461, 0.1, 70.0)
        glTranslatef(0, 0, -6)

        gluLookAt(dist, dist, dist, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
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
        glVertex3d(dist+6, dist+6, dist+6)

        glEnd()

        # Рисуем куб
        glColor3d(0, 1.0, 1.0)
        glColor3f(1,1,0)
        
        self.cube.determineVisibility()
        self.cube.draw_cube(flag, flag2)
        

        glFlush()