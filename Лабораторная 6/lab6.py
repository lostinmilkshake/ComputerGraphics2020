import sys
from OpenGL import GL, GLU
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import design
import math
from numpy import matmul
import  cube_lights

class App(QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.cameraButton.clicked.connect(self.cameraButtonClicked)
        self.lightButton.clicked.connect(self.lightButtonClicked)

    def cameraButtonClicked(self):
        try:
            x = float(self.xCameraLine.text())
            y = float(self.yCameraLine.text())
            z = float(self.zCameraLine.text())
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Неправильно введены координаты камеры')
            msg.setWindowTitle("Ошибка")
            msg.exec_()
            return
        cube_lights.eye = (x, y, z)
        self.openGLWidget.update()

    def lightButtonClicked(self):
        try:
            x = float(self.xLightLine.text())
            y = float(self.yLightLine.text())
            z = float(self.zLightLine.text())
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Неправильно введены координаты света')
            msg.setWindowTitle("Ошибка")
            msg.exec_()
            return

        cube_lights.lightPosition = (x, y, z, 1)
        self.openGLWidget.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
