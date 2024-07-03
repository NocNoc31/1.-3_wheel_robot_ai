# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(596, 513)
        MainWindow.setStyleSheet("\n"
"QPushButton#pushButton{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color: rgb(85, 87, 83);\n"
"}\n"
"\n"
"QPushButton#pushButton_3{\n"
"background-color:rgba(3, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_3:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton_3:hover{\n"
"background-color:rgba(2, 141, 238, 238);\n"
"}\n"
"\n"
"QPushButton#pushButton_2{\n"
"background-color:rgba(4, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"background-color:rgba(2, 141, 238, 238);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-30, -20, 861, 211))
        self.widget.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"background-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(130, 20, 401, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("zAyh-yON.jpeg"))
        self.label.setObjectName("label")
        self.switch_but = QtWidgets.QPushButton(self.centralwidget)
        self.switch_but.setGeometry(QtCore.QRect(380, 160, 141, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.switch_but.setFont(font)
        self.switch_but.setObjectName("switch_but")
        self.start_but = QtWidgets.QPushButton(self.centralwidget)
        self.start_but.setGeometry(QtCore.QRect(80, 160, 141, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.start_but.setFont(font)
        self.start_but.setStyleSheet("")
        self.start_but.setObjectName("start_but")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(140, 260, 16, 221))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(440, 260, 20, 171))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(160, 290, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(22)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(240, 220, 118, 23))
        self.progressBar.setProperty("value", 80)
        self.progressBar.setObjectName("progressBar")
        self.line.raise_()
        self.widget.raise_()
        self.switch_but.raise_()
        self.start_but.raise_()
        self.title.raise_()
        self.progressBar.raise_()
        self.line_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 596, 22))
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
        self.switch_but.setText(_translate("MainWindow", "S W I T C H"))
        self.start_but.setText(_translate("MainWindow", "S T A R T"))
        self.title.setText(_translate("MainWindow", "THE CONTROL BY VISION"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
