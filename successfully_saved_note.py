from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SavedNoteDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(269, 94)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 151, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Saved"))
        self.label.setText(_translate("Dialog", "Note saved successfully "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_SavedDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
