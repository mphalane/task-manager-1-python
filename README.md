# Task Manager
This is a basic python terminal program for a small business that can help it to manage tasks assigned to each member of the team.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development:
1) First follow the instruction [here](https://www.codecademy.com/articles/install-python) to install python 
2) Second click on "[Downlaod Zip](https://www.instructables.com/Downloading-Code-From-GitHub/)" to get a full copy of this project including the resources used.
## Code Style and Example
The code style used is standard 

The example of the code is shown below:

```python
from datetime import date


#Get list of users
#1) Init empty user list
#2) Open user.txt and append username and password in user_list[]
#3) Init user dictionary to store multiple split lists
user_list=[]

usernames_file=open('user.txt','r+')
user_list=usernames_file.readlines()
usernames_file.close()

user_dict={}
tasks_dict={}
user_index=0

#For each "username,password" item  split it
#into two items and store them in a temp list
#store this temp list into a user_dict
for x in user_list:
    temp_list=[]
    temp_list=x.split(',')
    user_dict[user_index]=temp_list
    user_index+=1
#print(user_dict)
```

## How To Use ?
1) Double click on the task_manager.py and follow the prompts displayed in the terminal 
2) The data for each task is stored on a separate line in the text file - task.txt. Each line includes the following data about a task in this order:

    1) The username of the person to whom the task is assigned.
    2) The title of the task.
    3) A description of the task.
    4) The date that the task was assigned to the user.
    4) The due date for the task.
    6) Either a ‘Yes’ or ‘No’ value that specifies if the task has been completed yet.
    
    
3) The text file user.txt stores the username and password for each user that has permission to use your program will be the current date. Also the assumption that whenever you add a new task, the value that indicates whether the task has been completed or not is ‘No’.
