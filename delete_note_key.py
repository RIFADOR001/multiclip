
from PyQt5 import QtCore, QtGui, QtWidgets
from delete_notes_window import Ui_DeleteNotes
from functions import load_dict
from key_not_found import Ui_KeyNotFound
from PyQt5.QtWidgets import QCompleter


class Ui_DeleteNoteKey(object):
    def setupUi(self, key_dialog, file):
        key_dialog.setObjectName("key_dialog")
        key_dialog.resize(400, 200)
        key_dialog.setMinimumSize(QtCore.QSize(400, 200))
        key_dialog.setMaximumSize(QtCore.QSize(400, 200))
        self.file = file
        self.lineEdit = QtWidgets.QLineEdit(key_dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 50, 231, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(key_dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 80, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(key_dialog)
        self.label.setGeometry(QtCore.QRect(130, 20, 121, 16))
        self.label.setObjectName("label")

        self.retranslateUi(key_dialog)
        QtCore.QMetaObject.connectSlotsByName(key_dialog)

        my_dict = load_dict(self.file)
        keys = [k for k in my_dict.keys()]
        completer = QCompleter(keys)
        self.lineEdit.setCompleter(completer)

        self.pushButton.clicked.connect(lambda: self.confirm_key())

    def retranslateUi(self, key_dialog):
        _translate = QtCore.QCoreApplication.translate
        key_dialog.setWindowTitle(_translate("key_dialog", "Delete note"))
        self.pushButton.setText(_translate("key_dialog", "Confirm"))
        self.label.setText(_translate("key_dialog", "Introduce key"))

    def confirm_key(self):
        my_dict = load_dict(self.file)
        key = self.lineEdit.text().strip()
        if key in my_dict.keys():
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_DeleteNotes()
            self.ui.setupUi(self.window, self.file, key)
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
    ui = Ui_DeleteNoteKey()
    ui.setupUi(key_dialog)
    key_dialog.show()
    sys.exit(app.exec_())
