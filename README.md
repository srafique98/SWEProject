[![Python application](https://github.com/comp129/customer-project-rayquaza/actions/workflows/python-app.yml/badge.svg)](https://github.com/comp129/customer-project-rayquaza/actions/workflows/python-app.yml)
# Overview

Team Rayquaza consists of David Leavenworth, Sean Higley, Shan Rafique, and Jesus Torres. With the help of our customer, Benjamin Vu, we developed and application in Python named JobSeeker. JobSeeker allows the user to sign up, or log in with an existing account, to search for a new job in a large database holding hundreds of positions. The user can filter out positions they seek and would wish to apply for. With these options, a user can find their dream position in their selected location and preferred salary. There will be no need for the user to upload a resume for each position they apply to. For the user who wishes to apply to more than one job, they have the freedom to quickly apply to as many positions as they desire.

# Implementations
## Signup/Login 

## Filters
###### Position: 
###### Location:
###### Salary Range: 

## Job Listings
###### Selection:
###### Paganation:

## Quick Apply

## Profile

## Database 


# Documents  

Technical debt assignment found [here](https://github.com/comp129/customer-project-rayquaza/blob/main/docs/techDebt.md)

Customer Notes found [here](https://github.com/comp129/customer-project-rayquaza/blob/main/CustomerNotes.md)

Sprint specific information found [here](https://github.com/comp129/customer-project-rayquaza/blob/main/docs/Sprints.md)

Traditional report found [here](https://github.com/comp129/customer-project-rayquaza/blob/main/docs/report.md)
 
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

Packages 3-5 can be installed by running ``pipenv shell && pipenv install`` from a CLI when in the root directory of this project.
