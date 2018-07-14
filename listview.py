# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listview.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 340)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 271))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.list1 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.list1.setFont(font)
        self.list1.setObjectName("list1")
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        self.horizontalLayout.addWidget(self.list1)
        spacerItem = QtWidgets.QSpacerItem(138, 38, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.list2 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.list2.setObjectName("list2")
        self.horizontalLayout.addWidget(self.list2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 300, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(250, 300, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.list1.itemDoubleClicked.connect(self.removelist1)
        self.list2.itemDoubleClicked.connect(self.removelist2)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def removelist1(self, item):
        self.list1.takeItem(self.list1.row(item))
        self.list2.addItem(item.text())

    def removelist2(self, item):
        self.list2.takeItem(self.list2.row(item))
        self.list1.addItem(item.text())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.list1.isSortingEnabled()
        self.list1.setSortingEnabled(False)
        item = self.list1.item(0)
        item.setText(_translate("Form", "MS Dhoni"))
        item = self.list1.item(1)
        item.setText(_translate("Form", "Virat Kohli"))
        item = self.list1.item(2)
        item.setText(_translate("Form", "Rahul Sharma"))
        item = self.list1.item(3)
        item.setText(_translate("Form", "Dinesh Karthik"))
        item = self.list1.item(4)
        item.setText(_translate("Form", "Bhuvaneshwar Kumar"))
        item = self.list1.item(5)
        item.setText(_translate("Form", "K L Rahul"))
        item = self.list1.item(6)
        item.setText(_translate("Form", "Ravindra Jadeja"))
        item = self.list1.item(7)
        item.setText(_translate("Form", "Gautam Gambhir"))
        item = self.list1.item(8)
        item.setText(_translate("Form", "Yuvraj Singh"))
        item = self.list1.item(9)
        item.setText(_translate("Form", "Ravichandran Ashwin"))
        self.list1.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Form", "Available Players"))
        self.label_2.setText(_translate("Form", "Selected Players"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

