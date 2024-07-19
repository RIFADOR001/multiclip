from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KeyNotFound(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(367, 137)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 20, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 60, 151, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Error"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">Error</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Key not found"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_KeyNotFound()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
