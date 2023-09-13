from PyQt5 import QtCore, QtGui, QtWidgets
import clipboard
from ui_functions import ui_save
from key_unavailable import Ui_ErrorDialog
from successfully_saved import Ui_SavedDialog


class Ui_Save(object):
    def setupUi(self, Save, file):
        Save.setObjectName("Save")
        Save.resize(400, 200)
        Save.setMinimumSize(QtCore.QSize(400, 200))
        Save.setMaximumSize(QtCore.QSize(400, 200))
        self.label = QtWidgets.QLabel(Save)
        self.label.setGeometry(QtCore.QRect(90, 40, 201, 16))
        self.label.setObjectName("label")
        self.data_line = QtWidgets.QLineEdit(Save)
        self.data_line.setGeometry(QtCore.QRect(70, 70, 321, 21))
        self.data_line.setObjectName("data_line")
        self.confirmButton = QtWidgets.QPushButton(Save)
        self.confirmButton.setGeometry(QtCore.QRect(50, 130, 113, 32))
        self.confirmButton.setObjectName("confirmButton")
        self.pasteButton = QtWidgets.QPushButton(Save)
        self.pasteButton.setGeometry(QtCore.QRect(220, 130, 113, 32))
        self.pasteButton.setObjectName("pasteButton")
        self.key_line = QtWidgets.QLineEdit(Save)
        self.key_line.setGeometry(QtCore.QRect(70, 100, 321, 21))
        self.key_line.setObjectName("key_line")
        self.label_2 = QtWidgets.QLabel(Save)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Save)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 31, 16))
        self.label_3.setObjectName("label_3")
        self.file = file

        self.retranslateUi(Save)
        QtCore.QMetaObject.connectSlotsByName(Save)

        self.confirmButton.clicked.connect(lambda: self.confirm())
        self.pasteButton.clicked.connect(lambda: self.paste())

    def retranslateUi(self, Save):
        _translate = QtCore.QCoreApplication.translate
        Save.setWindowTitle(_translate("Save", "Save"))
        self.label.setText(_translate("Save", "Type or paste the data and key"))
        self.confirmButton.setText(_translate("Save", "Confirm"))
        self.pasteButton.setText(_translate("Save", "Paste data"))
        self.label_2.setText(_translate("Save", "Data"))
        self.label_3.setText(_translate("Save", "Key"))

    def confirm(self):
        data = self.data_line.text()
        key = self.key_line.text().strip()
        if ui_save(self.file, data, key) == -1:
            self.error_window()
        else:
            self.saved_window()

    def paste(self):
        data = clipboard.paste()
        key = self.key_line.text().strip()
        if ui_save(self.file, data, key) == -1:
            self.error_window()
        else:
            self.saved_window()


    def error_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ErrorDialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def saved_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SavedDialog()
        self.ui.setupUi(self.window)
        self.window.show()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Save = QtWidgets.QDialog()
    ui = Ui_Save()
    ui.setupUi(Save)
    Save.show()
    sys.exit(app.exec_())
