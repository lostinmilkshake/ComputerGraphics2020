from math import factorial

class Make_bez:
    def __init__(self, points):
        self.points = points
        self.n = len(points) - 1

    def bezierSurface(self, us, vs):
        result = [[0 for i in range(len(us))] for i in range(len(vs))]
        #result = []
        for u in us:
            #resultX = []
            for v in vs:
                sumX = 0
                sumY = 0
                sumZ = 0
                for i in range(self.n+1):
                    # Finding bernstein for u point
                    binomialU = factorial(self.n) / (factorial(i)*factorial(self.n-i))
                    bernsteinU = binomialU * u**i * (1 - u)**(self.n-i)
                    for j in range(self.n+1):
                        # Finding bernstein for v point
                        binomialV =  factorial(self.n) / (factorial(j)*factorial(self.n-j))
                        bernsteinV = binomialV * v**j * (1 - v)**(self.n-j)
                        # Changing x point
                        sumX += self.points[i][j][0] * bernsteinU * bernsteinV
                        # Changing y point
                        sumY += self.points[i][j][1] * bernsteinU * bernsteinV
                        # Changing z point
                        sumZ += self.points[i][j][2] * bernsteinU * bernsteinV
                result[round(u*(len(us)-1))][round(v*(len(vs)-1))] = [sumX, sumY, sumZ]
                #result.append([sumX, sumY, sumZ])
        return result

