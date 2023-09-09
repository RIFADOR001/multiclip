from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QWidget


class Ui_SecondWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button001 = QtWidgets.QPushButton(self.centralwidget)
        self.button001.setGeometry(QtCore.QRect(220, 150, 121, 51))
        self.button001.setObjectName("button001")
        self.label001 = QtWidgets.QLabel(self.centralwidget)
        self.label001.setGeometry(QtCore.QRect(240, 70, 101, 16))
        self.label001.setObjectName("label001")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBy_note = QtWidgets.QAction(MainWindow)
        self.actionBy_note.setObjectName("actionBy_note")
        self.actionBy_key = QtWidgets.QAction(MainWindow)
        self.actionBy_key.setObjectName("actionBy_key")
        self.actionBy_content = QtWidgets.QAction(MainWindow)
        self.actionBy_content.setObjectName("actionBy_content")
        self.menuMenu.addAction(self.actionBy_note)
        self.menuMenu.addAction(self.actionBy_key)
        self.menuMenu.addAction(self.actionBy_content)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button001.setText(_translate("MainWindow", "Button thing"))
        self.label001.setText(_translate("MainWindow", "Label thing"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionBy_note.setText(_translate("MainWindow", "By note"))
        self.actionBy_key.setText(_translate("MainWindow", "By key"))
        self.actionBy_content.setText(_translate("MainWindow", "By content"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
