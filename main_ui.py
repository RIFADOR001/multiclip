from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QWidget
from save_window import Ui_Save
from delete_key import Ui_DeleteKey
from note_key import Ui_NoteKey
from load_key import Ui_LoadKey
from delete_note_key import Ui_DeleteNoteKey
from key_dialog import Ui_key
from confirm_delete import Ui_DeleteData
from list import Ui_List
from note_dialog import Ui_note
from label_list import Ui_LabelList
from functions import load_dict
from ui_functions import dict_to_string


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(573, 252)
        self.file = "multi.json"
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.list_button = QtWidgets.QPushButton(self.centralwidget)
        self.list_button.setGeometry(QtCore.QRect(30, 130, 121, 32))
        self.list_button.setObjectName("list_button")
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(190, 130, 121, 32))
        self.delete_button.setObjectName("delete_button")
        self.delete_note_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_note_button.setGeometry(QtCore.QRect(350, 130, 121, 32))
        self.delete_note_button.setObjectName("delete_note_button")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(30, 70, 121, 32))
        self.save_button.setObjectName("save_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 511, 16))
        self.label.setObjectName("label")
        self.load_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_button.setGeometry(QtCore.QRect(190, 70, 121, 32))
        self.load_button.setObjectName("load_button")
        self.note_button = QtWidgets.QPushButton(self.centralwidget)
        self.note_button.setGeometry(QtCore.QRect(350, 70, 121, 32))
        self.note_button.setObjectName("note_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 573, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSearch = QtWidgets.QMenu(self.menubar)
        self.menuSearch.setObjectName("menuSearch")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_file = QtWidgets.QAction(MainWindow)
        self.actionNew_file.setObjectName("actionNew_file")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionBy_key = QtWidgets.QAction(MainWindow)
        self.actionBy_key.setObjectName("actionBy_key")
        self.actionBy_Note = QtWidgets.QAction(MainWindow)
        self.actionBy_Note.setObjectName("actionBy_Note")
        self.actionBy_content = QtWidgets.QAction(MainWindow)
        self.actionBy_content.setObjectName("actionBy_content")
        self.menuFile.addAction(self.actionNew_file)
        self.menuFile.addAction(self.actionLoad)
        self.menuSearch.addAction(self.actionBy_key)
        self.menuSearch.addAction(self.actionBy_Note)
        self.menuSearch.addAction(self.actionBy_content)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSearch.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.save_button.clicked.connect(lambda: self.save_window())
        self.delete_button.clicked.connect(lambda: self.delete_window())
        self.note_button.clicked.connect(lambda: self.note_window())
        self.load_button.clicked.connect(lambda: self.load_window())
        self.delete_note_button.clicked.connect(lambda: self.delete_note_window())
        self.list_button.clicked.connect(lambda: self.list_window())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Multiclip"))
        self.list_button.setText(_translate("MainWindow", "List"))
        self.delete_button.setText(_translate("MainWindow", "Delete entry"))
        self.delete_note_button.setText(_translate("MainWindow", "Delete note"))
        self.save_button.setText(_translate("MainWindow", "Save entry"))
        self.label.setText(_translate("MainWindow", "Current document: "))
        self.load_button.setText(_translate("MainWindow", "Load entry"))
        self.note_button.setText(_translate("MainWindow", "Note"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSearch.setTitle(_translate("MainWindow", "Search"))
        self.actionNew_file.setText(_translate("MainWindow", "New"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionBy_key.setText(_translate("MainWindow", "By key"))
        self.actionBy_Note.setText(_translate("MainWindow", "By Note"))
        self.actionBy_content.setText(_translate("MainWindow", "By content"))

    def save_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Save()
        self.ui.setupUi(self.window, self.file)
        self.window.show()

    def delete_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DeleteKey()
        self.ui.setupUi(self.window)
        self.window.show()

    def note_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_NoteKey()
        self.ui.setupUi(self.window)
        self.window.show()

    def load_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LoadKey()
        self.ui.setupUi(self.window, self.file)
        self.window.show()

    def delete_note_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DeleteNoteKey()
        self.ui.setupUi(self.window)
        self.window.show()

    def list_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LabelList()
        my_dict = load_dict(self.file)
        text = dict_to_string(my_dict)
        self.ui.setupUi(self.window, text)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
