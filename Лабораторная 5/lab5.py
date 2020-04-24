import sys
from OpenGL import GL, GLU
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import design
import math
from numpy import matmul
import openglwidget

class App(QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.openGLWidget

        self.edgesCheckBox.stateChanged.connect(self.change)
        self.visibilityCheckBox.stateChanged.connect(self.change) 
    
    def change(self):
        if self.edgesCheckBox.isChecked():
            openglwidget.flag = True
        else:
            openglwidget.flag = False

        if self.visibilityCheckBox.isChecked():
            openglwidget.flag2 = True
        else:
            openglwidget.flag2 = False

        self.openGLWidget.update()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())