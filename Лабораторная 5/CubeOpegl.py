from OpenGL import GL, GLU, GLUT
from PyQt5 import QtWidgets
from math import  sqrt
from random import random, uniform

verticies = [
    [0, 0, 0], # A
    [2, 0, 0], # B
    [2, 2, 0], # C
    [0, 2, 0], # D
    [2, 0, 2], # E
    [0, 0, 2], # F
    [0, 2, 2], # K
    [2, 2, 2] # J
    ]

anotherVerticies = [
    [-1, -1, -1], # A
    [1, 1, -1], # B
    [1, 1, -1], # C
    [-1, 1, -1], # D
    [1, -1, 1], # E
    [-1, -1, 1], # F
    [-1, 1, 1], # K
    [1, 1, 1] # J
    ]

edges = (
    (0, 1),
    (0, 3),
    (0, 5),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 5),
    (6, 7),
    (4, 5),
    (4, 1),
    (4, 7)
    )

surfaces = (
    (0,1,2,3),
    (2,3,7,6),
    (1,2,4,7),
    (1,0,4,5),
    (0,3,5,6),
    (4,5,6,7)
    )

oppositePoints = (
    (0, 2),
    (0, 6),
    (0, 4),
    (1, 7),
    (4, 6),
    (5, 7)
)

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

x0 = 0
y0 = 0
z0 = 0
x1 = 0
y1 = 0
z1 = 0


def Cube():

    GL.glBegin(GL.GL_LINES)
    for edge in edges:
        for vertex in edge:
            GL.glVertex3fv(verticies[vertex])
    GL.glEnd()


def anotherCube():
    GL.glBegin(GL.GL_LINES)
    for edge in edges:
        for vertex in edge:
            GL.glVertex3fv(anotherVerticies[vertex])
    GL.glEnd()

def separateBySurface(vert):
    result = []
    for i in range(len(oppositePoints)):
        xdiff = abs(vert[oppositePoints[i][0]][0] - vert[oppositePoints[i][1]][0])
        ydiff = abs(vert[oppositePoints[i][0]][1] - vert[oppositePoints[i][1]][1])
        zdiff = abs(vert[oppositePoints[i][0]][2] - vert[oppositePoints[i][1]][2])
        xmax = max(vert[oppositePoints[i][0]][0], vert[oppositePoints[i][1]][0])
        ymax = max(vert[oppositePoints[i][0]][1],  vert[oppositePoints[i][1]][1])
        zmax = max(vert[oppositePoints[i][0]][2], vert[oppositePoints[i][1]][2])

        xmin = min(vert[oppositePoints[i][0]][0], vert[oppositePoints[i][1]][0])
        ymin = min(vert[oppositePoints[i][0]][1],  vert[oppositePoints[i][1]][1])
        zmin = min(vert[oppositePoints[i][0]][2], vert[oppositePoints[i][1]][2])

        result.append(getSurfacePoints(xdiff, ydiff, zdiff, xmin, ymin, zmin, xmax, ymax, zmax))
    return result

def getSurfacePoints(xdiff, ydiff, zdiff, xorig, yorig, zorig, xmax, ymax, zmax):
    if xdiff == 0:
        points = []
        yy = [k / 100 for k in range(yorig, 100*ymax)]
        zz = [k / 100 for k in range(zorig, 100*zmax)]
        for y in yy:
            for z in zz:
                points.append([xorig, y, z])
    elif ydiff == 0:
        points = []
        xx = [k / 100 for k in range(xorig, 100*xmax)]
        zz = [k / 100 for k in range(zorig, 100*zmax)]
        for x in xx:
            for z in zz:
                points.append([x, yorig, z])
    elif zdiff == 0:
        points = []
        xx = [k / 100 for k in range(xorig, 100*xmax)]
        yy = [k / 100 for k in range(yorig, 100*ymax)]
        for x in xx:
            for y in yy:
                points.append([x, y, zorig])
    return points
    

