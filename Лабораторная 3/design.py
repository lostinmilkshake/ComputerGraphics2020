# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openGLWidget = OpenGLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(10, 0, 800, 600))
        self.openGLWidget.setMinimumSize(QtCore.QSize(581, 461))
        self.openGLWidget.setObjectName("openGLWidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(820, 0, 481, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(830, 360, 492, 84))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.angleYlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.angleYlineEdit.setObjectName("angleYlineEdit")
        self.gridLayout.addWidget(self.angleYlineEdit, 1, 1, 1, 1)
        self.angleXlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.angleXlineEdit.setObjectName("angleXlineEdit")
        self.gridLayout.addWidget(self.angleXlineEdit, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.rotateXButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.rotateXButton.setObjectName("rotateXButton")
        self.gridLayout.addWidget(self.rotateXButton, 2, 0, 1, 1)
        self.rotateYButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.rotateYButton.setObjectName("rotateYButton")
        self.gridLayout.addWidget(self.rotateYButton, 2, 1, 1, 1)
        self.setButton = QtWidgets.QPushButton(self.centralwidget)
        self.setButton.setGeometry(QtCore.QRect(810, 310, 245, 32))
        self.setButton.setObjectName("setButton")
        self.randomButton = QtWidgets.QPushButton(self.centralwidget)
        self.randomButton.setGeometry(QtCore.QRect(1070, 310, 245, 32))
        self.randomButton.setObjectName("randomButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Введите угол поворота вокруг оси X"))
        self.label_2.setText(_translate("MainWindow", "Введите угол поворота вокруг оси Y"))
        self.rotateXButton.setText(_translate("MainWindow", "Повернуть по X"))
        self.rotateYButton.setText(_translate("MainWindow", "Повернуть по Y"))
        self.setButton.setText(_translate("MainWindow", "Задать многограник"))
        self.randomButton.setText(_translate("MainWindow", "Случайный многограник"))
from openglwidget import OpenGLWidget
