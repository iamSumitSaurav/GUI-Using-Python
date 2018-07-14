# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menusystem.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import math
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 111)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.t1 = QtWidgets.QLineEdit(self.centralwidget)
        self.t1.setObjectName("t1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.t1)
        self.t2 = QtWidgets.QLineEdit(self.centralwidget)
        self.t2.setObjectName("t2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.t2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 240, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSquare = QtWidgets.QAction(MainWindow)
        self.actionSquare.setShortcut("")
        self.actionSquare.setObjectName("actionSquare")
        self.actionCube = QtWidgets.QAction(MainWindow)
        self.actionCube.setObjectName("actionCube")
        self.actionSquare_Root = QtWidgets.QAction(MainWindow)
        self.actionSquare_Root.setObjectName("actionSquare_Root")
        self.actionCube_Root = QtWidgets.QAction(MainWindow)
        self.actionCube_Root.setObjectName("actionCube_Root")
        self.menuFile.addAction(self.actionSquare)
        self.menuFile.addAction(self.actionCube)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSquare_Root)
        self.menuFile.addAction(self.actionCube_Root)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.triggered[QtWidgets.QAction].connect(self.menufuction)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Number"))
        self.label_2.setText(_translate("MainWindow", "Result"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSquare.setText(_translate("MainWindow", "Square"))
        self.actionCube.setText(_translate("MainWindow", "Cube"))
        self.actionSquare_Root.setText(_translate("MainWindow", "Square Root"))
        self.actionCube_Root.setText(_translate("MainWindow", "Cube Root"))

    def menufuction(self, action):
        txt = (action.text())
        no = int(self.t1.text())
        print(txt, no)
        if txt == 'Square':
            self.t2.setText(str(no*no))
        if txt == 'Cube':
            self.t2.setText(str(no*no*no))
        if txt == 'Square Root':
            self.t2.setText(str(math.sqrt(no)))
        if txt == 'Cube Root':
            self.t2.setText(str(math.pow(no,1/3)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

