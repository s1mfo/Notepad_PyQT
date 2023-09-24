from PyQt5.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget, QPushButton, QTextEdit
from PyQt5.QtGui import QIcon, QFont
import sys
import time

now = time
now_time = now.strftime('%H:%M:%S')
now_date = now.localtime().tm_mday
now_month = now.localtime().tm_mon
now_year = now.localtime().tm_year

class Window(QWidget) :
    
    def __init__ (self):
        super().__init__()

        self.title="Wokatoka Notepad"
        self.top = 400
        self.left = 400
        self.width = 400
        self.height = 600

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(QIcon('D:/Solo Coding/Projects/Notepad_PyQT/image/woka.png'))
    
        self.Ui()
    
    def Ui (self):
        
        self.edit = QTextEdit()
        self.lineEdit = QLineEdit()
        self.save_btn = QPushButton('Save')
        self.save_btn.clicked.connect(self.save_text)

        vbox = QVBoxLayout()
        vbox.addWidget(self.edit)
        vbox.addWidget(self.lineEdit)
        vbox.addWidget(self.save_btn)

        self.setLayout(vbox)
        self.lineEdit.returnPressed.connect(self.updateBrowser)
    


    def updateBrowser(self):
       
        try:
            text = str(self.lineEdit.text ())
            self.edit.append("<b>[%s]</b> %s = <b>%s</b>" %(now_time, text, eval(text)))
            self.lineEdit.clear()
            
        except:
            if text == "*start":
                self.edit.append("<p style='font-size:16px'> <b>%s/%s/%s</b></p>" %(now_date,now_month,now_year))
                self.lineEdit.clear()
            elif text == "--":
                insert_line = "-------------------------------------------------------------------------------------------"
                self.edit.append("<p style= 'color:blue'>%s</p>"%(insert_line))
                self.lineEdit.clear()
            else:
                self.edit.append("<b>[%s]</b> %s" %(now_time, text))
                self.lineEdit.clear()

    def save_text(self):
        with open('test.txt', 'a' ) as f:
            my_text = self.edit.toPlainText()
            f.write(my_text)               
          
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()