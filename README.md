# This is the repo for Rayquaza
Technical debt assignment found [here](https://github.com/comp129/customer-project-rayquaza/blob/main/docs/techDebt.md)


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


# Software needed to run the application
1. [Python 3.10](https://www.python.org/downloads/release/python-3104/)
2. [Pipenv](https://pypi.org/project/pipenv/)
3. [PySide6](https://pypi.org/project/PySide6/) 
4. [PyMongo](https://pypi.org/project/pymongo/)
5. [Certifi](https://pypi.org/project/certifi/)
All of these packages can be installed by running ``pipenv shell && pipenv install`` when in the root directory from a CLI.