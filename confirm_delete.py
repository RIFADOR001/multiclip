
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeleteData(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 200)
        Dialog.setMinimumSize(QtCore.QSize(400, 200))
        Dialog.setMaximumSize(QtCore.QSize(400, 200))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 291, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 90, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 90, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Do you want to eliminate the data?"))
        self.pushButton.setText(_translate("Dialog", "Yes"))
        self.pushButton_2.setText(_translate("Dialog", "No"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_DeleteData()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
