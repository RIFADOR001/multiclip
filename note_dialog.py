# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'note_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_note_dialog(object):
    def setupUi(self, note_dialog):
        note_dialog.setObjectName("note_dialog")
        note_dialog.resize(400, 200)
        note_dialog.setMinimumSize(QtCore.QSize(400, 200))
        note_dialog.setMaximumSize(QtCore.QSize(400, 200))
        self.label = QtWidgets.QLabel(note_dialog)
        self.label.setGeometry(QtCore.QRect(140, 30, 121, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(note_dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 60, 351, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(note_dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 100, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(note_dialog)
        QtCore.QMetaObject.connectSlotsByName(note_dialog)

    def retranslateUi(self, note_dialog):
        _translate = QtCore.QCoreApplication.translate
        note_dialog.setWindowTitle(_translate("note_dialog", "Dialog"))
        self.label.setText(_translate("note_dialog", "Type a note"))
        self.pushButton.setText(_translate("note_dialog", "Confirm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    note_dialog = QtWidgets.QDialog()
    ui = Ui_note_dialog()
    ui.setupUi(note_dialog)
    note_dialog.show()
    sys.exit(app.exec_())