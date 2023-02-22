import os
import editor.core as core


from PyQt5.uic import loadUi
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QMainWindow,
    QFileDialog,
    QTextEdit,
    QAction,
)


# test
class Window(QMainWindow):
    def __init__(self) -> None:
        super(Window, self).__init__()
        loadUi("./editor/ui/main.ui", self)

        self.setWindowTitle(f"Neon code - {core.get_json_content['version']}")
        self.setStyleSheet(
            f"background-color: {core.get_json_content['ui']['background']};"
        )

        self.textBox = self.findChild(QTextEdit, "textEdit")

        self.textBox.setStyleSheet(
            f"color: {core.get_json_content['ui']['text-color']};"
        )
        self.textBox.setFont(
            QFont(
                core.get_json_content["ui"]["font"],
                core.get_json_content["ui"]["font-size"],
            )
        )

        self.textBox.setText(f"Hi {os.getlogin()}")

        menu = self.menuBar()
        menu.setStyleSheet(core.menu_bar_style)

        self.menu = menu.addMenu("file")

        # set open file action
        open_file = QAction("open file", self)
        open_file.setShortcut("Ctrl+o")
        open_file.triggered.connect(self.open_file_triggered)
        self.menu.addAction(open_file)

        # set save file action
        save_file = QAction("save file", self)
        save_file.setShortcut("Ctrl+s")
        save_file.triggered.connect(self.save_file_triggered)
        self.menu.addAction(save_file)

        self.show()

    def open_file_triggered(self):
        file = QFileDialog.getOpenFileName()

        self.textBox.clear()
        self.textBox.setText(open(file[0], "r").read())

    def save_file_triggered(self):
        get_source = QFileDialog.getOpenFileName()

        with open(get_source[0], "w") as file:
            file.write(self.textBox.toPlainText())
            file.close()
