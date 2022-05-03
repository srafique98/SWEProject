import sys
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

    def windowInit(self, uiFileName, where=None):
        uiFile = QFile(uiFileName)
        if not uiFile.open(QIODevice.ReadOnly):
            print(f"Cannot open {uiFileName}: {uiFile.errorString()}")
            sys.exit(-1)
        loader = QUiLoader()
        window = loader.load(uiFile, where)
        uiFile.close()
        if not window:
            print(loader.errorString())
            sys.exit(-1)
        window.show()
        return window
