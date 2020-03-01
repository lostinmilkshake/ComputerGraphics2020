import sys
from OpenGL import GL, GLU
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import design
import CubeOpegl
import math
from numpy import matmul



class App(QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_click)
        self.openGLWidget
        #self.angleSlider.valueChanged.connect(self.rotateAngle)
        self.pushButton.setText("Повернуть")
    
        
    def rotateAngle(self):
        # Считывание угла поворота
        teta = self.angleSlider.value()
        self.angleText.setText("Угол поворота: " + str(teta)) 
        

    @pyqtSlot()
    def on_click(self):
        # Обозначаем координаты оси поворота
        try:
            CubeOpegl.x0 = float(self.x0Coor.text())
            CubeOpegl.y0 = float(self.y0Coor.text())
            CubeOpegl.z0 = float(self.z0Coor.text())
            CubeOpegl.x1 = float(self.x1Coor.text())
            CubeOpegl.y1 = float(self.y1Coor.text())
            CubeOpegl.z1 = float(self.z1Coor.text())
            teta = (int(self.angleSlider.text()) * math.pi) / 180
            
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Неправильно введены координаты оси')
            msg.setWindowTitle("Ошибка")
            msg.exec_()
            return

        # Находим нормализированный вектор
        sqrtSum = math.sqrt((CubeOpegl.x1 - CubeOpegl.x0)**2 + (CubeOpegl.y1 - CubeOpegl.y0)**2 + (CubeOpegl.z1 - CubeOpegl.z0)**2)
        normX = (CubeOpegl.x1 - CubeOpegl.x0) / sqrtSum
        normY = (CubeOpegl.y1 - CubeOpegl.y0) / sqrtSum
        normZ = (CubeOpegl.z1 - CubeOpegl.z0) / sqrtSum
        
        
        #teta = 90
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

        # Меняем значения куба
        CubeOpegl.prevVerticies = CubeOpegl.verticies
        CubeOpegl.verticies = matmul(CubeOpegl.verticies, rotate)

        self.openGLWidget.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())