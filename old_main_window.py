from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QWidget


#class Ui_MainWindow(object):
class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 506)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button001 = QtWidgets.QPushButton(self.centralwidget)
        self.button001.setGeometry(QtCore.QRect(420, 350, 121, 51))
        self.button001.setObjectName("button001")
        self.button002 = QtWidgets.QPushButton(self.centralwidget)
        self.button002.setGeometry(QtCore.QRect(600, 350, 121, 51))
        self.button002.setObjectName("button002")
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
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
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

        self.actionBy_content.triggered.connect(lambda: self.clicked("content was clicked"))
        self.actionBy_note.triggered.connect(lambda: self.clicked("note was clicked"))
        self.actionBy_key.triggered.connect(lambda: self.clicked("key was clicked"))
        self.button001.clicked.connect(lambda: self.show_popup())
        self.button002.clicked.connect(lambda: self.set_label())
        # self.link001.click(lambda: self.clicked("link001"))

        self.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button001.setText(_translate("MainWindow", "Button thing"))
        self.button002.setText(_translate("MainWindow", "Button 2"))
        self.label001.setText(_translate("MainWindow", "Label thing"))
        self.menuMenu.setTitle(_translate("MainWindow", "Search"))
        self.actionBy_note.setText(_translate("MainWindow", "By note"))
        self.actionBy_key.setText(_translate("MainWindow", "By key"))
        self.actionBy_content.setText(_translate("MainWindow", "By content"))

    def clicked(self, text):
        self.label001.setText(text)
        self.label001.adjustSize()

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Tuto tittle")
        msg.setText("Main text")
        msg.setIcon(QMessageBox.Question)

        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.setInformativeText("here informative text")

        msg.setDetailedText("details")

        msg.buttonClicked.connect(self.popup_button)

        x = msg.exec_()

    def popup_button(self, button_clicked):
        print(button_clicked.text())

    def set_label(self):
        text = "Button 2 has beeen pushed"
        self.label001.setText(text)
        self.label001.adjustSize()

    def press_it(self):
        self.label001.setText(f"you picked {self.my_text.toPlainText()}")



def window():
    # app = QApplication(sys.argv)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # win = Ui_MainWindow()

    # win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()
