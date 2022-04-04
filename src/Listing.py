from sqlite3 import Cursor
from Window import Window
from db_client import DB_Client

import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

class Listing(Window):  # inheritance from window class
    def __init__(self):
        uiFile = "../ui/mainwindow.ui"
        super().__init__()      # implicitly calling the parent class
        self.window = super().windowInit(uiFile, self)
        # self.window.show()

        self.connection = DB_Client(True)
        self.job_button = self.findChild(QPushButton,"pushButton")
        self.cursor = self.connection.dbCollection.find({})

        # DO Something
        self.job_button.clicked.connect(self.display_a_job)

    @Slot()
    def display_a_job(self):
        obj = next(self.cursor, None)   # if no next then make obj = None
        if obj:
            print(obj)
        # for document in self.cursor:
        #     print(document)
        #     break
        # print(self.cursor.hasNext()) self.cursor = self.connection.dbCollection


app = QApplication(sys.argv)
window = Listing()
window.show()
sys.exit(app.exec())
