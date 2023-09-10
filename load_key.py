
from PyQt5 import QtCore, QtGui, QtWidgets
from functions import load
from ui_functions import ui_load
from key_not_found import Ui_KeyNotFound
from successfully_loaded import Ui_SuccessfullyLoaded

class Ui_LoadKey(object):
    def setupUi(self, key_dialog, file):
        key_dialog.setObjectName("key_dialog")
        key_dialog.resize(400, 200)
        key_dialog.setMinimumSize(QtCore.QSize(400, 200))
        key_dialog.setMaximumSize(QtCore.QSize(400, 200))
        self.lineEdit = QtWidgets.QLineEdit(key_dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 50, 231, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(key_dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 80, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(key_dialog)
        self.label.setGeometry(QtCore.QRect(130, 20, 121, 16))
        self.label.setObjectName("label")
        self.file = file

        self.retranslateUi(key_dialog)
        QtCore.QMetaObject.connectSlotsByName(key_dialog)

        self.pushButton.clicked.connect(lambda: self.load())

    def retranslateUi(self, key_dialog):
        _translate = QtCore.QCoreApplication.translate
        key_dialog.setWindowTitle(_translate("key_dialog", "Load data"))
        self.pushButton.setText(_translate("key_dialog", "Confirm"))
        self.label.setText(_translate("key_dialog", "Introduce key"))

    def load(self):
        key = self.lineEdit.text()
        aux = ui_load(self.file, key)
        if aux == 0:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_SuccessfullyLoaded()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_KeyNotFound()
            self.ui.setupUi(self.window)
            self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    key_dialog = QtWidgets.QDialog()
    ui = Ui_LoadKey()
    ui.setupUi(key_dialog, "multi.json")
    key_dialog.show()
    sys.exit(app.exec_())
