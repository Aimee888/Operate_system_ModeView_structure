# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_boke.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(638, 457)
        self.LabPic = QtWidgets.QLabel(Form)
        self.LabPic.setGeometry(QtCore.QRect(20, 10, 601, 441))
        self.LabPic.setText("")
        self.LabPic.setObjectName("LabPic")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图片"))
