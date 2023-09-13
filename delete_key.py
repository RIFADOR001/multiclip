from PyQt5 import QtCore, QtGui, QtWidgets
from confirm_delete import Ui_DeleteData
from key_not_found import Ui_KeyNotFound
from functions import load_dict, delete_data
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QWidget, QCompleter


class Ui_DeleteKey(object):
    def setupUi(self, key_dialog, file):
        key_dialog.setObjectName("key_dialog")
        key_dialog.resize(400, 200)
        key_dialog.setMinimumSize(QtCore.QSize(400, 200))
        key_dialog.setMaximumSize(QtCore.QSize(400, 200))
        self.file = file
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

        my_dict = load_dict(self.file)
        keys = [k for k in my_dict.keys()]
        completer = QCompleter(keys)
        self.lineEdit.setCompleter(completer)

        # self.confirmButton.clicked.connect(lambda: self.confirm_window())
        self.confirmButton.clicked.connect(lambda: self.verify_key())

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

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Are you sure?")
        # msg.setText("Main text")
        msg.setIcon(QMessageBox.Question)

        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.setInformativeText("The selected data will be deleted")

        msg.setDetailedText("Deleted data cannot be recovered")

        # msg.buttonClicked.connect(self.popup_button)
        # answer = self.popup_button.text()
        returnValue = msg.exec()
        if returnValue == QMessageBox.Ok:
            return 0

        # x = msg.exec_()

    def popup_button(self, button_clicked):
        print(button_clicked.text())

    def verify_key(self):
        key = self.lineEdit.text().strip()
        my_dict = load_dict(self.file)
        if key in my_dict.keys():
            answer = self.show_popup()
            if answer == 0:
                delete_data(self.file, key)
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_KeyNotFound()
            self.ui.setupUi(self.window)
            self.window.show()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    key_dialog = QtWidgets.QDialog()
    ui = Ui_DeleteKey()
    ui.setupUi(key_dialog, "multi.json")
    key_dialog.show()
    sys.exit(app.exec_())
