# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(577, 548)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.camera = QtWidgets.QLabel(self.centralwidget)
        self.camera.setGeometry(QtCore.QRect(16, 10, 551, 341))
        self.camera.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.camera.setText("")
        self.camera.setObjectName("camera")
        self.start_but = QtWidgets.QPushButton(self.centralwidget)
        self.start_but.setGeometry(QtCore.QRect(40, 440, 89, 25))
        self.start_but.setObjectName("start_but")
        self.end_but = QtWidgets.QPushButton(self.centralwidget)
        self.end_but.setGeometry(QtCore.QRect(250, 440, 89, 25))
        self.end_but.setObjectName("end_but")
        self.switch_but = QtWidgets.QPushButton(self.centralwidget)
        self.switch_but.setGeometry(QtCore.QRect(450, 440, 89, 25))
        self.switch_but.setObjectName("switch_but")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(220, 370, 191, 17))
        self.title.setObjectName("title")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 577, 22))
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
        self.start_but.setText(_translate("MainWindow", "START"))
        self.end_but.setText(_translate("MainWindow", "END"))
        self.switch_but.setText(_translate("MainWindow", "SWITCH"))
        self.title.setText(_translate("MainWindow", "CAMERA DETECTION"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
