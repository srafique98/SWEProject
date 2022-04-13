from src.Window import Window
from PySide6.QtWidgets import *


class Profile(Window):

    def __init__(self, parentWindow):
        uiFile = "ui/profilePage.ui"
        super().__init__()
        self.window = super().windowInit(uiFile, self)

        self.summary = self.findChild(QTextEdit, "summary")

        self.modifySummary = self.findChild(QPushButton, "modifySummary")
        self.modifySummary.clicked.connect(self.modifyData)

        self.saveSummary = self.findChild(QPushButton, "saveSummary")
        self.saveSummary.clicked.connect(self.saveData)

        self.parentWindow = parentWindow

    def testBack(self):
        super().nextWindow(self.window)
        self.parentWindow.show()
    
    def modifyData(self):
        self.summary.setReadOnly(False)

    def saveData(self):
        self.summary.setReadOnly(True)

   
