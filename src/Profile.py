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

        self.currentUser = email 
        self.currentPass =  password
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
        
        # click upload resume button
        self.resumeButton = self.findChild(QPushButton, "pushButton")
        self.filePath = self.findChild(QLabel, "resumeUploaded")
        self.resumePath = self.resumeButton.clicked.connect(self.getResumePath)

        self.coverLetterButton = self.findChild(QPushButton,"pushButton_2")
        self.filePath2 = self.findChild(QLabel,"letterUploadedButton")
        self.coverLetter = self.coverLetterButton.clicked.connect(self.getLetterPath)

        # Return
        self.parentWindow = parentWindow
        self.returnToListing = self.findChild(QPushButton, "returnButton")
        self.returnToListing.clicked.connect(self.testBack)

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
        tempUser = User()
        self.app = QApplication.instance()
        self.app.setQuitOnLastWindowClosed(False)
        resumeFullPath, resumeType = QFileDialog.getOpenFileNames(self)
        if resumeFullPath:
            validate = tempUser.validateUserLogin(self.currentUser, self.currentPass)
            self.filePath.setText(str(resumeFullPath))
            path = str(resumeFullPath)
            exclude = ["[","]","'"]
            for index in range(len(exclude)):
                path = path.replace(exclude[index],"")
            tempUser.uploadResume(path)
        self.app.setQuitOnLastWindowClosed(True)
       
        return resumeFullPath

    def getLetterPath(self):
        tempUser = User()
        self.app = QApplication.instance()
        self.app.setQuitOnLastWindowClosed(False)
        coverLetterFullPath, resumeType = QFileDialog.getOpenFileNames(self)
        if coverLetterFullPath:
            self.filePath2.setText(str(coverLetterFullPath))
            validate = tempUser.validateUserLogin(self.currentUser, self.currentPass)
            self.filePath2.setText(str(coverLetterFullPath))
            path = str(coverLetterFullPath)
            exclude = ["[","]","'"]
            for index in range(len(exclude)):
                path = path.replace(exclude[index],"")
            tempUser.uploadLetter(path)
        self.app.setQuitOnLastWindowClosed(True)
        return coverLetterFullPath
        
        
   
