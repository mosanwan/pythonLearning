from PyQt5.QtWidgets import *
import sys
from hashlib import md5
import os.path


class MainWin(QWidget):
    def __init__(self):
        super(MainWin,self).__init__()
        self.setWindowTitle('MD5')
        self.resize (800,600)

        self.md5lab = QTextEdit('')

        layout = QVBoxLayout()

        btnlayout = QHBoxLayout()

        fbtn = QPushButton('选择文件')
        fbtn.clicked.connect(self.openfile)
        btnlayout.addWidget(fbtn)

        dbtn = QPushButton("选择文件夹")
        dbtn.clicked.connect(self.opendir)
        btnlayout.addWidget(dbtn)

        layout.addLayout(btnlayout)
        layout.addWidget(self.md5lab)
        #layout.addStretch()
        
        self.setLayout(layout)
    
    def openfile(self):
        fileName, _ =QFileDialog.getOpenFileName(self)
        if fileName:
            m = md5()
            a_file = open(fileName,'rb')
            m.update(a_file.read())
            a_file.close()
            self.md5lab.setText(m.hexdigest()+" "+fileName)
            
    def opendir(self):
        select_dirname = QFileDialog.getExistingDirectory(self)
        if select_dirname:
            for parent,dirnames,filenames in os.walk(select_dirname):
                for filename in filenames:
                    filepath = parent+"/"+filename
                    m = md5()
                    a_file = open(filepath,'rb')
                    m.update(a_file.read())
                    a_file.close()
                    self.md5lab.append(m.hexdigest()+" "+filepath+'\n')
                   


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
