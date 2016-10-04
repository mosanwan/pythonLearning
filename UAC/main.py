import sys
from PyQt5.QtWidgets import *


class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.setWindowTitle("UCA")
        self.setMinimumSize(800,600)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())
