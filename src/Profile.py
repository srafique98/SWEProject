from argparse import FileType
from src.Window import Window
from src.User import User 
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui
import sys


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

        self.resumeButton = self.findChild(QPushButton, "pushButton")
        self.filePath = self.findChild(QLabel, "label_6")

        # click upload resume button
        self.resumePath = self.resumeButton.clicked.connect(self.getResumePath)

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

    def getResumePath(self):
        self.app = QApplication.instance()
        self.app.setQuitOnLastWindowClosed(False)
        resumeFullPath, resumeType = QFileDialog.getOpenFileNames(self)
        if resumeFullPath:
            # print("--", resumeFullPath)
            self.filePath.setText(str(resumeFullPath))
        self.app.setQuitOnLastWindowClosed(True)
        return resumeFullPath
        
        
   
