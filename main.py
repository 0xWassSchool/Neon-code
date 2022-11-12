#Simple Python code editor - Win

import sys
import subprocess
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QApplication, QTextEdit
from PyQt5 import uic


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('app.ui', self)

        self.setWindowTitle("Neon")

        self.run = self.findChild(QPushButton, "run")
        self.run.clicked.connect(self.run_script)

        self.file = self.findChild(QLineEdit, "file")
        self.code = self.findChild(QTextEdit, "code")
        self.output = self.findChild(QTextEdit, "output")

        self.show()

    def run_script(self):
        save = open(self.file.text(), "w")
        save.write(self.code.toPlainText())
        save.close()

        output = subprocess.check_output(
            F"py {self.file.text()}", shell=True).decode("850")
        self.output.setText(output)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui()
    app.exec_()