z_buffer = {}
color_buffer = {}

# z_buffer_y = {}
# color_buffer_y = {}

# z_buffer_z = {}
# color_buffer_z = {}


def fillZ_buffer(surfacePoints):
    for surfacePoint in surfacePoints:
        for points in surfacePoints:
            r = uniform(0, 1)
            g = uniform(0, 1)
            b = uniform(0, 1)
            GL.glColor3f(r, g, b)
            GL.glBegin(GL.GL_POINTS)
            for point in points:
                GL.glVertex3d(point[0], point[1], point[2])
                
                if z_buffer.get(point[2]) != None and z_buffer.get(point[2]).get(point[1]) != None:
                    if z_buffer[point[2]][point[1]] < point[0]:
                        z_buffer[point[2]][point[1]] = point[0]
                        color_buffer[point[2]][point[1]] = [r, g, b]
                else:
                    if z_buffer.get(point[2]) == None:
                        z_buffer[point[2]] = {}
                        color_buffer[point[2]] = {}
                    z_buffer[point[2]][point[1]] = point[0]
                    color_buffer[point[2]][point[1]] = [r, g, b]
            GL.glEnd()



class OpenGLWidget(QtWidgets.QOpenGLWidget):

    def initializeGL(self):
        GL.glClearDepth(1.0)
        # GL.glDepthFunc(GL.GL_LESS)
        # GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()



    def paintGL(self):
        # Настройка камеры для изометрического вида
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()

        dist = sqrt(1 / 3.0)

        GLU.gluPerspective(90, 491/461, 0.1, 70.0)
        GL.glTranslatef(0, 0, -6)

        GLU.gluLookAt(dist, dist, dist, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        GL.glMatrixMode(GL.GL_MODELVIEW)

        # Рисуем координатные оси
        GL.glBegin(GL.GL_LINES)

        GL.glColor3d(1.0, 0.0, 0.0)
        GL.glVertex3d(0.0, 0.0, 0.0)
        GL.glVertex3d(3.0, 0.0, 0.0)

        GL.glColor3d(0.0, 3.0, 0.0)
        GL.glVertex3d(0.0, 0.0, 0.0)
        GL.glVertex3d(0.0, 3.0, 0.0)

        GL.glColor3d(0.0, 0.0, 1.0)
        GL.glVertex3d(0.0, 0.0, 0.0)
        GL.glVertex3d(0.0, 0.0, 3.0)

        GL.glEnd()

        # Рисуем куб
        GL.glColor3f(1,1,0)
        Cube()
        # Инициализация z-buffer
        
        sp = separateBySurface(verticies)
        sp1 = separateBySurface(anotherVerticies)
        
        fillZ_buffer(sp)
        fillZ_buffer(sp1)

        # points()
        flag = 1
        if flag ==1:
            

            GL.glBegin(GL.GL_POINTS)

            for x in z_buffer:
                for y in z_buffer[x]:
                    GL.glColor3f(color_buffer[x][y][0], color_buffer[x][y][1], color_buffer[x][y][2])
                    GL.glVertex3f(x, z_buffer[x][y], y)

            GL.glEnd()

        GL.glFlush()



class OpenGLWidget2d(QtWidgets.QOpenGLWidget):
    def initializeGL(self):
        GL.glClearColor(1, 1, 1 ,1)

    # def paintGL(self):
    #     GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    #     GL.glMatrixMode(GL.GL_PROJECTION)
    #     GL.glLoadIdentity()
    #     GL.glOrtho(0, 1, 0, 1, -1, 1)
    #     GL.glViewport(0, 0, 100, 100)

       
    #     GL.glBegin(GL.GL_POINTS)
        
    #     for x in z_buffer:
    #         for y in z_buffer[x]:
    #             GL.glColor3f(color_buffer[x][y][0], color_buffer[x][y][1], color_buffer[x][y][2])
    #             GL.glVertex2f(x, y)

    #     GL.glEnd()
    
