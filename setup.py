import os
import sys
import json
import ctypes
import datetime
import requests

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QCheckBox


appdata_path = os.path.join(os.environ["APPDATA"] + "\\neon_code")

standard = {
    "version": "1.0.0",
    "ui": {
        "text-color": "white",
        "background": "#2A2824",
        "font-size": 12,
        "font": "Arial",
    },
}

all_dirs = ("logs", "plugins", "themes", "config")


def setup_dirs(dirs: tuple):
    os.mkdir(appdata_path)

    for dir in dirs:
        if not dir in os.listdir(appdata_path):
            os.mkdir(appdata_path + "\\" + dir)


try:
    setup_dirs(all_dirs)
    logs = open(appdata_path + "\logs\setup.log", "w")

    with open(appdata_path + "\config\standard.json", "w") as template:
        template.write(json.dumps(standard, indent=2))
except Exception as e:
    print(e)
    sys.exit(0)


class Setup(QMainWindow):
    url_base = " /setup"

    def __init__(self):
        super(Setup, self).__init__()

        self.setWindowTitle("Setup")

        self.setFixedHeight(88)
        self.setFixedWidth(233)

        # set button and check box
        self.install = QPushButton("Install", self)
        self.developer_mode = QCheckBox("Develope mode", self)

        self.install.move(125, 25)
        self.developer_mode.move(10, 25)

        self.install.clicked.connect(self.install_clicked)

        self.show()

    def install_clicked(self):
        if self.developer_mode.isChecked():
            self.url_base += "/developer"
        else:
            self.url_base += "/normal"

        response = requests.get(self.url_base).content

        with open("neon_editor.zip", "wb") as file:
            file.write(response)
            file.close()

        ctypes.windll.user32.MessageBoxW(
            int(self.winId()), "Success", " Neon editor succesfully installed", 0
        )

        logs.write(f"{datetime.datetime.now()} neon editor installed - setup log")
        logs.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    setup = Setup()

    app.exec()
