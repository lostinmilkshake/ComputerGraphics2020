import math



def pointToCode(point, window):
    T = []
    T.append(1 if point[0] < window[0] else 0)
    T.append(1 if point[0] > window[1] else 0)
    T.append(1 if point[1] < window[3] else 0)
    T.append(1 if point[1] > window[2] else 0)
    return T


def log_prod(code1, code2):
    p = 0
    for i in range(4):
        p += code1[i] & code2[i]

    return p


def is_visible(bar, rect):
    """Видимость - 0 = невидимый
                   1 = видимый
                   2 = частично видимый"""
    # вычисление кодов концевых точек отрезка
    s1 = sum(pointToCode(bar[0], rect))
    s2 = sum(pointToCode(bar[1], rect))

    # предположим, что отрезок частично видим
    vis = 2

    # проверка полной видимости отрезка
    if not s1 and not s2:
        vis = 1
    else:
        # проверка тривиальной невидимости отрезка
        l = log_prod(pointToCode(bar[0], rect), pointToCode(bar[1], rect))
        if l != 0:
            vis = 0

    return vis


def midPoint(lines, rect, tol):
    result = []
    for line in lines:

        if line[0][0] >= line[1][0]:
            tempX = line[0][0]
            tempY = line[0][1]
            line[0][0] = line[1][0]
            line[0][1] = line[1][1]
            line[1][0] = tempX
            line[1][1] = tempY

        s1 = sum(pointToCode(line[0], rect))
        s2 = sum(pointToCode(line[1], rect))

        p = log_prod(pointToCode(line[0], rect), pointToCode(line[1], rect))

        if s1 == 0 and s2 == 0:
            result.append(line)
            # break
        elif p != 0:
            break
        elif s1!=0 and s2!=0:
            tempX1 = line[0][0]
            tempY1 = line[0][1]
            tempX2 = line[1][0]
            tempY2 = line[1][1]

            leftBorder = find_left_border(line, rect, tol)
            rightBorder = find_right_border([[tempX1, tempY1], [tempX2, tempY2]], rect, tol)

            line[0][0] = leftBorder[0][0]
            line[0][1] = leftBorder[0][1]
            line[1][0] = rightBorder[1][0]
            line[1][1] = rightBorder[1][1]

            result.append(line)
        elif s1==0:
            tempX = line[0][0]
            tempY = line[0][1]

            border = find_left_border(line, rect, tol)

            line[0][0] = tempX
            line[0][1] = tempY
            line[1][0] = border[1][0]
            line[1][1] = border[1][1]
            result.append(line)
        elif s2==0:
            tempX = line[1][0]
            tempY = line[1][1]

            border = find_right_border(line, rect, tol)

            line[1][0] = tempX
            line[1][1] = tempY
            line[0][0] = border[0][0]
            line[0][1] = border[0][1]
            result.append(line)

    return result


def find_left_border(line, rect, tol):
    while math.sqrt((line[1][0] - line[0][0]) ** 2 + (line[1][1] - line[0][1]) ** 2) > tol:
        midLine = [(line[0][0] + line[1][0]) / 2, (line[0][1] + line[1][1]) / 2]
        temp = line[0]
        line[0] = midLine
        p = log_prod(pointToCode(line[0], rect), pointToCode(line[1], rect))
        if p != 0:
            line[0] = temp
            line[1] = midLine
    return line

def find_right_border(line, rect, tol):
    while math.sqrt((line[1][0] - line[0][0]) ** 2 + (line[1][1] - line[0][1]) ** 2) > tol:
        midLine = [(line[0][0] + line[1][0]) / 2, (line[0][1] + line[1][1]) / 2]
        temp = line[1]
        line[1] = midLine
        p = log_prod(pointToCode(line[0], rect), pointToCode(line[1], rect))
        if p != 0:
            line[1] = temp
            line[0] = midLine

    return  line