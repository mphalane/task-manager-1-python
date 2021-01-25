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


welcome_msg=' Welcome to Task Manager '
print(welcome_msg.center(50,'='))
print('\n')
#Init boolean flags
#1) Proceed is used when we validate user input
#2) Choice_correct is used when we validate user choice
proceed=False
choice_correct=False

#Ask user to enter login details
while proceed==False:
    
    username=input('Please Enter Your User Name: ')
    password=input('Please Enter The Password: ' )
    #For each user check if login details matches with
    #the login details of in user_dict value (lists)
    for x in user_dict.values():
    
        c_user=x[0]
        c_password=x[1].rstrip("\n") #takes out and trail \n
        
        #If a match is found set the proceed flag to true to break
        #out of the while loop
        if (username==c_user and password==c_password):
            proceed=True 
            print('Password Correct :)\n')
            break 
    #If no match found ,don't update the proceed flag
    #Display error message
    if proceed==False:
        print('Password inCorrect, Please try again\n')
    
#Check if the proceed flag is true
#if so , display appropriate menu
#and ask the user to make a choice
if proceed==True:

    #Check if the user is admin
    #if so display special menu
    #else display default user menu
    print('Please elect one of the following options:')
    if username.lower()=='admin':
        print('r - register user \na - add task \nvs - view statistics \nva - view all tasks \nvm - view my tasks \ne - exit')
    else:
     print('a - add task \nva - view all tasks \nvm - view my tasks \ne - exit')


    #Check if the user selected the correct choice
    #if so the choice_correct flag becomes true and
    #the next menu gets displayed
    #else Ask the user to try again
    while choice_correct==False:
         user_choice=input('Please Enter Your Choice Here: ')
         if user_choice.lower()=='r' and username.lower()=='admin':
             choice_correct=True
         elif user_choice.lower()=='a':
             choice_correct=True
         elif user_choice.lower()=='va':
             choice_correct=True
         elif user_choice.lower()=='vm':
             choice_correct=True
         elif user_choice.lower()=='vs' and username.lower()=='admin':
             choice_correct=True    
         elif user_choice.lower()=='e':
             choice_correct=True
         else:
             print('Choice entered incorrect, Please try again\n')
             choice_correct=False

    #Nested if that computes specified tasks based on user choice

    #1)Allows authenticated user to add a new user
    if user_choice.lower()=='r':

             #Get new user name
             new_user=input("Please enter new user name here: ")

             #Declare and init a confirm flag that enables us to
             #ask the user to re-enter the password again if the passwords
             #dont match, if the passwords match
             #the confirm flag updates to true
             confirm=False
             while confirm==False:
                 new_pword=input("Please enter new password here: ")
                 confirm_pword=input("Please confirm password here: ")
                 if new_pword==confirm_pword:
                     confirm=True
                 else:
                     confirm=False
                     print("Unfortunately your passwords don't match , Please try agin")

             #If confirm is true
             #Add the new user to a user.txt
             if confirm==True:
                #Init temp list
                #add the new_user and new_pword as
                #new items, there after store temp list in user_dict
                 u_templist=['']*2
                 u_templist[0]=new_user
                 u_templist[1]=new_pword
                 user_dict[user_index]=u_templist
                 user_index+=1
                 
                 #Wrie each user_dict value in the "x,y" format
                 with open('user.txt','w') as f:
                     for x in user_dict.values():   
                        f.write(f"{x[0]},{x[1]}")
                 f.close() 
                 print('New user succesfully added :)')
    #2)Allows all users to add a new task and store it in tasks.txt
    elif user_choice.lower()=='a':
             a_done=False
             while a_done==False:
                 t_user=input("Enter the username here: ")
                 t_title=input("Enter the task title here: ")
                 t_desc=input("Enter the task description here: ")
                 t_date=date.today()
                 t_datedone='TBA'
                 t_complete="No"
                 with open('tasks.txt','a+') as f:
                     f.write(f'\n{t_user},{t_title},{t_desc},{t_date},{t_datedone},{t_complete}')
                 f.close()
                 print('New tasks succesfully added :)')
                 a_valid=False

                 while a_valid==False:
                     a_again=input('\nDo you want to add another task (Y/N): ')
                     if a_again.lower()=='y':
                         a_done=False
                         a_valid=True
                     elif a_again.lower()=='n':
                         a_done=True
                         a_valid=True
                     else:
                        print('Choice entered incorrect, Please try again') 
                        a_valid=False
    #3)Allows all users to view all tasks                    
    elif user_choice.lower()=='va':
            #Get list of tasks
            #1) Init empty tasks list
            #2) Open tasks.txt and append each task in tasks_list[]
            #3) Init task_dict dictionary to store multiple split lists
             task_list=[]
             tasks_file=open('tasks.txt','r+')
             tasks_list=tasks_file.readlines()
             tasks_file.close()
             tasks_index=0
             for x in tasks_list:
                x=x.strip('\n')
                temp_list=[]
                temp_list=x.split(',')
                tasks_dict[tasks_index]=temp_list
                tasks_index+=1

            #Display task_dict values in a formated
            #user friendly way 
             caption_msg=' Tasks Done By All users '
             print(caption_msg.center(50,'='))   
             for j in tasks_dict.values():
                 temp_string=""
                 print(temp_string.center(50,'_'))
                 print(f'Task:            \t {j[1]}')
                 print(f'Assigned to:     \t {j[0]}')
                 print(f'Date assigned:   \t {j[3]}')
                 print(f'Due date:        \t {j[4]}')
                 print(f'Task complete ?: \t {j[5]}')
                 print(f'Task description:\n {j[2]}')
                 
    #2)Allows current user to their current tasks
    elif user_choice.lower()=='vm':
            #Get list of tasks
            #1) Init empty tasks list
            #2) Open tasks.txt and append each task in tasks_list[]
            #3) Init task_dict dictionary to store multiple split lists
             task_list=[]
             tasks_file=open('tasks.txt','r+')
             tasks_list=tasks_file.readlines()
             tasks_file.close()
             tasks_index=0
             for x in tasks_list:
                x=x.strip('\n')
                temp_list=[]
                temp_list=x.split(',')
                tasks_dict[tasks_index]=temp_list
                tasks_index+=1
            #Display task_dict values in a formated
            #user friendly way 
             caption_msg=f' Tasks Done By {username.lower()} '
             print(caption_msg.center(50,'='))   
             for j in tasks_dict.values():
                 #Only display tasks that match with username
                 if username.lower()==j[0].lower():
                     temp_string=""
                     print(temp_string.center(50,'_'))
                     print(f'Task:            \t {j[1]}')
                     print(f'Assigned to:     \t {j[0]}')
                     print(f'Date assigned:   \t {j[3]}')
                     print(f'Due date:        \t {j[4]}')
                     print(f'Task complete ?: \t {j[5]}')
                     print(f'Task description:\n {j[2]}')
    elif user_choice.lower()=='vs':
            #Open task list to count the number of tasks
            #store number of tasks value in tasks_len
            #Display total number of users(user_index) and tasks 
             task_list=[]
             tasks_file=open('tasks.txt','r+')
             tasks_list=tasks_file.readlines()
             tasks_file.close()
             tasks_len=len(tasks_list)
             caption_msg=f' Task Manager Statistics '
             print(caption_msg.center(50,'='))   
             temp_string=""
             print(temp_string.center(50,'_'))
             print(f'Total number of all tasks:            \t {tasks_len}')
             print(f'Total number of users:                \t {user_index}')
    elif user_choice.lower()=='e':
             quit() #exit the program
         
