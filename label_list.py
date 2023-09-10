from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QWidget


class Ui_LabelList(object):
    def setupUi(self, MainWindow, text="List"):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.list_label = QtWidgets.QLabel(self.centralwidget)
        self.list_label.setGeometry(QtCore.QRect(40, 40, 101, 16))
        self.list_label.setObjectName("label001")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.list_label.setText(text)
        self.list_label.adjustSize()
        self.centralwidget.adjustSize()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data list"))
        self.list_label.setText(_translate("MainWindow", "Label thing"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LabelList()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
