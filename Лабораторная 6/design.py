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
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openGLWidget = CubeLightsWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(90, 50, 451, 471))
        self.openGLWidget.setObjectName("openGLWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(576, 70, 219, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.zLightLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.zLightLine.setObjectName("zLightLine")
        self.gridLayout.addWidget(self.zLightLine, 4, 2, 1, 1)
        self.xLightLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.xLightLine.setObjectName("xLightLine")
        self.gridLayout.addWidget(self.xLightLine, 4, 0, 1, 1)
        self.xCameraLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.xCameraLine.setObjectName("xCameraLine")
        self.gridLayout.addWidget(self.xCameraLine, 1, 0, 1, 1)
        self.yCameraLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.yCameraLine.setObjectName("yCameraLine")
        self.gridLayout.addWidget(self.yCameraLine, 1, 1, 1, 1)
        self.zCameraLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.zCameraLine.setObjectName("zCameraLine")
        self.gridLayout.addWidget(self.zCameraLine, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.lightButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lightButton.setObjectName("lightButton")
        self.gridLayout.addWidget(self.lightButton, 5, 0, 1, 3)
        self.yLightLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.yLightLine.setObjectName("yLightLine")
        self.gridLayout.addWidget(self.yLightLine, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 3)
        self.cameraButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cameraButton.setObjectName("cameraButton")
        self.gridLayout.addWidget(self.cameraButton, 2, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.label.setText(_translate("MainWindow", "Введите координаты камеры"))
        self.lightButton.setText(_translate("MainWindow", "Ввести координаты света"))
        self.label_2.setText(_translate("MainWindow", "Введите координаты света"))
        self.cameraButton.setText(_translate("MainWindow", "Ввести координаты камеры"))
from cube_lights import CubeLightsWidget
