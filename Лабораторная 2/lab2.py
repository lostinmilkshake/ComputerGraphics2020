import design
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPainter, QColor, QBrush
from make_bez import *
from pyqtgraph import PlotWidget, plot, mkPen, mkColor
import pyqtgraph as pg

import sys

class App(QMainWindow, design.Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.dotsButton.clicked.connect(self.dotsPushed)
        self.bezierButton.clicked.connect(self.bezierPushed)

        self.graphicsView.setBackground('w')
        self.xys = []
    
    # def paintEvent(self, e):

    #     qp = QPainter()
    #     qp.begin(self)
    #     self.drawBezier(qp)
    #     qp.end()

        
    def drawBezier(self):
        if (len(self.xys)) > 0:
            ts = [t/100.0 for t in range(101)]
            
            bezier = make_bezier(self.xys)
            points = bezier(ts)

            self.graphicsView.clear()
            pen = mkPen('r')
            self.graphicsView.plot([first[0] for first in points], [first[1] for first in points], pen=pen)
            pen = mkPen('b')
            self.graphicsView.plot([first[0] for first in self.xys], [first[1] for first in self.xys], pen=pen)

    
    @pyqtSlot()
    def dotsPushed(self):
        try:
            n = int(self.numberEdit.text())
        except ValueError:
            self.xys.clear()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Неправильно введено число точек')
            msg.setWindowTitle("Ошибка")
            msg.exec_()
            return
        self.tableWidget.setRowCount(n)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setHorizontalHeaderLabels(['x', 'y'])
        self.tableWidget.setVerticalHeaderLabels(['P'+str(i+1) for i in range(n)])

    @pyqtSlot()
    def bezierPushed(self):
        self.xys.clear()
        try:
            for i in range(self.tableWidget.rowCount()):
                self.xys.append((float(self.tableWidget.item(i,0).text()), float(self.tableWidget.item(i,1).text())))
        except ValueError:
            self.xys.clear()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Неправильно введены координаты точек')
            msg.setWindowTitle("Ошибка")
            msg.exec_()
            return
        self.drawBezier()

        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())