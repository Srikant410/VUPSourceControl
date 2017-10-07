# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RADDevice_ui.ui'
#
# Created: Sat Sep 16 13:01:11 2017
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1124, 563)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(390, 0, 291, 51))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(19)
        font.setItalic(False)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(340, 60, 361, 181))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton_1 = QtGui.QPushButton(self.groupBox)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 60, 75, 23))
        self.pushButton_1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 60, 75, 23))
        self.pushButton_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 80, 75, 23))
        self.pushButton_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 80, 75, 23))
        self.pushButton_4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.dateTimeEdit = QtGui.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setEnabled(True)
        self.dateTimeEdit.setGeometry(QtCore.QRect(820, 60, 194, 22))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 311, 121))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(14)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setFrameShadow(QtGui.QFrame.Raised)
        self.label_2.setMidLineWidth(1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lcdNumber = QtGui.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(820, 120, 191, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(270, 0, 20, 471))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(770, 0, 20, 471))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(0, 460, 1121, 21))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 490, 171, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "RAD Device Specifications", None))
        self.label.setText(_translate("Dialog", "RAD DEVICE HEX NUMBER", None))
        self.groupBox.setTitle(_translate("Dialog", "Button Click Status", None))
        self.pushButton_1.setText(_translate("Dialog", "Button1", None))
        self.pushButton_2.setText(_translate("Dialog", "Button2", None))
        self.pushButton_3.setText(_translate("Dialog", "Button3", None))
        self.pushButton_4.setText(_translate("Dialog", "Button4", None))
        self.dateTimeEdit.setDisplayFormat(_translate("Dialog", "MM-dd-yyyy hh:mm:ss", None))
        self.label_2.setText(_translate("Dialog", "Current Software Version", None))
        self.label_3.setText(_translate("Dialog", "Status", None))

