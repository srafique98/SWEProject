from src.Window import Window
from src.Listing import Listing
from src.NewUser import NewUser
from src.User import User
from PySide6.QtWidgets import *


class Menu(Window):
    def __init__(self):
        #uiFileName = "ui/mainmenu.ui"
        uiFileName = "ui/signin.ui"
        super().__init__()
        self.nextWindow = None

        # Open application
        self.window = super().windowInit(uiFileName, self)
        self.window.startButton.clicked.connect(self.start)

        # Sign in 
        self.username = self.findChild(QLineEdit, "userNameBar")
        self.password = self.findChild(QLineEdit, "passwordBar")
        self.login = self.findChild(QPushButton, "loginButton")  # From mainwindow.ui
        self.login.clicked.connect(self.signIn)
        self.invalidSignIn = self.findChild(QLabel, "label_6")
        self.invalidSignIn.hide()

        # Sign up
        self.createAccount = self.findChild(QPushButton, "signUpButton")
        self.createAccount.clicked.connect(self.signUp)

    def signIn(self):
        currentUser = User()
        valid = currentUser.validateUserLogin(self.username.text(), self.password.text())
        if valid:
            #self.close()
            self.nextWindow = Listing(self.username.text(), self.password.text(), self.window)
            self.window.close()

        else: 
            self.invalidSignIn.show()

    def signUp(self):
        #self.close()
        self.nextWindow = NewUser(self.window)
        self.window.close()

    def start(self):
        self.close()
        self.nextWindow = Listing("eldenlord@souls.net", "moonviel", self.window)
        self.window.close()
        #super().nextWindow(self.window)




