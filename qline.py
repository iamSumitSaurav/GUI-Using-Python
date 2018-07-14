# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qline.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(306, 147)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.t1 = QtWidgets.QLineEdit(Form)
        self.t1.setObjectName("t1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.t1)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.t2 = QtWidgets.QLineEdit(Form)
        self.t2.setObjectName("t2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.t2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.t1.setValidator(QtGui.QIntValidator())
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.t3 = QtWidgets.QLineEdit(Form)
        self.t3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.t3.setObjectName("t3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.t3)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.t4 = QtWidgets.QLineEdit(Form)
        self.t4.setObjectName("t4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.t4)
        self.t4.textChanged.connect(self.textchange) 
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def textchange(self,text):
        if text.isalpha()==False:
            print("Non-alphabet characters are not allowed")
            self.t4.setText("")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Integer Validator"))
        self.label_2.setText(_translate("Form", "Input Mask"))
        self.t2.setInputMask(_translate("Form", "+99 999 999 9999"))
        self.label_3.setText(_translate("Form", "Password field"))
        self.label_4.setText(_translate("Form", "Text Changed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

