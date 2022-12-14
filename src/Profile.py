from argparse import FileType
from src.Window import Window
from src.User import User 
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui
import pypdfium2 as pdfium
import aspose.words as aw

class Profile(Window):
    def __init__(self, parentWindow, email, password):
        uiFile = "ui/profilePage.ui"
        super().__init__()
        self.window = super().windowInit(uiFile, self)

        # User
        tempUser = User()
        self.app = QApplication.instance()

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
        self.plzUploadLabel = self.findChild(QLabel, "jobTitle")

        self.status = tempUser.getUserField("resume")
        self.statusPDF = self.findChild(QLabel, "statusPDF")
        if self.status is None:
            self.statusPDF.setText("Not Applied")
        else: 
            self.statusPDF.setText("Applied")
            tempUser.downloadResume("")
            resumePng = "resume_1.jpg"
            self.pdfToPng("pdf_download.pdf",resumePng)
            self.displayToScreen(resumePng)

        self.coverLetterButton = self.findChild(QPushButton,"pushButton_2")
        self.filePath2 = self.findChild(QLabel,"letterUploadedButton")
        self.coverLetter = self.coverLetterButton.clicked.connect(self.getLetterPath)

        # Return
        self.parentWindow = parentWindow
        self.returnToListing = self.findChild(QPushButton, "returnButton")
        self.returnToListing.clicked.connect(self.returnToPrevWindow)

    def returnToPrevWindow(self):
        self.window.close()
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
        self.app.setQuitOnLastWindowClosed(False)

        resumePdf, resumeType = QFileDialog.getOpenFileName(
            parent=self,
            caption="Choose a Resume",
            filter="PDF Files (*.pdf);; docx Files (*.docx)"
        )
        if resumePdf:
            self.filePath.setText(resumePdf)
            validate = tempUser.validateUserLogin(self.currentUser, self.currentPass)
            self.statusPDF.setText("Applied")
        else:
            return None
        
        self.app.setQuitOnLastWindowClosed(True)
        if "PDF" in resumeType:
            tempUser.uploadResume(resumePdf)
            self.pdfToPng(resumePdf,resumePng)
            self.displayToScreen(resumePng)
        elif "docx" in resumeType:
            self.wordToPDF(resumePdf,"resume_1.pdf")
            tempUser.uploadResume("resume_1.pdf")
            self.pdfToPng("resume_1.pdf",resumePng)
            self.displayToScreen(resumePng)
            return "resume_1.pdf"
        return resumePdf

    def displayToScreen(self,outPuFile):
            pixma =  QtGui.QPixmap(outPuFile)
            self.plzUploadLabel.setPixmap(pixma)

    def pdfToPng(self,pdfPath, outPutFileName):
        with pdfium.PdfContext(pdfPath) as pdf:
            image = pdfium.render_page_topil(pdf,0)
            image.save(outPutFileName)

    def wordToPDF(self,docxPath, outPutFileName):
        doc = aw.Document(docxPath)
        doc.save(outPutFileName)

    def getLetterPath(self):
        tempUser = User()
        coverLetterPng = "coverLetter_1.png"
        self.app.setQuitOnLastWindowClosed(False)

        coverLetterPdf, CoverLetterType = QFileDialog.getOpenFileName(
            parent=self,
            caption="Choose a Cover Letter",
            filter="PDF Files (*.pdf);; docx Files (*.docx)"
        )
        if coverLetterPdf:
            self.filePath2.setText(coverLetterPdf)
            validate = tempUser.validateUserLogin(self.currentUser, self.currentPass)
            tempUser.uploadLetter(coverLetterPdf)
        else:
            return None
        
        if "PDF" in CoverLetterType:
            tempUser.uploadResume(coverLetterPdf)
            self.pdfToPng(coverLetterPdf,coverLetterPng)
            self.displayToScreen(coverLetterPng)
        elif "docx" in CoverLetterType:
            self.wordToPDF(coverLetterPdf,"coverLetter_1.pdf")
            tempUser.uploadResume("coverLetter_1.pdf")
            self.pdfToPng("coverLetter_1.pdf",coverLetterPng)
            self.displayToScreen(coverLetterPng)
            return "coverLetter_1.pdf"
        return coverLetterPdf


        
        
