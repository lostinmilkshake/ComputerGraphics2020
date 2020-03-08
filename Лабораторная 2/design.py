# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(610, 40, 160, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.numberEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.numberEdit.setObjectName("numberEdit")
        self.verticalLayout.addWidget(self.numberEdit)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(610, 140, 171, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.dotsButton = QtWidgets.QPushButton(self.centralwidget)
        self.dotsButton.setGeometry(QtCore.QRect(610, 110, 150, 23))
        self.dotsButton.setObjectName("dotsButton")
        self.bezierButton = QtWidgets.QPushButton(self.centralwidget)
        self.bezierButton.setGeometry(QtCore.QRect(610, 530, 150, 23))
        self.bezierButton.setObjectName("bezierButton")
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 50, 561, 451))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Кривые Безье"))
        self.label.setText(_translate("MainWindow", "Введите количество точек"))
        self.dotsButton.setText(_translate("MainWindow", "Продолжить"))
        self.bezierButton.setText(_translate("MainWindow", "Построить"))

