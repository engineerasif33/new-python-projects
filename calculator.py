import sys
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("calculator.ui")

def add_numbers():
    num1 = int(window.text1.text())
    num2 = int(window.text2.text())
    result = num1 + num2
    window.text3.setText(str(result))

window.calculate.clicked.connect(add_numbers)

window.show()

sys.exit(app.exec_())
