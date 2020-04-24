from OpenGL.GL import *
from random import random
from numpy import linalg

class Point():
    def __init__(self, x, y, z):
        self.x = x 
        self.y = y
        self.z = z

class Lines():
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Surfaces():
    def __init__(self, line1, line2, line3, line4, point1, point2, point3, point4):
        self.lines = [line1, line2, line3, line4]
        self.points = [point1, point2, point3, point4]
        self.visible = True

class Cube():
    def __init__(self):

        # a = Point(0, 0, 0) # 0
        # b = Point(2, 0, 0) # 1
        # c = Point(2, 2, 0) # 2
        # d = Point(0, 2, 0) # 3
        # e = Point(2, 0, 2) # 4
        # f = Point(0, 0, 2) # 5
        # k = Point(0, 2, 2) # 6
        # j = Point(2, 2, 2) # 7


        a = Point(1, 1, 1) # 0
        b = Point(3, 1, 1) # 1
        c = Point(3, 3, 1) # 2
        d = Point(1, 3, 1) # 3
        e = Point(3, 1, 3) # 4
        f = Point(1, 1, 3) # 5
        k = Point(1, 3, 3) # 6
        j = Point(3, 3, 3) # 7
        
        self.verticies = [a, b, c, d, e, f, k, j]

        self.eternalPoint = Point(2, 2, 2)
        self.cameraPoint = Point(7, 7, 7)

        line1 = Lines(a, b) # 0
        line2 = Lines(a, d) # 1 
        line3 = Lines(a, f) # 2
        line4 = Lines(c, b) # 3
        line5 = Lines(c, d) # 4
        line6 = Lines(c, j) # 5
        line7 = Lines(k, d) # 6
        line8 = Lines(k, f) # 7
        line9 = Lines(k, j) # 8
        line10 = Lines(e, f) # 9
        line11 = Lines(e, b) # 10
        line12 = Lines(e, j) # 11
        

        self.Lines = [
            line1,
            line2,
            line3,
            line4,
            line5,
            line6,
            line7,
            line8,
            line9,
            line10,
            line11,
            line12
        ]
        
        self.surfaces = [
            Surfaces(line1, line6, line3, line7, a, f, k, d),
            Surfaces(line6, line7, line9, line5, k, d, c, j),
            Surfaces(line6, line4, line12, line11, e, b, c, j),

            Surfaces(line1, line3, line11, line10, a, b, e, f),
            Surfaces(line1, line2, line5, line4, a, b, c, d),
            Surfaces(line10, line12, line8, line9, e, f, k, j), 
        ]
      

    
    def draw_cube(self, flag, flag2):
        if flag == True:
            glBegin(GL_QUADS)
            for surface in self.surfaces: 
                if surface.visible or flag2 == False:
                    glColor3f(random(), random(), random())
                    for point in surface.points:
                        glVertex3d(point.x, point.y, point.z)
            glEnd()
        else:  
            for surface in self.surfaces:
                glBegin(GL_LINES)
                if surface.visible or flag2 == False:
                    # glColor3f(random(), random(), random())
                    for line in surface.lines:
                        glVertex3d(line.start.x, line.start.y, line.start.z)
                        glVertex3d(line.end.x, line.end.y, line.end.z)
                glEnd()



    def determineVisibility(self):
        for surface in self.surfaces:
            line1 = surface.lines[0]
            line2 = surface.lines[1]

            point1 = line1.start
            point2 = line1.end
            point3 = line2.end
            
            x1 = point1.y
            y1 = point1.z
            z1 = point1.x

            x2 = point2.y
            y2 = point2.z
            z2 = point2.x

            x3 = point3.y
            y3 = point3.z
            z3 = point3.x

            matrixStart = [
                [self.eternalPoint.x - point1.x, self.eternalPoint.y - point1.y, self.eternalPoint.z - point1.z],
                [point2.x - point1.x, point2.y - point1.y, point2.z - point1.z],
                [point3.x - point1.x, point3.y - point1.y, point3.z - point1.z]
            ]

            matrixCamera =  [
                [self.cameraPoint.x - point1.x, self.cameraPoint.y - point1.y, self.cameraPoint.z - point1.z],
                [point2.x - point1.x, point2.y - point1.y, point2.z - point1.z],
                [point3.x - point1.x, point3.y - point1.y, point3.z - point1.z]
            ]

            detStart = linalg.det(matrixStart)
            detCamera = linalg.det(matrixCamera)

            if detStart*detCamera >= 0:
                surface.visible = False


