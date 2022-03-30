from PySide6.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Job project"
        self.top = 100
        self.left = 100
        self.width = 970
        self.height = 690

    def mainWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def nextWindow(self, nextWindow):
        self.w = nextWindow
        self.hide()
        self.w.show()
