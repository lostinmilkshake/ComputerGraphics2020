# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import CubeOpegl

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Вращение куба")
        MainWindow.resize(873, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(720, 530, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.openGLWidget = CubeOpegl.OpenGLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(10, 0, 641, 541))
        self.openGLWidget.setObjectName("openGLWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(680, 20, 171, 266))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.x0Coor = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.x0Coor.setObjectName("x0Coor")
        self.verticalLayout.addWidget(self.x0Coor)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.y0Coor = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.y0Coor.setObjectName("y0Coor")
        self.verticalLayout.addWidget(self.y0Coor)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.z0Coor = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.z0Coor.setObjectName("z0Coor")
        self.verticalLayout.addWidget(self.z0Coor)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.x1Coor = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.x1Coor.setObjectName("x1Coor")
        self.verticalLayout.addWidget(self.x1Coor)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.y1Coor = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.y1Coor.setObjectName("y1Coor")
        self.verticalLayout.addWidget(self.y1Coor)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.z1Coor = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.z1Coor.setObjectName("z1Coor")
        self.verticalLayout.addWidget(self.z1Coor)
        self.angleSlider = QtWidgets.QLineEdit(self.centralwidget)
        self.angleSlider.setGeometry(QtCore.QRect(680, 350, 160, 22))
        #self.angleSlider.setMaximum(360)
        #self.angleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.angleSlider.setObjectName("angleSlider")
        self.angleText = QtWidgets.QLabel(self.centralwidget)
        self.angleText.setGeometry(QtCore.QRect(680, 320, 150, 21))
        self.angleText.setObjectName("angleText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 21))
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
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "Введите координату y0"))
        self.label_2.setText(_translate("MainWindow", "Введите координату z0"))
        self.label_3.setText(_translate("MainWindow", "Введите координату x0"))
        self.label_4.setText(_translate("MainWindow", "Введите координату y1"))
        self.label_5.setText(_translate("MainWindow", "Введите координату z1"))
        self.label_6.setText(_translate("MainWindow", "Введите координату x1"))
        self.angleText.setText(_translate("MainWindow", "Угол поворота: 0"))

