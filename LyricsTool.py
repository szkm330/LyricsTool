#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: szkm330
import sys
import html
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 558)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input = QtWidgets.QTextEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(30, 50, 261, 311))
        self.input.setObjectName("input")
        self.output = QtWidgets.QTextBrowser(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(500, 50, 271, 311))
        self.output.setObjectName("output")
        self.end = QtWidgets.QLineEdit(self.centralwidget)
        self.end.setGeometry(QtCore.QRect(340, 110, 113, 21))
        self.end.setObjectName("end")
        self.run1 = QtWidgets.QPushButton(self.centralwidget)
        self.run1.setGeometry(QtCore.QRect(350, 190, 93, 28))
        self.run1.setObjectName("run1")
        self.run1.clicked.connect(run1)
        self.run11 = QtWidgets.QPushButton(self.centralwidget)
        self.run11.setGeometry(QtCore.QRect(350, 230, 93, 28))
        self.run11.setObjectName("run11")
        self.run11.clicked.connect(run11)
        self.changeto = QtWidgets.QLineEdit(self.centralwidget)
        self.changeto.setGeometry(QtCore.QRect(312, 150, 171, 21))
        self.changeto.setObjectName("changeto")
        self.changeto.setText("\\N{\\fn思源黑体}") 
        self.c1 = QtWidgets.QLineEdit(self.centralwidget)
        self.c1.setGeometry(QtCore.QRect(40, 440, 113, 21))
        self.c1.setObjectName("c1")
        self.c2 = QtWidgets.QLineEdit(self.centralwidget)
        self.c2.setGeometry(QtCore.QRect(170, 440, 113, 21))
        self.c2.setObjectName("c2")
        self.c3 = QtWidgets.QLineEdit(self.centralwidget)
        self.c3.setGeometry(QtCore.QRect(40, 470, 113, 21))
        self.c3.setObjectName("c3")
        self.c4 = QtWidgets.QLineEdit(self.centralwidget)
        self.c4.setGeometry(QtCore.QRect(170, 470, 113, 21))
        self.c4.setObjectName("c4")
        self.run2 = QtWidgets.QPushButton(self.centralwidget)
        self.run2.setGeometry(QtCore.QRect(350, 450, 93, 28))
        self.run2.setObjectName("run2")
        self.run2.clicked.connect(run2)
        self.gcolor = QtWidgets.QTextBrowser(self.centralwidget)
        self.gcolor.setGeometry(QtCore.QRect(500, 440, 271, 51))
        self.gcolor.setObjectName("gcolor")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 380, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(30, 10, 93, 28))
        self.clear.setObjectName("clear")
        self.clear_2 = QtWidgets.QPushButton(self.centralwidget)
        self.clear_2.setGeometry(QtCore.QRect(40, 400, 93, 28))
        self.clear_2.setObjectName("clear_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.clear.clicked.connect(self.input.clear)
        self.clear.clicked.connect(self.output.clear)
        self.clear.clicked.connect(self.end.clear)
        self.clear_2.clicked.connect(self.c1.clear)
        self.clear_2.clicked.connect(self.c2.clear)
        self.clear_2.clicked.connect(self.c3.clear)
        self.clear_2.clicked.connect(self.c4.clear)
        self.clear_2.clicked.connect(self.gcolor.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LyricsTool"))
        self.run1.setText(_translate("MainWindow", "→"))
        self.run11.setText(_translate("MainWindow", "→→"))
        self.run2.setText(_translate("MainWindow", "→"))
        self.clear.setText(_translate("MainWindow", "X"))
        self.clear_2.setText(_translate("MainWindow", "X"))

def run1():
    try:
        orgin = mainwin.input.toPlainText()
        end = mainwin.end.text()
        changeto = mainwin.changeto.text()
        orgin = orgin.replace(end,changeto + '\n')
        mainwin.output.setText(orgin)
    except:
        QtWidgets.QMessageBox.information(mainwin,'Error','出现错误', QtWidgets.QMessageBox.Ok)

def run11():
    try:
        orgin = mainwin.input.toPlainText()
        orgin = html.unescape(orgin)
        end = mainwin.end.text()
        changeto = mainwin.changeto.text()
        orgin = orgin.replace(end,changeto)
        mainwin.output.setText(orgin)
    except:
        QtWidgets.QMessageBox.information(mainwin,'Error','出现错误', QtWidgets.QMessageBox.Ok)

def run2():
    try:
        c1 = mainwin.c1.text()
        c2 = mainwin.c2.text()
        c3 = mainwin.c3.text()
        c4 = mainwin.c4.text()

        c0 = '{{\\1vc({},{},{},{})}}'.format(c1,c2,c3,c4)
        mainwin.gcolor.setText(c0)
    except:
        QtWidgets.QMessageBox.information(mainwin,'Error','出现错误', QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    mainwin = Ui_MainWindow()
    mainwin.show()
    sys.exit(app.exec_())