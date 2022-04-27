from src.Window import Window
from src.Listing import Listing
from src.User import User
from PySide6.QtWidgets import *
from src.Listing import Profile
import re


class NewUser(Window):

    def __init__(self):
        uiFile = "ui/signup.ui"
        super().__init__()
        self.window = super().windowInit(uiFile, self)
        
        # Create account
        self.firstName = self.findChild(QLineEdit, "firstNameBar")
        self.lastName = self.findChild(QLineEdit, "lastNameBar")
        self.email = self.findChild(QLineEdit, "userNameBar")
        self.password = self.findChild(QLineEdit, "passwordBar")
        self.newProfile = self.findChild(QPushButton, "createButton")  # From mainwindow.ui
        self.newProfile.clicked.connect(self.createProfile)

        self.pdf = self.findChild(QPushButton, "pdfButton")
        self.pdf.hide()
        self.pdf.clicked.connect(self.uploadPDF)

        self.login = self.findChild(QPushButton,"returnButton")
        self.login.hide()
        self.login.clicked.connect(self.loginNewUser)


    def emailValidation(self, strEmail):
        reg = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(reg,strEmail)):   
            print("Valid Email")
            newProfile = User()
            newProfile.signUp(self.email.text(),self.password.text(),
                            self.firstName.text(),self.lastName.text())
            self.login.show()
            self.pdf.show()
            self.firstName.setReadOnly(True)
            self.lastName.setReadOnly(True)
            self.email.setReadOnly(True)
            self.password.setReadOnly(True)   
        else:   
            print("Invalid Email") 
            # Prompt error  
        
    def createProfile(self):
        if(len(self.email.text()) == 0 or len(self.lastName.text()) == 0 
        or len(self.password.text()) == 0 or len(self.lastName.text()) == 0):
            print("Not valid")
        else: 
            self.emailValidation(self.email.text())
            
            # Read Only after create
    
    def loginNewUser(self):
        self.close()
        self.nextWindow = Listing(self.email.text(),self.password.text())
        super().nextWindow(self.window)

    def uploadPDF(self): 
        tempUser = User()
        self.app = QApplication.instance()
        self.app.setQuitOnLastWindowClosed(False)

        resumePdf, resumeType = QFileDialog.getOpenFileName(
            parent=self,
            caption="Choose a Resume",
            filter = "PDF Files (*.pdf)"
        )
        if resumePdf:
            validate = tempUser.validateUserLogin(self.email.text(), self.password.text())
            tempUser.uploadResume(resumePdf)

        self.app.setQuitOnLastWindowClosed(True)      

