"""
Sudarat Pitakwongroj
683040504-2
P2
"""

import sys
import math
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout,
    QPushButton, QLineEdit, QLabel
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 420)

        main_layout = QVBoxLayout(self)

        self.mode = QLabel("Standard")
        self.mode.setFont(QFont("Arial", 10))
        main_layout.addWidget(self.mode)

        self.display = QLineEdit()
        self.display.setFont(QFont("Arial", 20))
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(50)
        main_layout.addWidget(self.display)

        grid = QGridLayout()

        buttons = [
            ["%", "CE", "C", "<-"],
            ["1/x", "x^2", "sqrt(x)", "/"],
            ["7", "8", "9", "x"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["+/-", "0", ".", "="],
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                btn = QPushButton(text)
                btn.setFixedSize(60, 45)
                btn.clicked.connect(self.on_click)
                grid.addWidget(btn, r, c)

        main_layout.addLayout(grid)

    def on_click(self):
        text = self.sender().text()

        if text == "C":
            self.display.clear()

        elif text == "CE":
            self.display.clear()

        elif text == "<-":
            self.display.setText(self.display.text()[:-1])

        elif text == "=":
            self.calculate()

        elif text == "1/x":
            self.single_operation(lambda x: 1 / x)

        elif text == "x^2":
            self.single_operation(lambda x: x ** 2)

        elif text == "sqrt(x)":
            self.single_operation(lambda x: math.sqrt(x))

        elif text == "+/-":
            self.single_operation(lambda x: -x)

        elif text == "%":
            self.single_operation(lambda x: x / 100)

        else:
            self.display.setText(self.display.text() + text)

    def calculate(self):
        try:
            expression = self.display.text()
            result = eval(expression)
            self.display.setText(str(result))
        except:
            self.display.setText("Error")

    def single_operation(self, operation):
        try:
            value = float(self.display.text())
            result = operation(value)
            self.display.setText(str(result))
        except:
            self.display.setText("Error")


def main():
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
