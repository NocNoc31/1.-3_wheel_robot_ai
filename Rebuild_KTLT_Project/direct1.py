# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'direct1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(632, 462)
        Form.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-30, 0, 691, 211))
        self.widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(70, -20, 511, 261))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("direct1.jpg"))
        self.label.setObjectName("label")
        self.forw_but = QtWidgets.QPushButton(Form)
        self.forw_but.setGeometry(QtCore.QRect(260, 220, 100, 50))
        self.forw_but.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"\n"
"QPushButton#forw_but{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#forw_but:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#forw_but:hover{\n"
"background-color: rgb(85, 87, 83);\n"
"}")
        self.forw_but.setObjectName("forw_but")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(250, 290, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(173, 330, 20, 111))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(420, 330, 16, 151))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.right_but = QtWidgets.QPushButton(Form)
        self.right_but.setGeometry(QtCore.QRect(390, 280, 100, 50))
        self.right_but.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"\n"
"QPushButton#forw_but{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#forw_but:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#forw_but:hover{\n"
"background-color: rgb(85, 87, 83);\n"
"}")
        self.right_but.setObjectName("right_but")
        self.left_but = QtWidgets.QPushButton(Form)
        self.left_but.setGeometry(QtCore.QRect(130, 280, 100, 50))
        self.left_but.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"\n"
"QPushButton#forw_but{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#forw_but:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#forw_but:hover{\n"
"background-color: rgb(85, 87, 83);\n"
"}")
        self.left_but.setObjectName("left_but")
        self.reverse_but = QtWidgets.QPushButton(Form)
        self.reverse_but.setGeometry(QtCore.QRect(260, 380, 100, 50))
        self.reverse_but.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"\n"
"QPushButton#forw_but{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#forw_but:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#forw_but:hover{\n"
"background-color: rgb(85, 87, 83);\n"
"}")
        self.reverse_but.setObjectName("reverse_but")
        self.back_but = QtWidgets.QPushButton(Form)
        self.back_but.setGeometry(QtCore.QRect(510, 240, 100, 50))
        self.back_but.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"\n"
"QPushButton#forw_but{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#forw_but:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#forw_but:hover{\n"
"background-color: rgb(85, 87, 83);\n"
"}")
        self.back_but.setObjectName("back_but")
        self.start_but = QtWidgets.QPushButton(Form)
        self.start_but.setGeometry(QtCore.QRect(510, 370, 100, 50))
        self.start_but.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"background-color: rgb(138, 226, 52);\n"
"\n"
"QPushButton#forw_but{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#forw_but:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#forw_but:hover{\n"
"background-color: rgb(85, 87, 83);\n"
"}")
        self.start_but.setObjectName("start_but")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.forw_but.setText(_translate("Form", "FORWARD"))
        self.right_but.setText(_translate("Form", "RIGHT"))
        self.left_but.setText(_translate("Form", "LEFT"))
        self.reverse_but.setText(_translate("Form", "REVERSE"))
        self.back_but.setText(_translate("Form", "BACK"))
        self.start_but.setText(_translate("Form", "START"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
