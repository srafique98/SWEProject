[![Python application](https://github.com/comp129/customer-project-rayquaza/actions/workflows/python-app.yml/badge.svg)](https://github.com/comp129/customer-project-rayquaza/actions/workflows/python-app.yml)
# This is the repo for Rayquaza

Technical debt assignment found [here](https://github.com/comp129/customer-project-rayquaza/blob/main/docs/techDebt.md)

Customer Notes found [here](https://github.com/comp129/customer-project-rayquaza/blob/main/CustomerNotes.md)


# Sprint 1 March 29th - April 5th:
## What was Completed:
  - [x] [13 points] Story 1: Preparation/DB Setup 
        
  - Create the mongoDB structure and collections hosted in an online cluster. 
  - [x] [8 points] Story 3: text filter: Profession/Field Query 
  
  - Create a python mongoDB query to acquire documents based on Profession
  - [x] [8 points] Story 4: Filter: Location Query
  
  - Create a python mongoDB query to acquire documents based on Location
  - [x] [13 points] Story 5: Filter: Salary Range Query
  
  - Create a python mongoDB query to acquire documents based on Salary min/max
  - [x] [8 points] Story 6: Search 

  - Create a python mongoDB query to acquire documents based on any stirng found within
  - [x] [5 points] Story 2: Python Connection to DB
  
  - create a DB client side script that can connect successfully to the mongodb collecitons
  - [x] [5 points]User Collection MongoDB

  - store user information in an online collection on the cluster
  
  ```
  Estimated Story Points: 6 Stories for 55 Points
  
  Completed : 7 Stories for 60 points 
  ```
## What was NOT Completed:
  - [ ] Story 7: User Class
  - [ ] Story 8: User Interface
  - [ ] Story 9: Profile Page
  - [ ] Story 10: Quick Apply
  - [ ] Story 11: Employer's Perspective
  - [ ] Story 12: Returning User


# Sprint 2 April 5th - April 12th:
## What was Completed:
  - [x] [8 points] Story 7: User Class

  - Create a user clas that allows the user to sign in and have user info connect to mongoDB 
  - [x] [13 points] Story 8: User Interface 

  - Create basic interface layout for listings, search, and description
  - [x] [5 points] Story 13: Filter: Profession/Field UI Update

  - Filter for profession updates on the user interface
  - [x] [5 points] Story 14: Filter: Salary UI Update

  - Filter for salary updates on the user interface
  - [x] [5 points] Story 15: Filter: Location UI Update

  - Filter for location updates on the user interface
  - [x] [5 points] Story 16: Min and Max Salary Fields

  - Based of customer feeback, split the inputs for min and max as drop boxes

  ```
  Estimated Story Points: 9 Stories for 67 Points

  Completed : 6 Stories for 41 points 
  ```
    
## What was NOT Completed:
  - [ ] Story 9: Profile page
  - [ ] Story 10: Quick apply
  - [ ] User 12: Returning User
  - [ ] Story 11: Employer's Perspective
 
# Sprint 3 April 12th - April 19th:
## What was Completed:
  - [x] Cusotmer Story: First and Last Name infor on Signup
  - [x] Story 9: Profile Page
  - [x] PDF Upload/Download
  - [x] Story 12: Returning User
  - [x] Story 18: Extended Job Description
  - [x] Customer Story: Change Listing Font
  - [x] Story 17: Location Suggestions


## What was NOT Completed:
  - [ ] Change Drop Box Info
  - [ ] Location filter by zip code and state abbrev
  - [ ] PDF UI Display
  - [ ] Pagination for job listings
  - [ ] Set number og enteries per page
  - [ ] Quick apply
  - [ ] Employers Perspective
 
   ```
  Estimated Story Points: 7 Stories for 38 Points

  Completed : 7 Stories for 30 points 
  ```
  
# Sprint 4 April 19th - April 26th:
## What was Completed:
  - [x] Customer Story: Pagination for job listings
  - [x] Customer Story: Set number of entries per page
  - [x] Customer Story: Remove "in location" from Jobs
  - [x] Story 24: Location filter by zip code, and state abbreviation
  - [x] Customer Story: Extended Job Description/List#30
  - [x] Story: Case insensitive filters
  - [x] Customer: Change Drop Box Info
  - [x] Story: Quick Apply UI
  - [x] Story: PDF UI Display


## What was NOT Completed:
  All complete this week.
  
   ```
  Estimated Story Points: 9 Stories for 38 Points

  Completed : 9 Stories for 38 points 
  ```
# Sprint 4 April 26th - May 3rd:
 
## Customer interaction with the application
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
