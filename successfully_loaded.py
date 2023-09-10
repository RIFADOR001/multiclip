
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SuccessfullyLoaded(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(298, 148)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 50, 171, 41))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Loaded"))
        self.label.setText(_translate("Dialog", "Data loaded successfully"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_SuccessfullyLoaded()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
