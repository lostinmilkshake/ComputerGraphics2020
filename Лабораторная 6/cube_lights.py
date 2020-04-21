from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt5 import  QtWidgets
import math
from numpy import matmul

window = 0

faces = [[[0, 0, 2], [2, 0, 2], [2, 2, 2], [0, 2, 2]], 
         [[0, 0, 2], [0, 2, 2], [0, 2, 0], [0, 0, 0]],
         [[0, 0, 0], [0, 2, 0], [2, 2, 0], [2, 0, 0]],
         [[2, 0, 0], [2, 2, 0], [2, 2, 2], [2, 0, 2]],
         [[2, 0, 0], [2, 0, 2], [0, 0, 2], [0, 0, 0]],
         [[2, 2, 2], [2, 2, 0], [0, 2, 0], [0, 2, 2]]]

eye = (6, 6, 6)

lightPosition = (4.0, 5.0, 5.0, 1.0)
lightColor = (1.0, 1.0, 1.0, 1.0)

point = [0, 0, 0]

ambient = (0.5, 0.5, 0.5, 1)


def getCanonicalForm(pointOne, pointTwo, pointThree):  
    x1 = pointOne[0]
    y1 = pointOne[1]
    z1 = pointOne[2]

    x2 = pointTwo[0]
    y2 = pointTwo[1]
    z2 = pointTwo[2]

    x3 = pointThree[0]
    y3 = pointThree[1]
    z3 = pointThree[2]

    result = [0, 0, 0, 0] 
    result[0] = (y2-y1)*(z3-z1)-(z2-z1)*(y3-y1)
    result[1] = -((x2-x1)*(z3-z1)-(z2-z1)*(x3-x1))
    result[2] = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
    result[3] = -x1*result[0] - y1*result[1] - z1*result[2]

    return result


def getPointInside():
    global point
    count = 0
    for face in faces:
        count += len(face)
        temp = list(zip(*face))
        for i in range(3):
            point[i] += sum(temp[i])
    point = [element/count for element in point]


def getT(plane, pointOne, pointTwo):

    a = plane[0]
    b = plane[1]
    c = plane[2]
    d = plane[3]

    x1 = pointOne[0]
    y1 = pointOne[1]
    z1 = pointOne[2]

    x2 = pointTwo[0]
    y2 = pointTwo[1]
    z2 = pointTwo[2]

    t = (-d-a*x1-b*y1-c*z1)/(a*(x2-x1)+b*(y2-y1)+c*(z2-z1))

    return t


def initFigure():
    global faces, point, eye
    glLineWidth(2)
    for face in faces:
        cannonicalFrom = getCanonicalForm(face[0], face[1], face[2])
        t = getT(cannonicalFrom, point, eye)
        if 0 <= t <= 1:
            glBegin(GL_POLYGON)
            glNormal3f(cannonicalFrom[0], cannonicalFrom[1], cannonicalFrom[2])  
            for vertex in face:
                glVertex3dv(vertex)
            glEnd()



class CubeLightsWidget(QtWidgets.QOpenGLWidget):
    def initializeGL(self):
        self.initGL(800, 800)

    def initGL(self, Width, Height):
        glClearColor(1, 0, 1, 1.0)  # Цвет фона
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

        glEnable(GL_CULL_FACE)  
        glEnable(GL_LIGHTING)  
        glEnable(GL_LIGHT0)  
        glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)  
        glEnable(GL_NORMALIZE)  

    def paintGL(self):
        global ambient, lightPosition, lightColor
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient) 

        glLoadIdentity()

        gluLookAt(eye[0], eye[1], eye[2], 0, 0, 0, 0, 1, 0)


        glLightfv(GL_LIGHT0, GL_POSITION, lightPosition)  
        glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, (0.0, 0.0, 1.0)) 
        glLightfv(GL_LIGHT0, GL_SPECULAR, (0.0, 0.0, 0.0, 1.0))  
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightColor)  


        glMaterialfv(GL_FRONT, GL_DIFFUSE, lightColor) 
        glMaterialfv(GL_FRONT, GL_AMBIENT, (0.7, 0.7, 0.7, 1.0))  

        initFigure()

        glPointSize(5)
        glBegin(GL_POINTS)
        glColor3d(0,1,1)
        glVertex3d(lightPosition[0], lightPosition[1], lightPosition[2])
        glEnd()
