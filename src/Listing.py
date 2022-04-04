from Window import Window
from db_client import DB_Client
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

class Listing(Window):
    def __init__(self):
        uiFile = "../ui/mainwindow.ui"
        super().__init__()
        self.window = super().windowInit(uiFile, self)
        # self.window.show()

        self.connection = DB_Client(True)
        self.jobButton = self.findChild(QPushButton,"pushButton") # From mainwindow.ui
        self.cursor = self.connection.dbCollection.find({})

        # DO Something
        self.jobButton.clicked.connect(self.displayAJob)

    @Slot()
    def displayAJob(self):
        obj = next(self.cursor, None)
        if obj:
            print(obj)
