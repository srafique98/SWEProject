from src.Window import Window
from PySide6.QtWidgets import *


class Profile(Window):

    def __init__(self):
        uiFile = "ui/profilePage.ui"
        super().__init__()
        self.window = super().windowInit(uiFile, self)

        self.summary = self.findChild(QTextEdit, "summary")

        self.modifySummary = self.findChild(QPushButton, "modifySummary")
        self.modifySummary.clicked.connect(self.modifyData)

        self.saveSummary = self.findChild(QPushButton, "saveSummary")
        self.saveSummary.clicked.connect(self.saveData)
    
    def modifyData(self):
        self.summary.setReadOnly(False)

    def saveData(self):
        self.summary.setReadOnly(True)

   
