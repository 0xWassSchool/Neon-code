import sys


from editor import *
from PyQt5.QtWidgets import QApplication



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()

    app.exec_(Terminal.commands())
