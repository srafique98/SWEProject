# Customer Projec Rayquaza: JobSeeker (Report)  
## Team Members
David Leavenworth   - 

Sean Higley         -

Shan Rafique        -

Jesus Torres        - User Interface

## Project Objectives
######  Value delivered to your client:
During the five week period given to us by the customer, Ben, we were able to deliver a product up to the standards of the customer. After the end of each sprint, weekly interval, we received feedback from the customer, which we took and transformed the product in the direction of the customer. Overall, we received positive feedback and approval from the customer.

## Project Design
###### Team goals:
Our team goal is to deliver a high quality product that meets the needs and values of our customers. We planned to hit all the user cases provided to us by the customer. The user cases provided by the customer consisted of applying filters for a job search; uploading a pdf that is saved to the user profiles, and being able to apply to a job relatively quickly (quick apply). Along with those large criteria, we wanted the user interface to be user friendly and usable. Lastly, to create a welcoming and friendly environment for the team.

###### User stories completed:
During the five week period we completed a total of 35 stories for 197 points. We estimated a total of 38 stories for 231. The reason for the discrepancies has to do with overplanning stories, as well as pushing potential stories we planned to get to but ended up freezing. We have a file dedicated to the specifics of our sprints. If you wish to see more click [here](https://github.com/comp129/customer-project-rayquaza/blob/main/docs/Sprints.md). 

## Implementation Details
###### Programming Languages Used:
JobSeekers was programmed 100% in Python. Although the program was utilized in Python, we did use the MongoDB Query Language (MQL) to query data from the jobs and user database.

###### Libraries or Tools Used:
Along with the many tools used for the application, we used MongoDB to store all the data associated with the job listings and profiles created in JobSeekers. Our database is accessible 24/7 with the connection to a network. Since we are working with a database, we use the MongoDB compass to query, optimize, and analyze our data. The use of this tool is purely for developers.

###### Challenges and Solutions:
Throughout the process, we faced many challenges. 
- 

## Testing
###### Testing Plan and Strategies (revised/updated)
###### Test Cases
## Project Highlights (Retrospective)
###### Parts of the actual software you are proud of
- When the user uploads a PDF resume, the resume file is converted to a png file that displays inside of the profile page. The profile page also displays the status of whether a resume has been uploaded.
- For the filters, depending on the character ers being input to the search bar, the bar will suggest recommended locations and positions.
- When a user logs in to their account, their information will display on the screen. So, their resume, summary and cover letter will be saved on displayed on their profile page. They can also be modified.
- The listing of the jobs allows the user to set an amount to be populated and can be edited to have a longer list to browse. Along with this long list, you can flip through the list and see the rest of the jobs that did not appear initially (pagination).

###### Things you guys did as a team that you think worked really well
- Communication was a value the team upheld. Through out the process, the team was consistently updated. If a team member confronted an issue, we made sure to help to the best of our ability.
- Outside of core hours, we made sure to put some time aside to build friendships. We saw great improvement in communication from this.
- Although schedules did not allow for a lot of pair programming, when the opportunity arose we did pair programming to help with any confusion with new topics.

###### Troubles that you ended up solving or finding.
- A problem we ended up solving was the issue with the PDF display. Since the data being transferred to and from the database was in binary, it would not display as an image on screen. Eventually a function was written that would convert the following binary to an image, which would then be set to on the screen.
- Continuing the issue of PDF, originally we had implemented an input box to have the user enter the file path of their PDF file manually. Having this was not very user friendly, so we then changed the method of input. Using a package, we allow for the use of a file explorer. The users file explorer would open and allow the user to upload the resume.
- An issue we found but did not solve, was the suggested completers in the search box for state abbreviations. So, if the user enters 'Texas' the input would not suggest 'TX' as a complete. We managed to aggregate the two when querying the data but not suggest as a complete.
- When creating the listings, there were issues with populating the list and having the each entity be clickable. Since the listing would be updated after each search, it would be appropriate to remove the unneeded entities. Originally they would stack over one another, leading to a mess of characters and readability issues. However, this issue was fixed and works as intended.


## Things To Be Improved (Also Retrospective)
###### Parts of the software that you would improve
- An imporvement that would importge the product would be scaling. Since all the team members have differt aspect ratio on their machines, the scaling of the software varies per user. Smaller screen would results in less to be seen on screen. 
- Another improvement would be the suggested search for the abbreviation issue mentioned. This will allow for a better experience when searching for a location using abbreviations, which are commonly used.

###### Parts of your teamwork/process that you would improve on in the future
- Although we did pair programming. More pair programming would help improve the team. It will help clear up any confusion.
- 
## Lessons Learned
###### Advice you have for future COMP 129 students:
- Communication is key to having a very successful team. A large portion of our success can be credited to the team heavily communicating with one another. If you need help, or dont know how to do a task, don't be afraid to ask. We are a team for a reason.
