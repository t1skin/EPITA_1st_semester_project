Project name: EPITA first semester project.


Description:
Web application built with flask framework. The purpose is to represent
particular data fetched from database.


Modules:

main.py: imports "flask" and "DB.py" module. "Main.py" containes 
         definitions of all functions that are used to generate web pages 
         and runs the application.

DB.py:  imports "jaydebeapi" and "Quaries.py" modules. "DB.py"
        contains definitions of all functions that fetch data from database.

jaydebeapi: used to connect to H2 database.

Quaries.py: containes SQL quaries. Some quaries are static, others
            depend on different variables.

index.html: template for main (home) page.

population.html: template for page that represents population and courses
                 of a particular program. 

student.html: template for page that represents information about a 
              particular student.

grades.html: template for page that represents all students of a course
             and their grades in this course.

main.css: main styles for all html templates.

styles_index.css: additional styles for "index.html".

bar_chart.js: script for generating a bar chart.

pie_chart.js: script for generating a pie chart.

clock.js: script for generating clock.


Author: Ilia Tiskin
Email: tiskin2308@gmail.com