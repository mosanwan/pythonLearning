import sys
from PyQt5.QtWidgets import *


class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin,self).__init__()
        self.setWindowTitle("UCA")
        self.setMinimumSize(800,600)
        self.createAction()
        self.createMenu()

    def about(self):
        QMessageBox.about(self,"About Menu","asdf\n sdfasd")

    def createAction(self):
        self.aboutAct = QAction("&About UAC", self,
                        statusTip="Show About",
                        triggered=self.about)
        self.aboutQTAct = QAction("&About PyQT5", self,
                                statusTip="Show About",
                                triggered=self.about)

    def createMenu(self):
        self.settingMenu = self.menuBar().addMenu("&Setting")
        self.aboutMenu = self.menuBar().addMenu("&About")
        self.aboutMenu.addAction(self.aboutAct)
        self.aboutMenu.addAction(self.aboutQTAct)


app = QApplication(sys.argv)
win = MainWin()
win.show()
sys.exit(app.exec())
