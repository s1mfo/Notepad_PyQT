from PyQt5.QtWidgets import QApplication, QTextBrowser, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon, QFont
import sys
import time
import os

class Window(QWidget) :
    
    def __init__ (self):
        super().__init__()

        self.title="Wokatoka Notepad"
        self.top = 400
        self.left = 400
        self.width = 300
        self.height = 600

        self.setFixedSize(self.width,self.height)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(QIcon('/image/woka.png'))
    
        self.Ui()
    
    def Ui (self):
        
        self.browser = QTextBrowser()
        self.lineEdit = QLineEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(self.browser)
        vbox.addWidget(self.lineEdit)

        self.setLayout(vbox)
        self.lineEdit.returnPressed.connect(self.updateBrowser)
        
    
    def updateBrowser(self):
        now = time
        now_time = now.strftime('%H:%M:%S')
        now_date = now.localtime().tm_mday
        now_month = now.localtime().tm_mon
        now_year = now.localtime().tm_year
        insert_line = "-------------------------------------------------------------------------------------------"


        try:
            text = str(self.lineEdit.text ())
            self.browser.append("%s = <b>%s</b>" %(text, eval(text)))
            self.lineEdit.clear()
        except:
            if text == "--":
                self.browser.append(insert_line)
                self.lineEdit.clear()
            if text == "*start":
                self.browser.append("<p style='font-size:16px'> <b>%s/%s/%s</b> </p>" %(now_date,now_month,now_year))
                self.lineEdit.clear()
            else:
                self.browser.append("<b>[%s]</b> %s" %(now_time, text))
                self.lineEdit.clear()
          
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
