#=====Importing Libraries===========
from datetime import date 
#====Login Section====
def login():
    #Create users dictionary to store list of usernames and passwords from the file.
    users = {}
     # Read user.txt file to validate if user is exists.
    with open('user.txt', 'r') as file:
        for line in file:
            username, password = line.strip().split(", ", 1)
            users[username] = password   

    while True:
        # Request user credentials.
        get_username = input("Enter your username: ").strip()
        get_password = input("Enter your password: ").strip()
        if get_username in users:
            if users[get_username] == get_password:
                print("Logged In Successfully")
                return get_username # User has logged in successfully
            else:
                print("Incorrect password, try again.")
        else:
            print("Username not found.")    
        break # Exit loop
# Function to register a new user.
def new_user(get_username):
    if get_username !="admin":
        print("You are not authorized to register a new user.")
        return
    # Load users dictionary to check for duplicate usernames
    users = {}
    with open('user.txt', 'r') as file:
        for line in file:
            username, password = line.strip().split(", ")
            users[username] = password

    new_username = input("Create a new username: ")
    # Check if username already exists
    if new_username in users:
        print("Error: That username has been taken, please choose another username.")

    new_password = input("Create new password: ")
    confirm_pwd = input("Confirm new password: ")
    # Check if the new password matches the confirmed password.
    if new_password != confirm_pwd:
        print("Error: Passwords do not match. Please try again.")  
    else:
        with open('user.txt', 'a') as file:
            file.write(f"{new_username}, {new_password}\n")
            print("Account successfully created!")

# Function to create a task
def new_task(): 
    users = {} 
    with open('user.txt', 'r') as file:
            for line in file:
                username, _ = line.strip().split(", ", 1)
                users[username] = None  # We only need the username for validation

    task_owner = input("Enter username of task asignee: ").strip()
    # Validation to check if task_owner exists in users list.
    if task_owner not in users:
        print("Error: Task assignee username does not exist. Please enter a valid username.")
        return
    
    task_title = input("Title of the task: ").strip()
    task_descrip = input("Describe the task: ").strip()
    task_due = input("Enter the task's due date(DD-MM-YYYY): ").strip()
    today = date.today().strftime('%Y-%m-%d') # Used to format the date.today() object into a consistent string format.
    task_status = 'No'

    # Format: title, assignee, date_assigned, due_date, status, desscription
    task_entry = (f"{task_owner},"
                  f"{task_title},"
                  f"{task_descrip},"
                  f"{today}," 
                  f"{task_due},"
                  f"{task_status}\n")
    with open('tasks.txt', 'a') as file:
            file.write(task_entry)                           
            print("Task successfully created!")
            
# Function to view all tasks   
def viewall_tasks():
    # Read tasks.txt file using open with method.
    with open('tasks.txt', 'r') as file:
        for line in file:
            line = line.strip()
            # Split by comma and space, limit to 5 splits to get 6 parts
            parts = line.split(', ', 5)
            task_owner, task_title, task_descrip, date_assigned, task_due, task_status = parts
            # Print the task details as shown in the Output 2 in the PDF
            if len(parts) == 6:  
                print("\n------------------------")             
                print(f"Task Title:\t{task_title}")
                print(f"Assigned To:\t{task_owner}")
                print(f"Due Date:\t{task_due}")
                print(f"Date Assigned:\t{date_assigned}")
                print(f"Status:\t{task_status}")
                print(f"Description:\n{task_descrip}\n")
                print("\n------------------------")
            else:
                print("Error: Task format is incorrect. Please check the task file.")                       
# Function to view tasks assigned to the logged-in user
def view_my_tasks(get_username):
    # Read tasks.txt file using open with method.
    with open('tasks.txt', 'r') as file:
        for line in file:
            line = line.strip()
            parts = line.split(', ', 5)
            task_owner, task_title, task_descrip, date_assigned, task_due, task_status = parts
            if task_owner == get_username:
                # Print the task details as shown in the Output 2 in the PDF
                if len(parts) == 6:
                     print("\n------------------------")
                     print(f"Task Title:\t{task_title}")
                     print(f"Assigned To:\t{task_owner}")
                     print(f"Due Date:\t{task_due}")
                     print(f"Date Assigned:\t{date_assigned}")
                     print(f"Status:\t{task_status}")
                     print(f"Description:\n{task_descrip}\n")
                     print("\n------------------------")
            else:
                print("Error: You can't view others' tasks.")      
# Statistics display function.
def display_statistics():
    """Calculates and displays the total number of tasks and registered users."""
    total_tasks = 0
    with open('tasks.txt', 'r') as file:
            for line in file:
                if line.strip(): # Ensures that empty lines are not counted as tasks
                    total_tasks += 1
    total_users = 0
    with open('user.txt', 'r') as file:
            for line in file:   
                if line.strip(): # Ensures that empty lines are not counted as users
                    total_users += 1
    print("\n--- Statistics ---")
    print(f"Total Tasks:\t{total_tasks}")
    print(f"Total Users:\t{total_users}") 

# Call the login function to authenticate the user.
logged_in_user = login()
if  logged_in_user:
    #====Menu Section====
    while True:
         # Make sure that the user input is converted to lower case.
        menu = '''Select one of the following options:'''
        # Add 'r-register a user' only if logged_in_user is 'admin'.
        if logged_in_user == "admin":
            menu += '''
                    r - register a user 
                    s - display statistics '''
    
        menu += '''
                    a - add task
                    va - view all tasks
                    vm - view my tasks
                    e - exit
                    : '''
        
        menu_choice = input(menu).lower()

        # If user chooses r.
        if menu_choice == 'r':
                new_user(logged_in_user)
        # If user chooses a.    
        elif menu_choice == 'a':    
            new_task()
        # If user chooses va.   
        elif menu_choice == 'va':
            viewall_tasks()
        # If user chooses vm.
        elif menu_choice == 'vm':
            view_my_tasks(logged_in_user)
        # If user chooses s.
        elif menu_choice == 's':
            if logged_in_user == "admin":
                display_statistics()
            else:
                print("You are not authorized to view statistics.")
         # If user chooses e.
        elif menu_choice == 'e':
             print('Goodbye!!!')
             exit()
        else:
            print("You have entered an invalid input. Please try again")
