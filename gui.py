from PyQt6.QtWidgets import QApplication, QWidget
from qt_setup import Ui_Form
from functools import partial
import sys

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()       
        self.ui.setupUi(self)

    def setDisplayText(self, text):
        self.ui.textBrowser.setText(text)

    def displayText(self):
        return self.ui.textBrowser.toPlainText()

    def clearDisplay(self):
        self.setDisplayText("")

    def checkClicks(self):
        self.ui.pushButton_15.clicked.connect(lambda: self.setDisplayText("2"))

def evaluateExpression(expression):
    """Evaluate an expression (Model)."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = "ERROR"
    return result

class PyCalc:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view

        # Define button map before connecting signals
        self._view.buttonMap = {
            "AC": self._view.ui.pushButton,       # AC for Clear
            "C": self._view.ui.pushButton,        # Add clear symbol
            "1": self._view.ui.pushButton_13,
            "2": self._view.ui.pushButton_15,
            "3": self._view.ui.pushButton_16,
            "4": self._view.ui.pushButton_9,
            "5": self._view.ui.pushButton_10,
            "6": self._view.ui.pushButton_11,
            "7": self._view.ui.pushButton_2,
            "8": self._view.ui.pushButton_6,
            "9": self._view.ui.pushButton_7,
            "0": self._view.ui.pushButton_14,
            "+": self._view.ui.pushButton_17,
            "-": self._view.ui.pushButton_12,
            "*": self._view.ui.pushButton_8,
            "/": self._view.ui.pushButton_5,
            "%": self._view.ui.pushButton_4,
            "=": self._view.ui.pushButton_19,
            ".": self._view.ui.pushButton_18,
        }

        self._connectSignalsAndSlots()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, subExpression):
        if self._view.displayText() == "ERROR":
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)

    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C", "AC"}:
                button.clicked.connect(partial(self._buildExpression, keySymbol))

        # "=" button calculates result
        self._view.buttonMap["="].clicked.connect(self._calculateResult)

        # "AC" and "C" buttons clear the display
        self._view.buttonMap["AC"].clicked.connect(self._view.clearDisplay)
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login()
    login_window.show()
    PyCalc(model=evaluateExpression, view=login_window)
    sys.exit(app.exec())
