# Customer Projec Rayquaza: JobSeeker (Report)  
## Team Members
David Leavenworth   - User Interface 

Sean Higley         -

Shan Rafique        - User Interface

Jesus Torres        - User Interface

## Project Objectives
######  Value delivered to your client:
Our customer, Ben, sought an application that assists in finding jobs and facilitating application to those jobs. During the five-week period given to us by our customer we were able to deliver a product up to the standards of the customer. After the end of each sprint, we received feedback from the customer, which we took and transformed the product in the direction of the customer. Overall, we satisfied our customer and implemented every major feature he wanted, along with some ancillary features he suggested during our feedback sessions.

## Project Design
###### Team goals:
Our team goal is to deliver a high quality product that meets the needs and values of our customers. We planned to implement all the use cases provided to us by the customer. The use cases provided by the customer consisted of applying filters for a job search; uploading a PDF that is saved to the user profiles, and being able to apply to a job relatively quickly (quick apply). Along with those large criteria, we wanted the user interface to be user-friendly and usable. Lastly, to create a welcoming and friendly environment for the team.

###### User stories completed:
During the five-week period we completed a total of 35 stories for 197 points. We estimated a total of 38 stories for 231. The reason for the discrepancies has to do with over-planning stories, as well as pushing potential stories we planned to get to but ended up ice-boxing. We have a file dedicated to the specifics of our sprints. If you wish to see more click [here](https://github.com/comp129/customer-project-rayquaza/blob/main/docs/Sprints.md). 

## Implementation Details
###### Programming Languages Used:
JobSeekers was programmed 100% in Python. Although the program was utilized in Python, we also used the MongoDB Query Language (MQL) to query data from the jobs and user database.

###### Libraries or Tools Used:
On the backend, we used MongoDB to store all the data associated with the job listings and profiles created in JobSeekers. Our database is accessible 24/7 with the connection to a network due to our use of MongoDB Atlas, a database hosting service provided by the developers of MongoDB. Since we are working with a database, we use the MongoDB compass to query, optimize, and analyze our data. The use of this tool is purely for developers. When the application itself is retrieving data we made use of pymongo, a library which provides a python API for accessing Mongo databases.

On the frontend we used PySide6, a library which provides Python bindings for the Qt library. When designing our user interface we made use of QtCreator/QtDesigner. This is a what you see is what you get (WYSIWYG) GUI editor which created .UI files. We then load these .UI files with PySide6 and add the necessary logic to the UI elements. This helped our productivity greatly as we never had to worry about "writing" the UI. Because of this WYSIWYG GUI editor we could focus most of our efforts on the logic behind the UI and the more complex UI features not possible from the editor.

Other miscellaneous libraries we used include:
- PyTest for unit testing.
- Certifi for SSL and TSL authentication when connecting to the database.
- PyPdfium2 to convert uploaded resumes to an image for display.
- Aspose-words for conversion from a .docx to PDF.
- PyQtDarkTheme for an easy dark mode setting.

###### Challenges and Solutions:
The Qt library which PySide6 provides Python bindings for is written in C++. This creates an interesting situation where creating an object results in two objects being created, the Python object we created, and the UI element created by the Qt library. It is important to ensure that changes made to the Python object reflect in the C++ object and vice versa. For instance, it is entirely possible to keep a reference to a Python object but have lost all references to the underlying C++ object. When calling Qt methods for the still existing Python object this results in an exception. The solution is to ensure all references to the Python object are removed when the UI element the C++ object represents is removed. Essentially, more careful management of Python objects is necessary when programming with PySide6 than is normally required when using Python.

## Testing
###### Testing Plan and Strategies (revised/updated)
###### Test Cases
## Project Highlights (Retrospective)
###### Parts of the actual software you are proud of
- When the user uploads a PDF resume, the resume file is converted to a png file that displays inside the profile page. The profile page also displays the status of whether a resume has been uploaded.
- For the filters, depending on the character ers being input to the search bar, the bar will suggest recommended locations and positions.
- When a user logs in to their account, their information will display on the screen. So, their resume, summary and cover letter will be saved on displayed on their profile page. They can also be modified.
- The listing of the jobs allows the user to set an amount to be populated and can be edited to have a longer list to browse. Along with this long list, you can flip through the list and see the rest of the jobs that did not appear initially (pagination).

###### Things you guys did as a team that you think worked really well
- Communication was a value the team upheld. Throughout the process, the team was consistently updated. If a team member confronted an issue, we made sure to help to the best of our ability.
- Outside of core hours, we made sure to put some time aside to build friendships. We saw great improvement in communication from this.
- Although schedules did not allow for a lot of pair programming, when the opportunity arose we did pair programming to help with any confusion with new topics.

###### Troubles that you ended up solving or finding.
- A problem we ended up solving was the issue with the PDF display. Since the data being transferred to and from the database was in binary, it would not display as an image on screen. Eventually a function was written that would convert the following binary to an image, which would then be set to on the screen.
- Continuing the issue of PDF, originally we had implemented an input box to have the user enter the file path of their PDF file manually. Having this was not very user-friendly, so we then changed the method of input. Using a package, we allow for the use of a file explorer. The users file explorer would open and allow the user to upload the resume.
- An issue we found but did not solve, was the suggested auto-complete in the search box for state abbreviations. So, if the user enters 'Texas' the input would not suggest 'TX' as an input. We managed to aggregate the two when querying the data but not suggest as a complete.
- When creating the listings, there were issues with populating the list and having each entity be clickable. Since the listing would be updated after each search, it would be appropriate to remove the unneeded entities. Originally they would stack over one another, leading to a mess of characters and readability issues. However, this issue was fixed and works as intended.


## Things To Be Improved (Also Retrospective)
###### Parts of the software that you would improve
- An improvement that would improve the product would be scaling. Since all the team members have different aspect ratio on their machines, the scaling of the software varies per user. Smaller screen size results in less to be seen on screen. 
- Another improvement would be the suggested search for the abbreviation issue mentioned. This will allow for a better experience when searching for a location using abbreviations, which are commonly used.
- Custom styling through the use of QML style sheets would improve the look and feel of our application. Our primary concern during the five weeks we had was implementing the major features our customer wanted - which was not custom styling - and as such our application has little to no custom styling. 
- We were never able to successfully package our application for distribution, this likely has something to do with our directory structure. Unfortunately the import style we used depends on the current directory structure and would require significant reworking to package for distribution. If work was continued this would likely be the most pressing issue to fix.

###### Parts of your teamwork/process that you would improve on in the future
- Although we did pair programming. More pair programming would help improve the team. It will help clear up any confusion.
- Create more detailed user stories. 
- Break up the work so each team member could get a taste of the different side of the project.

## Lessons Learned
###### Advice you have for future COMP 129 students:
- Communication is key to having a very successful team. A large portion of our success can be credited to the team heavily communicating with one another. If you need help, or don't know how to do a task, don't be afraid to ask. We are a team for a reason.
- Researching the tool that you are using will take the majority of your time. Learning a new tool is not an easy task but at the end it is defintely rewarding.

