import sys
from OpenGL import GL, GLU
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import design
import math
from numpy import matmul
import openglwidget as mygl
import random

class App(QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.openGLWidget

        self.rotateXButton.clicked.connect(self.rotateXPushed)
        self.rotateYButton.clicked.connect(self.rotateYPushed)
        self.setButton.clicked.connect(self.setPushed)
        self.randomButton.clicked.connect(self.randomPushed)

        self.tableWidget.setRowCount(len(mygl.xyzs)*4)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['x', 'y', 'z'])
        self.tableWidget.setVerticalHeaderLabels(['P'+str(i+1) for i in range(len(mygl.xyzs)*4)])

        k, l = 0, 0
        for i in range(self.tableWidget.rowCount()):
            if k % 4 == 0 and k != 0:
                k = 0
            if l % 4 == 0 and l != 0:
                l = 0

            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(mygl.xyzs[k][l][0])))
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(mygl.xyzs[k][l][1])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(mygl.xyzs[k][l][2])))
            k += 1
            l += 1
        self.tableWidget.resizeColumnsToContents()

    @pyqtSlot()
    def rotateXPushed(self):
        teta = float(self.angleXlineEdit.text())
        teta = teta * math.pi / 180

        # Находим нормализированный вектор
        sqrtSum = math.sqrt((0 - 0)**2 + (0- 0)**2 + (3 - 0)**2)
        normX = (0 - 0) / sqrtSum
        normY = (0 - 0) / sqrtSum
        normZ = (3 - 0) / sqrtSum

        # Создаём матрицу
        rotate = []
        rotate.append([])
        rotate[0].append(math.cos(teta) + normX**2*(1-math.cos(teta)))
        rotate[0].append(normX*normY*(1 - math.cos(teta)) - normZ*math.sin(teta))
        rotate[0].append(normX*normZ*(1 - math.cos(teta)) + normY*math.sin(teta))
        rotate.append([])
        rotate[1].append(normY*normX*(1 - math.cos(teta)) + normZ*math.sin(teta))
        rotate[1].append(math.cos(teta) + normY**2*(1 - math.cos(teta)))
        rotate[1].append(normY*normZ*(1-math.cos(teta)) - normX*math.sin(teta))
        rotate.append([])
        rotate[2].append(normZ*normX*(1-math.cos(teta)) - normY*math.sin(teta))
        rotate[2].append(normZ*normY*(1 - math.cos(teta)) + normX*math.sin(teta))
        rotate[2].append(math.cos(teta) + normZ**2*(1-math.cos(teta)))

        for i in range(len(mygl.xyzs)):
            mygl.xyzs[i] = matmul(mygl.xyzs[i], rotate)

        self.openGLWidget.update()

    @pyqtSlot()
    def rotateYPushed(self):
        teta = float(self.angleXlineEdit.text())
        teta = teta * math.pi / 180

        # Находим нормализированный вектор
        sqrtSum = math.sqrt((3 - 0) ** 2 + (0 - 0) ** 2 + (0 - 0) ** 2)
        normX = (3 - 0) / sqrtSum
        normY = (0 - 0) / sqrtSum
        normZ = (0 - 0) / sqrtSum

        # Создаём матрицу
        rotate = []
        rotate.append([])
        rotate[0].append(math.cos(teta) + normX ** 2 * (1 - math.cos(teta)))
        rotate[0].append(normX * normY * (1 - math.cos(teta)) - normZ * math.sin(teta))
        rotate[0].append(normX * normZ * (1 - math.cos(teta)) + normY * math.sin(teta))
        rotate.append([])
        rotate[1].append(normY * normX * (1 - math.cos(teta)) + normZ * math.sin(teta))
        rotate[1].append(math.cos(teta) + normY ** 2 * (1 - math.cos(teta)))
        rotate[1].append(normY * normZ * (1 - math.cos(teta)) - normX * math.sin(teta))
        rotate.append([])
        rotate[2].append(normZ * normX * (1 - math.cos(teta)) - normY * math.sin(teta))
        rotate[2].append(normZ * normY * (1 - math.cos(teta)) + normX * math.sin(teta))
        rotate[2].append(math.cos(teta) + normZ ** 2 * (1 - math.cos(teta)))

        for i in range(len(mygl.xyzs)):
            mygl.xyzs[i] = matmul(mygl.xyzs[i], rotate)
        
        self.openGLWidget.update()

    @pyqtSlot()
    def setPushed(self):
        k, l = 0, 0
        for i in range(self.tableWidget.rowCount()):
            if k % 4 == 0 and k != 0:
                k = 0
            if l % 4 == 0 and l != 0:
                l = 0
            mygl.xyzs[k][l][0] = float(self.tableWidget.item(i, 2).text())
            mygl.xyzs[k][l][1] = float(self.tableWidget.item(i, 0).text())
            mygl.xyzs[k][l][2] = float(self.tableWidget.item(i, 1).text())
            k += 1
            l += 1
        self.openGLWidget.update()

    def randomPushed(self):
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(random.randint(-15, 15))))
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(random.randint(-15, 15))))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(random.randint(-15, 15))))
        self.tableWidget.resizeColumnsToContents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())