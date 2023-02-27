from PyQt5.QtWidgets import QApplication, QTextBrowser, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtSignal
import sys

class Window(QWidget) :
    def __init__ (self):
        super().__init__()

        self.title="PyQt5 Simple Application"
        self.top = 400
        self.left = 400
        self.width = 800
        self.height = 600

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        # 아이콘: self.setWidnowIcon(QIcon('icon.png'))

        self.Ui()
    
    def Ui (self):
        self.browser = QTextBrowser()
        self.lineEdit = QLineEdit("Calculator!")

        vbox = QVBoxLayout()
        vbox.addWidget(self.browser)
        vbox.addWidget(self.lineEdit)

        self.setLayout(vbox)
        self.lineEdit.returnPressed.connect(self.updateBrowser)
    
    def updateBrowser(self):
        try:
            text = str(self.lineEdit.text ())
            self.browser.append("%s = <b>%s</b>" %(text, eval(text)))
        except:
            self.browser.append(
                "<font - color = red> <b>%s</b> is invalid! Type number only </font>" %text
            )

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
