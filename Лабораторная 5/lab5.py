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
        self.openGLWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())