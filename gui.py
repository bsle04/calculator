from PyQt6.QtWidgets import QApplication, QWidget
from qt_setup import Ui_Form
import sys

class Login(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()       
        self.ui.setupUi(self)       
        
        # show the lwindow
        self.show()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login()
    sys.exit(app.exec())