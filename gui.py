from PyQt6.QtWidgets import QApplication, QWidget
from qt_setup import Ui_Form
import sys

class Login(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()       
        self.ui.setupUi(self)

    def setDisplayText(self, text):
        self.ui.textBrowser.setText(text)
    
    def displayText(self):
        return self.display.text()
    
    def clearDisplay(self):
        self.setDisplayText("")
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login()
    login_window.show()
    login_window.setDisplayText("Test")
    sys.exit(app.exec())