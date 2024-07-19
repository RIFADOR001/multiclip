from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QWidget


class Ui_List(QWidget):
    def setupUi(self, List):
        List.setObjectName("List")
        List.resize(400, 502)
        List.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 398, 500))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableView = QtWidgets.QTableView(self.scrollAreaWidgetContents)
        self.tableView.setGeometry(QtCore.QRect(20, 20, 361, 461))
        self.tableView.setObjectName("tableView")
        List.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(List)
        QtCore.QMetaObject.connectSlotsByName(List)

    def retranslateUi(self, List):
        _translate = QtCore.QCoreApplication.translate
        List.setWindowTitle(_translate("List", "ScrollArea"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    List = QtWidgets.QScrollArea()
    ui = Ui_List()
    ui.setupUi(List)
    List.show()
    sys.exit(app.exec_())
