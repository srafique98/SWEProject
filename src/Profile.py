from argparse import FileType
from src.Window import Window
from src.User import User 
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui
import pypdfium2 as pdfium


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

        self.status = tempUser.getUserField("resume")
        self.statusPDF = self.findChild(QLabel, "statusPDF")
        if(self.status == None):
            self.statusPDF.setText("Not Applied")
        else: 
            self.statusPDF.setText("Applied")

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
        resumePng = "resume_1.jpg"
        self.app = QApplication.instance()
        self.app.setQuitOnLastWindowClosed(False)

        resumePdf, resumeType = QFileDialog.getOpenFileName(
            parent=self,
            caption="Choose a Resume",
            filter = "PDF Files (*.pdf)"
        )
        if resumePdf:
            self.filePath.setText(resumePdf)
            validate = tempUser.validateUserLogin(self.currentUser, self.currentPass)
            tempUser.uploadResume(resumePdf)
            self.statusPDF.setText("Applied")

        self.app.setQuitOnLastWindowClosed(True)
        self.pdfToPng(resumePdf,resumePng)
        plzUploadLabel = self.findChild(QLabel, "jobTitle")
        pixma =  QtGui.QPixmap(resumePng)
        plzUploadLabel.setPixmap(pixma)
        return resumePdf

    def pdfToPng(self,pdfPath, outPutFileName):
        with pdfium.PdfContext(pdfPath) as pdf:
            image = pdfium.render_page_topil(pdf,0)
            image.save(outPutFileName)

    def getLetterPath(self):
        tempUser = User()
        coverLetterPng = "coverLetter_1.png"
        self.app = QApplication.instance()
        self.app.setQuitOnLastWindowClosed(False)

        coverLetterPdf, resumeType = QFileDialog.getOpenFileName(
            parent=self,
            caption="Choose a Resume",
            filter = "PDF Files (*.pdf)"
        )
        if coverLetterPdf:
            self.filePath2.setText(coverLetterPdf)
            validate = tempUser.validateUserLogin(self.currentUser, self.currentPass)
            tempUser.uploadLetter(coverLetterPdf)
        
        self.app.setQuitOnLastWindowClosed(True)
        self.pdfToPng(coverLetterPdf,coverLetterPng)
        plzUploadLabel = self.findChild(QLabel, "jobTitle")
        pixma =  QtGui.QPixmap(coverLetterPng)
        plzUploadLabel.setPixmap(pixma)
        return coverLetterPdf
        
        
