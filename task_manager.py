import datetime

def reg_users():
       if username_1 == "admin":   
         # Prompting the user to enter a new username and password if they choose 'r'. 
        new_username = input("Enter the new user's username:\n")
       #Checking if the new username is already listed in the user.txt file.
        with open('user.txt', 'r') as user_file:
            usernames_list = user_file.read()
            # If the new username is already listed, prompt the user to enter a new username.
            while new_username in usernames_list:
                print("\nThis user is already listed. Try registering a new user.\n")
                new_username = input("Enter the new user's username:\n")
                   
        # If the new username entered is not listed in the user.txt file,
        # prompt the user to enter a new password for the username.
        if new_username not in usernames_list:
            new_password = input("Enter the new user's password:\n")
            # Prompting the user to confirm the new password.
            new_password_conf = input("Confirm the new user's password:\n") 

            # If new password and confirmed password do not match,
            # prompt the user to re-enter the password.
            while new_password != new_password_conf:
                print("\nThe new password and the confirmed password do not match, please try again.\n")
                new_password = input("Enter the new user's password:\n")
                new_password_conf = input("Confirm the new user's password:\n")
           
        # Saving the new username and password to the user.txt text file.
        if new_password == new_password_conf:              
            with open("user.txt", "a") as user_file:
                user_file.write("\n" + new_username + ", " + new_password)
                # Displaying a message to user when the username and password has been saved.
                print("\nThe new user has been registered.\n")       

def add_task():
       
       # Prompting the user enter the details of the task they are assigning.
       task_username = input("Enter the username of the person whom the task will be assigned to:\n")
       name_of_task = input("Enter the title of the task:\n")
       task_description = input("Please provide a description of the task at hand:\n")
       task_due_date = input("Enter the due date of the task (dd-mmmm-yyyy):\n")
       task_due_date = task_due_date.replace("-", " ")

       task_list = [task_username, name_of_task, task_description, task_due_date]      
       tasks_dict[f"Task {count} details:"] = task_list 

       # Adding the task details to the tasks.txt file.
       with open('tasks.txt', 'a') as task_file:
          task_file.write("\n" + task_username + ", " + name_of_task + ", " + task_description + ", " + str(datetime.date.today()) + ", " + task_due_date + ", " + "No")     
       print("\nNew task has been added to the tasks.txt file.\n") # Displaying confirmation to the user.

# Function view all the tasks in the tasks.txt file.
def view_all(user_menu):
    print("\nAll the tasks in the tasks.txt text file:\n")

    if user_menu == "va":
        task_count = -1
        for key in tasks_dict:
            task_count += 1

            print(f"""__________________________________________________________________________________________________________________

Task {str(task_count)}:                 {str(tasks_dict[key][1])}
Assigned to:            {str(tasks_dict[key][0])}
Date assigned:          {str(tasks_dict[key][3])}
Due Date:               {str(tasks_dict[key][4])}
Task Complete?          {str(tasks_dict[key][5])}
Task Description:
{str(tasks_dict[key][2])}
__________________________________________________________________________________________________________________""")
    return("\nEnd of Tasks.\n")

