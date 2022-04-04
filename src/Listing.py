from Window import Window
from db_client import DB_Client
from PySide6.QtWidgets import *
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
         
        # Search text and button
        self.searchBar = self.findChild(QTextEdit, "searchBar")
        self.searchButton = self.findChild(QPushButton,"searchButton") # From mainwindow.ui
        self.searchButton.clicked.connect(self.getSearch)
        
        # Field filter text and button
        self.fieldFilter = self.findChild(QTextEdit, "filter")
        self.jobTypeButton = self.findChild(QPushButton,"jobTypeButton") # From mainwindow.ui
        self.jobTypeButton.clicked.connect(self.getFieldFilter)
        
        # Location filter text and button
        self.locFilter = self.findChild(QTextEdit, "filter_2")
        self.locationTypeButton = self.findChild(QPushButton,"locationTypeButton") # From mainwindow.ui
        self.locationTypeButton.clicked.connect(self.getLocFilter)
        
        # Salary filter  text and button
        self.salaryFilter = self.findChild(QTextEdit, "filter_3")
        self.salaryButton = self.findChild(QPushButton,"salaryTypeButton") # From mainwindow.ui
        self.salaryButton.clicked.connect(self.getSalaryFilter)



    # Stores text field
    def getSearch(self):
        searchKeyword = self.searchBar.toPlainText()
        print(searchKeyword)

     # Stores text field
    def getLocFilter(self):
        locKeyword = self.locFilter.toPlainText()
        print(locKeyword)

    # Stores text field
    def getSalaryFilter(self):
        salaryKeyword = self.salaryFilter.toPlainText()
        print(salaryKeyword)    
    
    def getFieldFilter(self):
        fieldKeyword = self.fieldFilter.toPlainText()
        print(fieldKeyword) 

    @Slot()
    def displayAJob(self):
        obj = next(self.cursor, None)
        if obj:
            print(obj)
