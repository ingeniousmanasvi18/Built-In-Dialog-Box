from PySide6.QtGui import*
from PySide6.QtCore import *
import sys
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QTextBrowser, QLineEdit, QVBoxLayout,QFileDialog
__appname__="BuiltIn"
class Program(QDialog):
    def __init__(self,parent=None):
        super(Program, self).__init__(parent)
        openButton= QPushButton("open")
        saveButton = QPushButton("save")
        dirButton = QPushButton("other")
        closeButton = QPushButton("close")

        self.connect(openButton,SIGNAL("clicked()"),self.open)

        layout = QVBoxLayout()
        layout.addWidget(openButton)
        layout.addWidget(saveButton)
        layout.addWidget(dirButton)
        layout.addWidget(closeButton)
        self.setLayout(layout)

    def open(self):
        dir="."
        fileobj= QFileDialog.getOpenFileName(self,__appname__+"open file Dialog",dir=dir,filter="Text files('.txt)")
        print(fileobj)
        print(fileobj.dtype)
        fileName=fileobj[0]
        file=open(fileName,"r")
        read=file.read()
        file.close()
        print (read)





app=QApplication(sys.argv)
form= Program()
form.show()
app.exec_()