# Function that allows the user to view all tasks assigned to them.
def view_mine(user_menu, username_1):
       
    if user_menu == "vm":
        task_count = -1  # Setting a count for number of tasks.
        for key in tasks_dict:
            task_count += 1  # calculating the total number of tasks by increasing the count through tasks_dict.
            if username_1 == (tasks_dict[key][0]):  # If the task is assigned to the user, it is displayed.
                print(f"""___________________________________________________________________________________________________________

Task {str(task_count)}:             {str(tasks_dict[key][1])}
Assigned to:        {str(tasks_dict[key][0])}
Date assigned:      {str(tasks_dict[key][3])}
Due Date:           {str(tasks_dict[key][4])}
Task Complete?      {str(tasks_dict[key][5])}
Task Description:
{str(tasks_dict[key][2])}
___________________________________________________________________________________________________________""")       

        # The user can now choose to either edit a task by number or return to the main menu.
        task_selection = input("\nPlease select a task by number to edit (e.g. 1, 2,3) or type -1 to return to the main menu. \n")
        if task_selection == "-1":  # If they select '-1', they return to the outer while loop main menu.
            return(user_menu)        
                
        else:  # If they enter a task number, they can choose to mark as complete or edit.
            option = input("Would you like to mark the task as complete or edit the task? (e.g. mark OR edit) \n")
            if option == "mark":
                task_selection = int(task_selection)

                with open("tasks.txt", "r+") as tasks_file:           
                    data = tasks_file.readlines()
                    data[task_selection] = data[task_selection].replace("No", "Yes")

                    with open("tasks.txt", "w") as file:
                        file.writelines(data)

                 # If they choose to mark, the item linked to that task for completion is changed to 'Yes' in tasks_dict.
                tasks_dict[f"Task {task_selection} details:"][5] = "Yes"

                return("\nYour task has been successfully marked as complete.\n")
                        
            # If they choose to edit, the task must be incomplete, i.e. appropriate item in dictionary list equal to 'No'.
            elif option == "edit" and (tasks_dict[f"Task {task_selection} details:"][5] == "No"):
                #They are given the option to edit username or due date.
                edit_choice = input("Would you like to edit the task username or due date? (Type 'U' or 'D') \n").lower()            
                if edit_choice == "u":  # If they choose to edit the username, they are prompted to enter a new username for the task.
                    name_edit = input("Please enter a new username for the task: \n")
                    tasks_dict[f"Task {task_selection} details:"][0] = name_edit  # The new name is assigned in the dictionary.
                    return("The task username has been updated successfully.")  # Successful return message.
                
                elif edit_choice == "d":  # If they choose to edit the due date, they are prompted to enter a new date. 
                    due_date_change = input("Please enter a new due date (e.g. 12 May 2020) \n")
                    tasks_dict[f"Task {task_selection} details:"][4] = due_date_change  # New date is updated in the tasks_dict.
                    return("The due date has been updated successfully.")  # Sucessful return message.
            
            elif option == "edit" and (tasks_dict[f"Task {task_selection} details:"][5] == "Yes"):
                return("\nYou can only edit tasks that are not already complete. \nChoose 'vm' from menu below to select another task to edit.")

def over_due_check(due_date):

    over_due = False  # Setting Boolean variable for the task as over_due.  

    # Importing datetime and dates to enable the comparison and to retrieve the current date.
    import datetime
    from datetime import date
    
    # The dates in this task are in the format '10 Dec 2015' as a string.
    # So, this needs to be converted to integers to compare dates.
    # First, the variable is split into a list.
    list_dates = due_date.split()
    
    day = int(list_dates[0])  # The first item is cast into an integer and stored in the 'day' variable.
    year = int(list_dates[2])  # The second item is cast into an integer and stored in the 'year' variable.

    # A month dictionary with number values is set to enable calculation of string month into an integer. 
    months_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul':7, 'Aug': 8, 'Sep':  9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

    # The corresponding value of the key in months_dict which is equal to list_dates[1] (i.e. 'Dec', 'Oct' etc.) is stored in 'month'.
    # This will be a number value from the appropriate key in months_dict.
    month = months_dict[list_dates[1][0:3]]

    # Getting the current date using the datetime module and formatting it into the same format at the due date initially was.
    date_now = datetime.date.today().strftime('%d %b %Y')

    # The same process is repeated for the current date.
    # Firstly, it is split into a list of items.
    date_now_list = date_now.split()

    day_2 = int(date_now_list[0])  # The first item is stored as an integer in day_2.
    year_2 = int(date_now_list[2])  # Second item is stored as an integer in year_2.
    month_2 = months_dict[date_now_list[1]]  # The corresponding integer value from months_dict at appropriate key is stored in month_2.

    # Now that we have integers for year, day and month to work with, two dates can be created in the correct format for comparison.
    # date_1 is the due date and date_2 is the current date.
    date_1 = date(year, month, day)
    date_2 = date(year_2, month_2, day_2)

    if date_2 > date_1:  # If current date is greater than set due date, over_due is changed to 'True'.

        over_due = True
        return(over_due)  # over_due value is returned.

    elif date_1 > date_2 or date_1 == date_2:  # If set due date is greater than current date, over_due is 'False'.

        over_due = False
        return(over_due)  # over_due value is returned.

