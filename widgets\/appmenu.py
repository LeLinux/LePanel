from PySide6 import QtWidgets, QtGui, QtCore
import subprocess as sb


class AppMenu(QtWidgets.QToolButton):
    def __init__(self):
        super().__init__()
        self._icon = None

        self.clicked.connect(self.openMenu)
        self.setText("|Le|")

    def openMenu(self):
        sb.call(["rofi", "-show", "drun"])
