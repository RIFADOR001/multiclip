from PyQt5 import QtCore, QtGui, QtWidgets
import multiclip
from ui_functions import ui_save


class Ui_Save(object):
    def setupUi(self, Save, file):
        Save.setObjectName("Save")
        Save.resize(400, 200)
        Save.setMinimumSize(QtCore.QSize(400, 200))
        Save.setMaximumSize(QtCore.QSize(400, 200))
        self.label = QtWidgets.QLabel(Save)
        self.label.setGeometry(QtCore.QRect(120, 40, 138, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Save)
        self.lineEdit.setGeometry(QtCore.QRect(30, 80, 321, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.confirmButton = QtWidgets.QPushButton(Save)
        self.confirmButton.setGeometry(QtCore.QRect(50, 130, 113, 32))
        self.confirmButton.setObjectName("confirmButton")
        self.pasteButton = QtWidgets.QPushButton(Save)
        self.pasteButton.setGeometry(QtCore.QRect(220, 130, 113, 32))
        self.pasteButton.setObjectName("pasteButton")
        self.file = file

        self.retranslateUi(Save)
        QtCore.QMetaObject.connectSlotsByName(Save)


    def retranslateUi(self, Save):
        _translate = QtCore.QCoreApplication.translate
        Save.setWindowTitle(_translate("Save", "Dialog"))
        self.label.setText(_translate("Save", "Type or paste the data"))
        self.confirmButton.setText(_translate("Save", "Confirm"))
        self.pasteButton.setText(_translate("Save", "Paste"))

    def confirm(self):
        data = self.lineEdit.text()
        ui_save(self.file, data)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Save = QtWidgets.QDialog()
    ui = Ui_Save()
    ui.setupUi(Save)
    Save.show()
    sys.exit(app.exec_())
