import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Title
        self.setWindowTitle("First window")
        self.setGeometry(400, 400, 200, 200)
        # Layout
        self.setLayout(qtw.QVBoxLayout())
        # Label
        self.my_label = qtw.QLabel("Label thing")
        # Change font size of label
        self.my_label.setFont(qtg.QFont("Helvetica", 18))
        self.layout().addWidget(self.my_label)

        # entry box
        self.my_entry = qtw.QLineEdit()
        self.my_entry.setObjectName("entry001")
        # my_entry.setText("")
        self.layout().addWidget(self.my_entry)

        # Button
        my_button = qtw.QPushButton("Button001", clicked=lambda: self.save())
        self.layout().addWidget(my_button)


        self.show()

    def save(self):
        self.my_label.setText(self.my_entry.text())
        self.my_entry.setText("")


def main_thing():
    app = qtw.QApplication([])
    mw = MainWindow()

    app.exec_()


if __name__ == "__main__":
    main_thing()