# Function to generate reports.
def generate_reports():

    task_overview = ""  # Setting blank strings to store info in to be written to the generated text files.
    user_overview = ""

    tasks_total = len(tasks_dict)  # Total number of tasks is equal to the key count of tasks_dict.
        
    # Adding a string with the total tasks number to the tas_overview string. 
    task_overview = task_overview + f"The total number of tasks generated and tracked by task_manager.py is {str(len(tasks_dict))}."

    x = 0  # Setting variables for integers concerning complete tasks, incomplete tasks and overdue tasks respectively.
    y = 0
    z = 0
    
        
    for key in tasks_dict:

        if tasks_dict[key][5] == "Yes":  # Checking for which tasks are complete by finding the 'Yes' string in each key of tasks_dict.

            x += 1  # If the task is complete, i.e. 'Yes' string item is present, variable x is increased by 1.     

        elif tasks_dict[key][5] == "No":  # Checking for which tasks are complete by finding the 'No' string in each key of tasks_dict.

           y += 1  # If the task is complete, i.e. 'No' string item is present, variable y is increased by 1. 

           if over_due_check(tasks_dict[key][4]):  # If the over_due_check function returns 'True', a task is overdue and incomplete.

               z += 1  # 'z' is increased by 1 to count the incomplete, overdue tasks.
            

    # All of the numbers calculated above are now built into sentences in the task_overview string.
    # Percentages are also calculated within the f-strings added, with the results being rounded to 2 decimal places and cast into strings into sentences.
    task_overview = task_overview + f"\nThe total number of completed tasks is {str(x)}." + f"\nThe total number of incomplete tasks is {str(y)}."
    task_overview = task_overview + f"\nThe total number of uncompleted and overdue tasks is {str(z)}."
    task_overview = task_overview + f"\nThe percentage of incomplete tasks is {str(round((y / len(tasks_dict)) * 100, 2))}%."
    task_overview = task_overview + f"\nThe percentage of tasks that are overdue {str(round((z / len(tasks_dict)) * 100, 2))}%."

    # Now generating a 'task_overview' file.
    # The task_overview string is then written to the file in an easy to read format.
    with open('task_overview.txt', 'w') as f3:

        f3.write(task_overview)

    # Setting variables to store information regarding total users, complete tasks for a user, incomplete tasks for the user,
    # incomplete and over-due tasks for the user respectively.
    a = 0
    b = 0
    c = 0
    d = 0

    for key in tasks_dict:

        if tasks_dict[key][0] == username_1:  # Counting the number of tasks assigned to the user by identifying the first list item.

            a += 1  # Integer 'a' is increased by 1 if the task is for the user.

        elif tasks_dict[key][0] == username_1 and tasks_dict[key][5] == "Yes":  # Checking if the task for the user is complete.

           b += 1  # Integer 'b' is increased by 1 if the task is complete.     

        elif tasks_dict[key][0] == username_1 and tasks_dict[key][5] == "No":  # Checking if the task for the user is incomplete.

            c += 1  # Integer 'c' is increased by 1 if the task is incomplete.  

            if over_due_check(tasks_dict[key][4]):  # Checking if the task is incomplete and overdue.

                d += 1  # If overdue, integer 'd' is increased by 1.
         
    # Writing all the info calculated above into sentence strings which are built into the user_overview string variable.
    user_overview = user_overview + f"The total number of users registered with task_manager.py is {str(len(user_details))}."
    user_overview = user_overview + f"\nThe total number of tasks generated and tracked by task_manager.py is {str(len(tasks_dict))}."
    user_overview = user_overview + f"\nThe total number of tasks assigned to {username_1} is {str(a)}."
    user_overview = user_overview + f"\nThe percentage of the total number of tasks assigned to {username_1} is {str(round((a / len(tasks_dict)) * 100, 2))}%."
    user_overview = user_overview + f"\nThe percentage of tasks assigned to {username_1} that have been completed is {str(round((b / a) * 100, 2))}%."
    user_overview = user_overview + f"\nThe percentage of tasks still to be completed by {username_1} is {str(round((c / a) * 100, 2))}%."
    user_overview = user_overview + f"\nThe percentage of incomplete and overdue tasks assigned to {username_1} is {str(round((d / a) * 100, 2))}%."

    # Now generating a 'user_overview' file.
    # The user_overview string is then written to the file in an easy to read format.
    with open('user_overview.txt', 'w') as f4:

        f4.write(user_overview)        

    # The user then views a message stating that their reports have been successfully generated.
    # They do not have the option to view the reports.
    # The admin user can select to display statistics from their main menu.
    return("Your reports have been generated successfully.")


