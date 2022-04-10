from tokenize import Double
from src.Window import Window
from src.db_client import DB_Client
from PySide6.QtWidgets import *
#from PySide6.QtCore import *
from PySide6 import QtCore
from src.Job import Job


class Listing(Window):
    def __init__(self):
        uiFile = "ui/mainwindow.ui"
        super().__init__()
        self.window = super().windowInit(uiFile, self)

        self.connection = DB_Client(True, "Jobs", "NewJobs")
        self.jobButton = self.findChild(QPushButton, "pushButton")  # From mainwindow.ui
        self.jobs = self.connection.general_search({""}, {"job_title": 1, "sector": 1, "min_salary_range": 1,
                                                          "max_salary_range": 1})
        self.jobSummaries = []

        # Search text and button
        self.searchBar = self.findChild(QLineEdit, "searchBar")
        self.searchButton = self.findChild(QPushButton, "searchButton")  # From mainwindow.ui
        self.searchButton.clicked.connect(self.getSearch)

        # Field filter text and button
        self.jobFilter = self.findChild(QLineEdit, "filter")
        self.jobTypeButton = self.findChild(QPushButton, "jobTypeButton")  # From mainwindow.ui
        self.jobTypeButton.clicked.connect(self.getJobFilter)

        # Location filter text and button
        self.locFilter = self.findChild(QLineEdit, "filter_2")
        self.locationTypeButton = self.findChild(QPushButton, "locationTypeButton")  # From mainwindow.ui
        self.locationTypeButton.clicked.connect(self.getLocFilter)

        # Salary filter  text and button
        self.salaryFilter = self.findChild(QLineEdit, "filter_3")
        self.salaryButton = self.findChild(QPushButton, "salaryTypeButton")  # From mainwindow.ui
        self.salaryButton.clicked.connect(self.getSalaryFilter)

        self.scrollArea = self.findChild(QScrollArea, "scrollArea")
        self.vertJobs = self.findChild(QVBoxLayout, "jobDisplay")

        for count, document in enumerate(self.jobs.collection.find()):
            newTitle = document["job_title"]
            newSector = document["sector"] if document["sector"] else "Sector not reported"
            newSalary = '{minSal} - {maxSal}'.format(minSal=document["min_salary_range"],
                                                     maxSal=document["max_salary_range"])
            self.jobSummaries.append(Job(newTitle, newSector, newSalary))

        for i in range(0, 20):
            self.vertJobs.addWidget(self.jobSummaries[i])

    # Stores text field
    def getSearch(self):
        searchKeyword = self.searchBar.text()
        document = self.connection.general_search(searchKeyword, {})
        for field in document:
            print(field["job_title"], field["location"])  # or do something with the document

    # Stores text field
    def getLocFilter(self):
        locKeyword = self.locFilter.text()
        document = self.connection.fil_location(locKeyword)
        for field in document:
            print(field["job_title"], field["location"])
        #print(locKeyword)

    # Stores text field
    def getSalaryFilter(self):
        salaryKeyword = self.salaryFilter.text()
        min_sal, max_sal = salaryKeyword.split('-', 1)
        #print(min_sal,max_sal)
        min_sal = float(min_sal)
        max_sal = float(max_sal)
        document = self.connection.fil_salary_range(min_sal, max_sal)
        for field in document:
            print(field["job_title"], field["location"], field["min_salary_range"], field["max_salary_range"])
        #print(salaryKeyword)

    def getJobFilter(self):
        fieldKeyword = self.jobFilter.text()
        document = self.connection.fil_sect_profession(fieldKeyword)
        for field in document:
            print(field["job_title"], field["location"])
        #(fieldKeyword)
