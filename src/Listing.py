from tokenize import Double

from PySide6.QtCore import Slot

from src.Window import Window
from src.db_client import DB_Client
from src.Profile import Profile
from src.User import User
from PySide6.QtWidgets import *
from PySide6 import QtCore
from PySide6.QtGui import QIcon
from src.JobSummary import JobSummary
import gc


class Listing(Window):
    db_name = "Jobs"
    db_collection = "NewJobsPrt2"
    def __init__(self, email, password):
        uiFile = "ui/mainwindow.ui"
        super().__init__()
        self.window = super().windowInit(uiFile, self)

        self.connection = DB_Client(True, self.db_name, self.db_collection)
        self.jobButton = self.findChild(QPushButton, "pushButton")  # From mainwindow.ui
        self.jobs = self.connection.general_search({""}, {"job_title": 1, "sector": 1, "min_salary_range": 1,
                                                          "max_salary_range": 1})
        self.jobSummaries = []

        self.highlightedSummary = None
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
        suggestedJobs = self.connection.fil_location("")
        jobsList = []
        for someJobs in suggestedJobs:
            jobsList.append(someJobs["job_title"])
        suggestedJobSearch = QCompleter(jobsList, self)
        suggestedJobSearch.setFilterMode(QtCore.Qt.MatchContains)
        suggestedJobSearch.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.jobFilter = self.findChild(QLineEdit, "searchJobFilter")
        self.jobFilter.setCompleter(suggestedJobSearch)
        self.applyJobFil = self.findChild(QCheckBox, "applyJobFilter")

        # Location filter text and button
        suggestedLocations = self.connection.fil_location("")
        locationsList = []
        for someLocation in suggestedLocations:
            locationsList.append(someLocation["location"])

        suggestedLocationSearch = QCompleter(locationsList, self)
        suggestedLocationSearch.setFilterMode(QtCore.Qt.MatchContains)
        suggestedLocationSearch.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.locFilter = self.findChild(QLineEdit, "searchLocationFilter")
        self.locFilter.setCompleter(suggestedLocationSearch)
        self.applyLocFil = self.findChild(QCheckBox, "applyLocFilter")

        # Salary min and max filter text and button
        self.minSalaryFilter = self.findChild(QComboBox, "minComboBox")
        self.maxSalaryFilter = self.findChild(QComboBox, "maxComboBox")
        self.applySalaryFil = self.findChild(QCheckBox, "applySalaryFilter")

        # Remove filter
        self.removeFilterButton = self.findChild(QPushButton, "removeFilters")
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
        self.summaryScroll = self.findChild(QScrollArea, "summaryScroll")
        self.vertJobs = self.findChild(QVBoxLayout, "jobDisplay")

        self.descriptionScroll = self.findChild(QScrollArea, "descriptionScroll")
        self.jobDescription = self.descriptionScroll.findChild(QVBoxLayout, "jobDesc")
        self.jobTitle = self.findChild(QLabel, "jobTitle")
        self.fullDesc = self.findChild(QLabel, "fullDesc")
        self.salary = self.findChild(QLabel, "salary")
        self.numberOfEntries = self.findChild(QComboBox, "entriesPerPage")
        self.numberOfEntries.currentIndexChanged.connect(self.getSearch)
        self.nextPageButton = self.findChild(QPushButton, "nextPage")
        self.previousPageButton = self.findChild(QPushButton, "previousPage")
        self.nextPageButton.setIcon(QIcon("./media/forwardArrow.svg"))
        self.previousPageButton.setIcon(QIcon("./media/backArrow.svg"))
        self.nextPageButton.clicked.connect(self.nextPage)
        self.previousPageButton.clicked.connect(self.previousPage)

        # self.jobs = self.getJobs()
        print(self.jobs)

        for count, job in enumerate(self.jobs.collection.find().limit(int(self.numberOfEntries.currentText()))):
            self.createJobSummary(count, job)

    def nextPage(self):
        pass

    def previousPage(self):
        pass

    def handleClick(self, jobID):
        self.highlightSelected(jobID)
        self.displayDescription(jobID)

    def displayDescription(self, jobID):
        toDisplay = self.jobs.collection.find_one({"_id": jobID})
        title = toDisplay["job_title"]
        desc = toDisplay["job_description"]
        self.jobTitle.setText(str(title))
        self.fullDesc.setText(str(desc))
        minSal = (format(int(toDisplay["min_salary_range"]), ',d'))
        maxSal = (format(int(toDisplay["max_salary_range"]), ',d'))
        newSalary = '${minSal} - ${maxSal}'.format(minSal=minSal,
                                                   maxSal=maxSal)
        self.salary.setText(newSalary)
        print(str(jobID))

    def highlightSelected(self, jobID):
        # Go through the list of jobSummaries and find the one with jobID and then call a set color function on it
        jobToHighlight = None
        for job in self.jobSummaries:
            if job.getUID() == jobID:
                jobToHighlight = job
                break
        if self.highlightedSummary:
            self.highlightedSummary.toggleHighlight()
        self.highlightedSummary = jobToHighlight
        self.highlightedSummary.toggleHighlight()

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
             or self.applySalaryFil.isChecked()):
            salaryTemp = self.getSalaryKey()
            newJobs = self.connection.fil_search(self.getJobKeyword(), self.getLocationKey(),
                                                 salaryTemp[0], salaryTemp[1], {})
        for count, job in enumerate(newJobs):
            if count >= int(self.numberOfEntries.currentText()):
                break

            self.createJobSummary(count, job)

    def createJobSummary(self, count, job):
        newTitle = job["job_title"]
        newSector = job["sector"] if job["sector"] else "Sector not reported"
        minSal = (format(int(job["min_salary_range"]), ',d'))
        maxSal = (format(int(job["max_salary_range"]), ',d'))
        newSalary = '${minSal} - ${maxSal}'.format(minSal=minSal,
                                                   maxSal=maxSal)
        newUID = job["_id"]
        newJob = JobSummary(newTitle, newSector, newSalary, newUID, self)
        self.jobSummaries.append(newJob)
        self.jobSummaries[count].clicked.connect(lambda jobID=newUID: self.handleClick(jobID))
        self.vertJobs.addWidget(self.jobSummaries[count])


    def getJobKeyword(self):
        jobKeyword = self.jobFilter.text()
        return jobKeyword

    def getLocationKey(self):
        locationKeyword = self.locFilter.text()
        return locationKeyword

    def getSalaryKey(self):
        minSalaryKeyword = self.minSalaryFilter.currentText()
        tempMinSalary = minSalaryKeyword.replace('$', "")
        minSalary = tempMinSalary.replace(',', "")
        minSalary = float(minSalary)
        
        maxSalaryKeyword = self.maxSalaryFilter.currentText()
        tempMaxSalary = maxSalaryKeyword.replace('$', "")
        tempMaxSalary2 = tempMaxSalary.replace(',', "")
        maxSalary = tempMaxSalary2.replace('+', "0")  
        maxSalary = float(maxSalary)
        
        #print(minSalary,maxSalary)
        if maxSalary > 100000:
            maxSalary = 249500000
        return minSalary, maxSalary    
    
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
        for i in range(len(self.jobSummaries)-1, -1, -1):
            self.jobSummaries[i].deleteLater()
            self.highlightedSummary = None
        self.jobSummaries.clear()

    def viewProfile(self):
        self.close()
        self.nextWindow = Profile(self.window, self.currentUser, self.currentPass)
        super().nextWindow(self.window)
     

