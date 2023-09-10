from PyQt5 import QtCore, QtGui, QtWidgets
from confirm_delete import Ui_DeleteData


class Ui_DeleteKey(object):
    def setupUi(self, key_dialog):
        key_dialog.setObjectName("key_dialog")
        key_dialog.resize(400, 200)
        key_dialog.setMinimumSize(QtCore.QSize(400, 200))
        key_dialog.setMaximumSize(QtCore.QSize(400, 200))
        self.lineEdit = QtWidgets.QLineEdit(key_dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 50, 231, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.confirmButton = QtWidgets.QPushButton(key_dialog)
        self.confirmButton.setGeometry(QtCore.QRect(130, 80, 113, 32))
        self.confirmButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(key_dialog)
        self.label.setGeometry(QtCore.QRect(130, 20, 121, 16))
        self.label.setObjectName("label")

        self.retranslateUi(key_dialog)
        QtCore.QMetaObject.connectSlotsByName(key_dialog)

        self.confirmButton.clicked.connect(lambda: self.confirm_window())

    def retranslateUi(self, key_dialog):
        _translate = QtCore.QCoreApplication.translate
        key_dialog.setWindowTitle(_translate("key_dialog", "Delete data"))
        self.confirmButton.setText(_translate("key_dialog", "Confirm"))
        self.label.setText(_translate("key_dialog", "Introduce key"))

    def confirm_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DeleteData()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    key_dialog = QtWidgets.QDialog()
    ui = Ui_DeleteKey()
    ui.setupUi(key_dialog)
    key_dialog.show()
    sys.exit(app.exec_())
