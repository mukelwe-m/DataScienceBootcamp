# DataScienceBootcamp
HyperionDev x Stellenbosch Uni data science bootcamp projects


Through this bootcamp I got do a few builds, which are listed below: 
| Build | Purpose | Learnings | Link 
|------|---------|-----------|-----|
| Task Management System | Assign and organise tasks for an SME | Python syntax, error handling, debugging | ...|
| ML Models | Use different machine learning models|Linear Regression, Logistic Regression, Desision trees, etc.| ...|
| NLP App |...| Unsupervised machine learning (K-Means Clustering) | ...|

# Task Management System 📋

A Python-based command-line task management application with user authentication and role-based access control.

## Features

- **User Authentication**: Secure login system with username/password validation
- **Role-Based Access**: Admin-only features for user registration and statistics
- **Task Management**: Create, view, and track tasks with due dates
- **Personal Dashboard**: Users can view tasks assigned specifically to them
- **Statistics Dashboard**: Admins can view system-wide metrics

## Demo

### Login Screen
```
Enter your username: admin
Enter your password: ****
Logged In Successfully
```


### Main Menu (Admin View)
```
Select one of the following options:
r - register a user 
s - display statistics 
a - add task
va - view all tasks
vm - view my tasks
e - exit
: 
```

### Adding a New Task
```
: a
Enter username of task asignee: john_doe
Title of the task: Complete project documentation
Describe the task: Write comprehensive README and user guide for the application
Enter the task's due date(DD-MM-YYYY): 15-02-2026
Task successfully created!
```

### Viewing All Tasks
```
: va

------------------------
Task Title:     Complete project documentation
Assigned To:    john_doe
Due Date:       15-02-2026
Date Assigned:  2026-01-07
Status:         No
Description:
Write comprehensive README and user guide for the application

------------------------
```

### Statistics (Admin Only)
```
: s

--- Statistics ---
Total Tasks:    12
Total Users:    5
```

## Installation

1. Clone the repository:
```bash
https://github.com/hyperiondev-bootcamps/MM25010017606/blob/main/Level%201%20-%20Python%20for%20Data%20Science/L1T15%20-%20Capstone%20Project%20-%20Files/task_manager.py
```

2. Ensure you have the required text files:
   - `user.txt` - Contains usernames and passwords (format: `username, password`)
   - `tasks.txt` - Stores all tasks (auto-created on first task addition)

3. Run the application:
```bash
python task_manager.py
```

## File Structure

```
task-management-system/
│
├── task_manager.py      # Main application file
├── user.txt            # User credentials storage
├── tasks.txt           # Task data storage
└── README.md           # This file
```

## Sample Data Files

**user.txt** (example):
```
admin, admin123
john_doe, password1
jane_smith, password2
```

**tasks.txt** (format):
```
username, task_title, task_description, date_assigned, due_date, status
```

## Usage

### For Regular Users:
- **a**: Add new tasks
- **va**: View all tasks in the system
- **vm**: View only your assigned tasks
- **e**: Exit the application

### For Admin Users:
All regular user options plus:
- **r**: Register new users
- **s**: Display system statistics

## Requirements

- Python 3.x
- No external libraries required (uses standard library only)

## Future Enhancements

- [ ] Task editing and deletion
- [ ] Task completion marking
- [ ] Priority levels for tasks
- [ ] Search and filter functionality
- [ ] Export reports to CSV
- [ ] Password encryption
- [ ] GUI interface

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Author

Mukelwe Mdluli - [GitHub Profile](https://github.com/mukelwe-m)

---

**Note**: This is a learning project. For production use, implement proper password hashing and database storage.