
from PyQt5 import QtCore, QtGui, QtWidgets
from functions import load_dict
from ui_functions import ui_save_dictionary


#class Ui_MainWindow(object):
class Ui_DeleteNotes(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow, file, key):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(461, 255)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.file = file
        self.key = key
        self.my_dict = load_dict(file)
        self.notes = self.my_dict[key][1:]
        self.checkBoxes = []
        aux = 0
        for n in range(len(self.my_dict[key][1:])):
            cb = QtWidgets.QCheckBox(self.centralwidget)
            cb.setGeometry(QtCore.QRect(20, 50+aux*20, 87, 20))

            cb.setObjectName("checkBox")
            aux += 1
            self.checkBoxes.append(cb)
        # self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        # self.checkBox.setGeometry(QtCore.QRect(20, 50, 87, 20))
        # self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 231, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 80+aux*20, 113, 32))
        self.pushButton.setObjectName("pushButton")
        MainWindow.resize(461, 150+aux*20)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 461, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(lambda: self.delete_selected(MainWindow))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Delete notes"))
        # self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        for n, cb in enumerate(self.checkBoxes):
            cb.setText(_translate("MainWindow", f"{self.my_dict[self.key][n+1]}"))
            cb.adjustSize()
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Select the notes to delete</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Confirm"))

    def delete_selected(self, MainWindow):
        self.checkBoxes.reverse()
        length = len(self.notes)
        for n, cb in enumerate(self.checkBoxes):
            if cb.isChecked():
                self.my_dict[self.key].pop(length-n)

        print(self.notes)
        ui_save_dictionary(self.file, self.my_dict)
        MainWindow.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_DeleteNotes()
    ui.setupUi(MainWindow, [0,1,2,3,4,1 , 1,1 ,1 ,1 ,1 ,1 ,1])
    MainWindow.show()
    sys.exit(app.exec_())
