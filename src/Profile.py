from src.Window import Window
from src.User import User 
from PySide6.QtWidgets import *


class Profile(Window):

    def __init__(self, parentWindow, email, password):
        uiFile = "ui/profilePage.ui"
        super().__init__()
        self.window = super().windowInit(uiFile, self)

        # User
        tempUser = User()
        validate = tempUser.validateUserLogin(email, password)
        self.user = self.findChild(QLabel, "user")
        self.user.setText(tempUser.getUserField("first_name"))

        # Summary 
        self.summary = self.findChild(QTextEdit, "summary")
        self.summary.setText(tempUser.getUserField("summary"))
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
        tempUser = User()
        self.summary.setReadOnly(True)
        #tempUser.updateLocalInfo()
        tempUser.changeUserData("summary", self.summary.toPlainText())
        
   
