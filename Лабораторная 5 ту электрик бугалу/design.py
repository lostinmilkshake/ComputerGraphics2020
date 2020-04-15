# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openGLWidget = OpenGLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(90, 50, 451, 471))
        self.openGLWidget.setObjectName("openGLWidget")
        self.edgesCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.edgesCheckBox.setGeometry(QtCore.QRect(590, 110, 131, 17))
        self.edgesCheckBox.setObjectName("edgesCheckBox")
        self.visibilityCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.visibilityCheckBox.setGeometry(QtCore.QRect(590, 140, 201, 17))
        self.visibilityCheckBox.setObjectName("visibilityCheckBox")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.edgesCheckBox.setText(_translate("MainWindow", "Отображать грани"))
        self.visibilityCheckBox.setText(_translate("MainWindow", "Показывать только видимые грани"))

from openglwidget import OpenGLWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