user_details = {}

# The user details dictionary will be built with lists from 'usernames_list' and 'passwords_list' as values.
usernames_list = []
passwords_list = []

tasks_dict = {}


with open('user.txt', 'r+') as f:
    for line in f:
        newline = line.rstrip('\n')  # Stripping newline characters from the line.
        split_line = newline.split(", ")  # Splitting the line into a list.
        usernames_list.append(split_line[0])  # Assigning items from the list into corresponding list.
        passwords_list.append(split_line[0])

        user_details["Usernames"] = usernames_list  # Lists are now stored as values assigned to keys in user_details dictionary.
        user_details["Passwords"] = passwords_list      


# Setting a count to keep track of the number of lines in the tasks.txt file.
count = 1

with open('tasks.txt', 'r+') as f2:
    for line in f2:      
        newline = line.rstrip('\n')  # Stripping newline characters.        
        split_line = newline.split(", ")  # Splitting line into a list of items.
        tasks_dict[f"Task {count} details:"] = split_line # Assigning each list of items to a key in tasks_dict.
        count += 1  

# Prompting the user to enter their login details.
print("Please enter your login details:\n\n")

# Checking if the user's username and password is stored in the user.txt file.
with open('user.txt', 'r') as file:
    login_details = file.read()
    username_1 = input("Enter your username: ")
    
    while username_1 not in login_details:
        print("\nThe username you entered is invalid. Please try again.\n") 
        username_1 = input("Enter your username: ")

    password_1 = input("Enter your password: ")
    while password_1 not in login_details:
        print("\nThe password you entered is invalid. Please try again.\n")
        password_1 = input("Enter your password: ")
       
    if username_1 and password_1 in login_details:
        print("\nLogin was successful.\n")

while True:
    if username_1 == "admin":       # The admin user views a specific menu with extra options (gr and ds).
        user_menu = input('''\nPlease select one of the following options:

r  - Register user
a  - Add task
va - View all tasks
vm - View my tasks
gr - Generate reports
vs - View statistics 
e  - Exit

Enter your choice: ''').lower()  
    
    else:
   # Presenting the menu to the user after they have logged in successfully.
        user_menu = input('''Select one of the following Options below:
r  - Registering a user 
a  - Adding a task
va - View all tasks
vm - View my task    
e  - Exit
                      
Enter your choice: ''').lower()  # Converting the user's option to lowercase.
    
    if user_menu == 'r':
        reg_users()
    elif user_menu == 'a':     
        add_task()   
    elif user_menu == 'va':
        print(view_all(user_menu))
    elif user_menu == 'vm':
        print(view_mine(user_menu, username_1))   
    elif user_menu == 'gr':
        print(generate_reports())          
    elif user_menu == "vs":      
        print(generate_reports())  
        print("""\n____________________________________________________

The task overview report is as follows:
____________________________________________________\n""")  

        with open('task_overview.txt', 'r+') as f3:  
            for line in f3:
                print(line)  
        print("""\n_____________________________________________________

The user overview report is as follows:
_____________________________________________________\n""")  

        with open('user_overview.txt', 'r+') as f4:  
            for line in f4:
                print(line)  
        print("""\n______________________________________________________

End of Statistics Reports
______________________________________________________\n""")  

   # Exiting the program if the user chooses 'e'.
    elif user_menu == 'e':
       print("\nProgram has ended.\n")
       exit()   
    # Displaying a message if the user chooses an option that is not listed in the menu.
    else:
       print("\nThe option you chose is not listed in the menu. Please try again.\n")
