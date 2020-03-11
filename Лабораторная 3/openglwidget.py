from OpenGL import GL, GLU
from PyQt5 import QtWidgets
from bez2ElectircBoogaloo import *

# xyzs = [
#     [
#         [-5, -3, 24],
#         [1, 5, 16],
#         [-5, 11, 5],
#         [0, 19, 1]
#     ],
#     [
#         [7, -1, 9],
#         [3, 3, 3],
#         [5, 13, 11],
#         [6, 21, 17]
#     ],
#     [
#         [13, -3, 28],
#         [12, 9, 14],
#         [14, 16, 16],
#         [11, 21, 29]
#     ],
#     [
#         [22, -2, 19],
#         [20, 7, 19],
#         [20, 13, 28],
#         [23, 25, 23]
#     ],
# ]

xyzs = [
    [
        [-15, 0, 15],
        [-15, 5, 5],
        [-15, 5, -5],
        [-15, 0, -15]
    ],
    [
        [-5, 5, 15],
        [-5, 5, 5],
        [-5, 5, -5],
        [-5, 5, -15]
    ],
    [
        [5, 5, 15],
        [5, 5, 5],
        [5, 5, -5],
        [5, 5, -15]
    ],
    [
        [15, 0, 15],
        [15, 5, 5],
        [15, 5, -5],
        [15, 0, -15]
    ],
]



class OpenGLWidget(QtWidgets.QOpenGLWidget):

    def initializeGL(self):
        GL.glClearDepth(1.0)
        GL.glDepthFunc(GL.GL_LESS)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GLU.gluPerspective(45, 800/600, 0.1, 400.0)
        GL.glTranslatef(-3.0, -3.0, -80)
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glEnable(GL.GL_COLOR_MATERIAL)

    def paintGL(self):
        myBez = Make_bez(xyzs)
        us = [i / 100 for i in range(0, 101, 4)]
        vs = [i / 100 for i in range(0, 101, 4)]

        bezierPoints = myBez.bezierSurface(us, vs)

        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glLoadIdentity()
        GLU.gluLookAt(1, 1, 3, -2.5, 0, -3,0,1.5,0)
        GL.glColor3f(1,1,1)

        # Рисуем оси
        GL.glBegin(GL.GL_LINES)
        GL.glVertex3f(0, 0, 0)
        GL.glVertex3f(0, 0, 40)
        GL.glEnd()
        GL.glBegin(GL.GL_LINES)
        GL.glVertex3f(0, 0, 0)
        GL.glVertex3f(40, 0, 0)
        GL.glEnd()
        GL.glBegin(GL.GL_LINES)
        GL.glVertex3f(0, 0, 0)
        GL.glVertex3f(0, 40, 0)
        GL.glEnd()

        # Рисуем горизонтальные линии многоугольника
        GL.glColor(1, 0, 0)
        GL.glBegin(GL.GL_LINE_STRIP)
        for i in range(len(xyzs)):
            for j in range(len(xyzs)):
                GL.glVertex3f(xyzs[i][j][0], xyzs[i][j][1], xyzs[i][j][2])
        GL.glEnd()
        # Рисуем вертикальные линии многоугольника
        GL.glBegin(GL.GL_LINE_STRIP)
        for i in range(len(xyzs)):
            for j in range(len(xyzs)):
                GL.glVertex3f(xyzs[j][i][0], xyzs[j][i][1], xyzs[j][i][2])
        GL.glEnd()

        # Рисуем горизонтальные линии поверхности Безье
        GL.glColor(0, 1, 0)
        GL.glBegin(GL.GL_LINE_STRIP)
        for i in range(len(bezierPoints)):
            for j in range(len(bezierPoints)):
                if bezierPoints[i][j] == 0:
                    continue
                GL.glVertex3f(bezierPoints[i][j][0], bezierPoints[i][j][1], bezierPoints[i][j][2])
        GL.glEnd()
        # Рисуем вертикальные линии поверхности Безье
        GL.glBegin(GL.GL_LINE_STRIP)
        for i in range(len(bezierPoints)):
            for j in range(len(bezierPoints)):
                GL.glVertex3f(bezierPoints[j][i][0], bezierPoints[j][i][1], bezierPoints[j][i][2])
        GL.glEnd()
