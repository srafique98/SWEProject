from tokenize import Double

from PySide6.QtCore import Slot

from src.Window import Window
from src.db_client import DB_Client
from src.Profile import Profile
from src.User import User
from PySide6.QtWidgets import *
from PySide6 import QtCore
from src.JobSummary import JobSummary


class Listing(Window):
    def __init__(self, email, password):
        uiFile = "ui/mainwindow.ui"
        super().__init__()
        self.window = super().windowInit(uiFile, self)

        self.connection = DB_Client(True, "Jobs", "NewJobs")
        self.jobButton = self.findChild(QPushButton, "pushButton")  # From mainwindow.ui
        self.jobs = self.connection.general_search({""}, {"job_title": 1, "sector": 1, "min_salary_range": 1,
                                                          "max_salary_range": 1})
        self.jobSummaries = []
        # User 
        self.user = self.findChild(QLabel, "label")
        tempUser = User()
        self.currentUser = email 
        self.currentPass =  password
        validate = tempUser.validateUserLogin(email, password)
        self.user.setText(tempUser.getUserField("first_name"))

        # Search text and button
        self.searchBar = self.findChild(QLineEdit, "searchBar")
        self.searchButton = self.findChild(QPushButton, "searchButton")  # From mainwindow.ui
        self.searchButton.clicked.connect(self.getSearch)

        # Job filter text and button
        self.jobFilter = self.findChild(QLineEdit, "searchJobFilter")
        self.jobTypeButton = self.findChild(QPushButton, "jobTypeButton")  # From mainwindow.ui
        self.jobTypeButton.clicked.connect(self.getJobFilter)
        self.applyJobFil = self.findChild(QCheckBox, "applyJobFilter")
        # Location filter text and button
        self.locFilter = self.findChild(QLineEdit, "searchLocationFilter")
        self.locationTypeButton = self.findChild(QPushButton, "locationTypeButton")  # From mainwindow.ui
        self.locationTypeButton.clicked.connect(self.getLocFilter)
        self.applyLocFil = self.findChild(QCheckBox, "applyLocFilter")

        # Salary min and max filter text and button
        self.minSalaryFilter = self.findChild(QComboBox, "minComboBox")
        self.maxSalaryFilter = self.findChild(QComboBox, "maxComboBox")
        self.salaryButton = self.findChild(QPushButton, "salaryTypeButton")  # From mainwindow.ui
        self.salaryButton.clicked.connect(self.getSalaryFilter)
        self.applySalaryFil = self.findChild(QCheckBox, "applySalaryFilter")

        # Remove filter
        self.removeFilterButton = self.findChild(QPushButton,"removeFilters")
        self.removeFilterButton.clicked.connect(self.removeFilters)
        self.applyAllFilterButton = self.findChild(QPushButton, "allFilters")
        self.applyAllFilterButton.clicked.connect(self.applyAllFilters)

        # Error message
        self.invalidSalary = self.findChild(QLabel, "invalidSalaryLabel")
        self.invalidSalary.hide()

        # Profile
        self.name = self.findChild(QLabel, "label")
        self.profileButton = self.findChild(QPushButton, "profileButton")
        self.profileButton.clicked.connect(self.viewProfile)

        # List view 
        self.scrollArea = self.findChild(QScrollArea, "scrollArea")
        self.vertJobs = self.findChild(QVBoxLayout, "jobDisplay")

        self.jobDescription = self.findChild(QFrame, "jobDesc")
        self.jobTitle = self.jobDescription.findChild(QLabel, "jobTitle")

        # self.jobs = self.getJobs()
        print(self.jobs)

        for count, document in enumerate(self.jobs.collection.find().limit(20)):
            newTitle = document["job_title"]
            newSector = document["sector"] if document["sector"] else "Sector not reported"
            newSalary = '{minSal} - {maxSal}'.format(minSal=document["min_salary_range"],
                                                     maxSal=document["max_salary_range"])
            uid = document["_id"]
            newJob = JobSummary(newTitle, newSector, newSalary, uid)
            newJob.clicked.connect(lambda jobID=uid: self.displayJobDesc(jobID))
            self.jobSummaries.append(newJob)
            self.vertJobs.addWidget(self.jobSummaries[count])

    def displayJobDesc(self, jobID):
        toDisplay = self.jobs.collection.find_one({"_id": jobID})
        title = toDisplay["job_title"]
        self.jobTitle.setText(str(title))
        print(str(jobID))

    # Stores text field
    def getSearch(self):
        self.clearSummaries()
        newJobs = []

        if((not self.applyJobFil.isChecked()) and (not self.applyLocFil.isChecked()) 
                                                and (not self.applySalaryFil.isChecked())):
            searchKeyword = self.searchBar.text()
            newJobs = self.connection.general_search(searchKeyword, {})
        # else if 
        elif((self.applyJobFil.isChecked() or self.applyLocFil.isChecked())
                                                or (self.applySalaryFil.isChecked())): 
            salaryTemp = self.getSalaryKey()
            newJobs = self.connection.fil_search(self.getJobKeyword(), self.getLocationKey(),
                                                            salaryTemp[0], salaryTemp[1], {})
        for count, job in enumerate(newJobs):
            if count >= 20:
                break

            newTitle = job["job_title"]
            newSector = job["sector"] if job["sector"] else "Sector not reported"
            newSalary = '{minSal} - {maxSal}'.format(minSal=job["min_salary_range"],
                                                     maxSal=job["max_salary_range"])
            newJob = JobSummary(newTitle, newSector, newSalary)
            newJob.clicked.connect(self.displayJobDesc)
            self.jobSummaries.append(newJob)
            self.vertJobs.addWidget(self.jobSummaries[count])
    
    
    
    def getJobKeyword(self):
        jobKeyword = self.jobFilter.text()
        return jobKeyword

    def getLocationKey(self):
        locationKeyword = self.locFilter.text()
        return locationKeyword

    def getSalaryKey(self):
        minSalaryKeyword = self.minSalaryFilter.currentText()
        minSalary = minSalaryKeyword.replace(',', "")
        minSalary = float(minSalary)
        
        maxSalaryKeyword = self.maxSalaryFilter.currentText()
        maxSalary = maxSalaryKeyword.replace(',', "") 
        maxSalary = float(maxSalary)
        #print(minSalary,maxSalary)
        return minSalary, maxSalary    
  
    def getJobFilter(self):
        document = self.connection.fil_sect_profession(self.getJobKeyword())
        for field in document:
            print(field["job_title"], field["location"])
        #(fieldKeyword)

    def getLocFilter(self):
        document = self.connection.fil_location(self.getLocationKey())
        for field in document:
            print(field["job_title"], field["location"])
        #print(locKeyword)

    # Stores text field
    def getSalaryFilter(self):
        salary = self.getSalaryKey()
        # Max must be higher
        if(salary[0] < salary[1]):
            self.invalidSalary.hide()
            document = self.connection.fil_salary_range(salary[0], salary[1])
            for field in document:
                print(field["job_title"], field["location"], field["min_salary_range"], field["max_salary_range"])
        else: 
            self.invalidSalary.show()
    
    def removeFilters(self):
        self.applyJobFil.setChecked(False)
        self.applyLocFil.setChecked(False)
        self.applySalaryFil.setChecked(False)

        self.jobFilter.setText("")
        self.locFilter.setText("")

    def applyAllFilters(self):
        self.applyJobFil.setChecked(True)
        self.applyLocFil.setChecked(True)
        self.applySalaryFil.setChecked(True)


    def clearSummaries(self):
        for job in self.jobSummaries:
            job.deleteLater()
        self.jobSummaries.clear()

    def viewProfile(self):
        self.close()
        self.nextWindow = Profile(self.window, self.currentUser, self.currentPass)
        super().nextWindow(self.window)


