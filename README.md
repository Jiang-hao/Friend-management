# Friend-management

I used Django + Sqlite3(PostgreSql) for back-end. Javacript + Jquery + Ajax are used for front-end. Since I saw from the project description, the requirements are mainly about back-end, I did not use any framework for front-end. 

And I published my project onto pythonanywhere. You can have a test at [Here](http://jianghao.pythonanywhere.com/index/) - http://jianghao.pythonanywhere.com/index/

Each step in the project challenges me but I enjoyed it. I will introduce the project from below perspectives:
1. Basic flow
2. Techniques used
3. Things to note
4. Things to be improved

## Basic flow:
The system supports functions( same as project description): 
connect: add two persons
retrieve: retrieve friends
find common: find common friends for two persons
follow: follow others
block: block others
post a message

The left panel in the webpage is an operation panel. Users can choose operations to be performed and then enter information.
The right panel is to show the logs including both data sent to server and data received from server.

Front-end makes ajax calls to back-end. Back-end performs logics with data sent. Deals with database and then sends data back to front-end.
#### Examples:
```
Connect: a@a and c@c
Connect: a@a and b@b
Follow: d@d follows a@a
Follow: e@e follows a@a
Message: a@a 'Hello g@g and h@h' -> receivers should be b@b, c@c, d@d, e@e, g@g, h@h

Block: c@c blocks a@a
Block: e@e blocks a@a
Block: g@g blocks a@a
Message: a@a 'Hello g@g and h@h' -> receivers should be b@b, d@d, h@h(others blocked a@a)
```
## Techniques used:

##### Back-end 
Python(Django framework) + Sqlite3
djangorestframework: Changed to ajax
django-cors-header, django-cors-middleware, csrf_exempt -> to handle cross-site calls
Exceptions-> to handle exceptions might occur
Regular expressions-> to handle mention function in text
pythonanywhere-> to deploy the project

##### Front-end
HTML + CSS + Javascript + Jquery + Ajax



## Things to note: 
1. For message mention function, I assume all persons use email as their id. And as long as an email is in the text, it is considered as memtions.
2. Database max-length is 200 characters. 
3. If database goes wrong, please let me know jiangh0313@gmail.com / +6586694597
4. Default data in database is
  a@a and b@b. They are friends with each other
  *In this project, I just tested db since all others I tested on the webpage itself. For more testing, you may find here: https://github.com/cl-nus/JavaTerminal/tree/master/test . It is a school project which is a software testing module. We wrote tests cases for a self-made PC cmd software

## Things to be improved:
Since this is an interview, I wanted to showcase the project as soon as possible. There may be some points to be improved
1. Security: Since time limitation, I did not add enough security features. In the future, will make the web site more secure
2. Extendable: Because of time limitation and this time I focused more on the tasks in the descriptions, the system may not be efficient to support other features that may need in the future such as deleting, groups etc. But in the future, I could think more and change the structures of the webpage to make the project more extendable.

## Conclusion
Thanks for the opportunity. I enjoyed the learning process and hope this API server works fine.
If you need any detailed explanations or you have any doubts, please feel free contact me.
Thank you.






