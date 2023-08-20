import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.count = 0
        self.setWindowTitle("QT test")
        self.setGeometry(300, 300, 1920, 1080)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText('Some text')
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(200, 200)
        self.btn.setText('1')
        self.btn.setFixedWidth(150)
        self.btn.clicked.connect(self.add_button_count)

    def add_button_count(self):
        self.count = self.count + 1
        self.main_text.setText(str(self.count))
        pass
def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
