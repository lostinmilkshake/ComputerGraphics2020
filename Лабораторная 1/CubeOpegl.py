from OpenGL import GL, GLU
from PyQt5 import QtWidgets


'''verticies = [
    [2, 0, 0],
    [2, 2, 0],
    [0, 2, 0],
    [0, 0, 0],
    [2, 0, 2],
    [2, 2, 2],
    [0, 0, 2],
    [0, 2, 2]
    ]

prevVerticies = [
    [2, 0, 0],
    [2, 2, 0],
    [0, 2, 0],
    [0, 0, 0],
    [2, 0, 2],
    [2, 2, 2],
    [0, 0, 2],
    [0, 2, 2]
    ]'''

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

prevVerticies = [
    [0, 0, 0], # A
    [2, 0, 0], # B
    [2, 2, 0], # C
    [0, 2, 0], # D
    [2, 0, 2], # E
    [0, 0, 2], # F
    [0, 2, 2], # K
    [2, 2, 2] # J
    ]

'''edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
    )'''
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

def prevCube():
    GL.glBegin(GL.GL_LINES)
    for edge in edges:
        for vertex in edge:
            GL.glVertex3fv(prevVerticies[vertex])
    GL.glEnd()

class OpenGLWidget(QtWidgets.QOpenGLWidget):

    def initializeGL(self):
        GL.glClearDepth(1.0)
        GL.glDepthFunc(GL.GL_LESS)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GLU.gluPerspective(45, 641/541, 0.1, 80.0)
        GL.glTranslatef(-1.0, -1.0, -7)
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glEnable(GL.GL_COLOR_MATERIAL)

    def paintGL(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT) 
        GL.glLoadIdentity()
        GLU.gluLookAt(1, 1, 3, -2.5, 0, -3,0,1.5,0)
        GL.glColor3f(1,1,1)
        # Рисуем оси
        GL.glBegin(GL.GL_LINES)
        GL.glVertex3f(0, 0, 0)
        GL.glVertex3f(0, 0, 3)
        GL.glEnd()
        GL.glBegin(GL.GL_LINES)
        GL.glVertex3f(0, 0, 0)
        GL.glVertex3f(3, 0, 0)
        GL.glEnd()
        GL.glBegin(GL.GL_LINES)
        GL.glVertex3f(0, 0, 0)
        GL.glVertex3f(0, 3, 0)
        GL.glEnd()
        # Рисуем предыдущий куб
        prevCube()
        # Рисуем куб
        GL.glColor3f(1,0,0)
        Cube()
        # Рисуем вектор, вокруг которого поворачиваемся
        GL.glColor3f(0,1,0)
        GL.glBegin(GL.GL_LINES)
        GL.glVertex3f(x0, y0, z0)
        GL.glVertex3f(x1, y1, z1)
        GL.glEnd()