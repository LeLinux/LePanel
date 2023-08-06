import sys

#import qdarktheme
from PySide6 import QtWidgets, QtGui, QtCore
import json5 as json


class LePanel(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.mainwidget = QtWidgets.QWidget(self)
        self.mainwidget.setStyleSheet("""QWidget{border-radius:12px;background:#FFFFFF;}""")

        self.setCentralWidget(self.mainwidget)


        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    #qdarktheme.setup_theme()

    app.setFont(QtGui.QFont("Ubuntu Mono"))

    lepanel = LePanel()
    lepanel.setFixedSize(1900, 25)
    lepanel.move(10, 50)
    lepanel.show()

    sys.exit(app.exec())
