import design
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPainter, QColor, QBrush
from lab4 import *
from pyqtgraph import PlotWidget, plot, mkPen, mkColor
import pyqtgraph as pg

import sys


class App(QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        # self.dotsButton.clicked.connect(self.dotsPushed)
        # self.bezierButton.clicked.connect(self.bezierPushed)

        self.pushButton.clicked.connect(self.buttonPushed)
        self.linesTableButton.clicked.connect(self.lines_button_pushed)
        self.sectionButton.clicked.connect(self.section_pushed)

        self.graphicsView.setBackground('w')
        self.lines = []
        self.foundLines = []
        self.window = []

        self.rectXLeft.setText(str(10))
        self.rectYLeft.setText(str(20))
        self.widthEdit.setText(str(10))
        self.lengthEdit.setText(str(10))

    @pyqtSlot()
    def lines_button_pushed(self):
        try:
            n = int(self.linesEdit.text())
            if n < 0:
                raise ValueError
        except ValueError:
            self.lines.clear()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Неправильно введено число точек')
            msg.setWindowTitle("Ошибка")
            msg.exec_()
            return

        self.tableWidget.setRowCount(n)
        self.tableWidget.setColumnCount(4)
        # self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setHorizontalHeaderLabels(['x1', 'y1', 'x2', 'y2'])
        self.tableWidget.setVerticalHeaderLabels(['P'+str(i+1) for i in range(n)])

    @pyqtSlot()
    def buttonPushed(self):
        self.lines.clear()
        try:
            for i in range(self.tableWidget.rowCount()):
                self.lines.append([[float(self.tableWidget.item(i,0).text()),
                                    float(self.tableWidget.item(i,1).text())],
                                   [float(self.tableWidget.item(i,2).text()),
                                    float(self.tableWidget.item(i,3).text())]])
        except Exception:
            self.lines.clear()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Неправильно введены координаты точек')
            msg.setWindowTitle("Ошибка")
            msg.exec_()
            return

        try:
            x = float(self.rectXLeft.text())
            y = float(self.rectYLeft.text())
            length = float(self.lengthEdit.text())
            width = float(self.widthEdit.text())

            self.window = [x, x + width, y, y - length]
        except Exception:
            self.lines.clear()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Неправильно введены координаты точек')
            msg.setWindowTitle("Ошибка")
            msg.exec_()
            return
        #self.lines = [[[15, 15], [15, 5]]]
        # Window
        # First = Xleft, Second = Xright
        # Third = Yup, Fourth = Ydown
        self.drawScene()

    def drawScene(self, linesPen=mkPen('k')):
        self.graphicsView.clear()
        pen = mkPen('r')
        # Up
        self.graphicsView.plot([self.window[0], self.window[1]], [self.window[2], self.window[2]], pen=pen)
        # Down
        self.graphicsView.plot([self.window[0], self.window[1]], [self.window[3], self.window[3]], pen=pen)
        # Left
        self.graphicsView.plot([self.window[0], self.window[0]], [self.window[2], self.window[3]], pen=pen)
        # Right
        self.graphicsView.plot([self.window[1], self.window[1]], [self.window[2], self.window[3]], pen=pen)

        # Draw lines
        for line in self.lines:
            self.graphicsView.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], pen=mkPen('k'))


    def section_pushed(self):
        self.foundLines = midPoint(self.lines, self.window, 0.1)
        self.drawNewLines()

    def drawNewLines(self):
        # Draw lines
        for line in self.foundLines:
            self.graphicsView.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], pen=mkPen('g'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())