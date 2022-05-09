[![Python application](https://github.com/comp129/customer-project-rayquaza/actions/workflows/python-app.yml/badge.svg)](https://github.com/comp129/customer-project-rayquaza/actions/workflows/python-app.yml)
# Overview

Team Rayquaza consists of David Leavenworth, Sean Higley, Shan Rafique, and Jesus Torres. With the help of our customer, Benjamin Vu, we developed and application in Python named JobSeeker. JobSeeker allows the user to sign up, or log in with an existing account, to search for a new job in a large database holding hundreds of positions. The user can filter out positions they seek and would wish to apply for. With these options, a user can find their dream position in their selected location and preferred salary. There will be no need for the user to upload a resume for each position they apply to. For the user who wishes to apply to more than one job, they have the freedom to quickly apply to as many positions as they desire.

# Implementations
## Signup/Login

![Home Screen](media/images/homeScreen.png)
 
![Sign Up Screen](media/images/signUpScreen.png)
 
JobSeeker allows a returning user to login into their account and access the many jobs the application has to offer. When a user attempts to sign in with a non-existent account or with invalid credentials, then the user will not be allowed access. If the user is new, then they can sign up and create a new account that will be saved in our database. 

## Filters
### Position:
![Position Filter](media/images/positionFilter.png)
 
For job seekers who want to narrow down the search results for their dream job, we have added a filter to populate the results to your specifications. No need to search through a list of positions that you are not interested in. With suggested searches, we will recommend search options for a job we believe the user is interested in.
  
### Location:
![Location Filter](media/images/locationFilter.png)
  
For users who want to work near home, or far away from home, we added a filter for locations when searching for jobs. Compared to the position filter, the location filter works very similarly. With suggested searches, we will recommend search options for a location we believe the user is interested in. 
  
### Salary Range: 
![Salary Range](media/images/salaryRange.png)
 
One of the most important factors when searching for a job is the salary offered for the position. For the user who wants to seek a preferred salary, they can filter out jobs that don't fit their criteria. No need to search for a job that will not pay the salary you seek. With hundreds of jobs in our database, we have filters ranging from $0-100,000+. Jobs ranging over $100,000 reach a salary of $20,000,000+.
 
## Job Listings
![Pagination](media/images/paganation.png)
 
### Selection:
Once a user searches for a job, or they decide to look at the position already on screen, the user can click and select a position from the listings. The selected position will populate the portion of the screen to the right of the listing. We will see the position title, salary range, and a description of the position. If the user wishes to see another job, the user can change by clicking on a different position; the process will repeat once done.

### Pagination:
Following the same process as the selection option, pagination allows the user to browse more jobs, rather than the first few results. With the option to adjust the size of the populate list, the user can now navigate to a larger list to search through. If the user wishes to see even more listings, there are arrow keys provided to allow the user to flip through the results in intervals of the size set.
  
## Quick Apply
For the user that wishes to apply to as many places as possible, in a timely manner, we have a quick apply function. The quick apply button will apply to the job selected on the screen. If the quick apply button is clicked, the application will upload the user information to the position, meaning the position will record that the user applied to that job. This can be done on as many jobs as the user desires.
  
## Profile
![Profile Screen](media/images/profileScreen.png)
  
On the profile page, all the user information will be stored. Since our purpose is to help those who are seeking a job, we have all the needs for a profile page. The profile page includes three sections: a modifiable summary; an upload for a resume as a PDF, and an optional cover letter. If the user wishes to change any of their information, they can do so. The summary and resume are always on display for the user. There were plans to add a section for the jobs applied to the user, but do to deadlines we failed to include the extra feature.
  
# Documents  
Technical debt assignment found [here](/docs/techDebt.md)

Customer Notes found [here](/docs/CustomerNotes.md)

Sprint specific information found [here](/docs/Sprints.md)

Traditional report found [here](/docs/report.md)
 
# Customer interaction with the application
1. Not deployable as of right now
2. Will host DB on the cloud (24/7 access from the cloud rather than our local host)
3. Will interact through an executable
    - For Windows, it be packaged as a .exe file
    - For Macs, it will be packaged as a .app file
    - For Linux, it will be packaged as a Linux distribution

# Software needed to run the application
1. Install [Python 3.10](https://www.python.org/downloads/release/python-3104/)
2. Install [Pipenv](https://pypi.org/project/pipenv/) via ``pip install pipenv``
3. [PySide6](https://pypi.org/project/PySide6/) 
4. [PyMongo](https://pypi.org/project/pymongo/)
5. [Certifi](https://pypi.org/project/certifi/)
6. [PyPdfium2](https://pypi.org/project/pypdfium2/)
7. [aspose-words](https://pypi.org/project/aspose-words/)
8. [PyQtDarkTheme](https://pypi.org/project/pyqtdarktheme/)

Packages 3-8 can be installed by running ``pipenv shell && pipenv install`` from a CLI when in the root directory of this project.
