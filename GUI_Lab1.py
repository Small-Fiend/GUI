from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Laboratory Work on the GUI №1")
        self.setGeometry(350, 250, 320, 250)

        self.push_button = QtWidgets.QPushButton(self)
        self.push_button.move(110, 130)
        self.push_button.setText("Click on me")
        self.push_button.setFixedWidth(100)
        self.push_button.setStyleSheet("background-color: lightgreen")
        self.push_button.clicked.connect(self.bt_push)

        self.display_label = QtWidgets.QLabel(self)
        self.display_label.setText("Here is the original text")
        self.display_label.move(100, 80)
        self.display_label.setStyleSheet("background-color: lightpink")
        self.display_label.adjustSize()

    def bt_push(self):
        self.display_label.setText("Here is the text after you click on the button")
        self.display_label.move(50, 80)
        self.display_label.setStyleSheet("background-color: lightblue")
        self.push_button.setStyleSheet("background-color: gray")
        self.display_label.adjustSize()

def application():
    app = QApplication(sys.argv)
    window = Window()
    window.setStyleSheet("background-color: #F5DEEE")

    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    application()
