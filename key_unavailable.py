from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ErrorDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(195, 115)
        Dialog.setMinimumSize(QtCore.QSize(195, 115))
        Dialog.setMaximumSize(QtCore.QSize(195, 115))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 20, 40, 22))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 131, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Error"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">Error</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Key already in use "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ErrorDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
