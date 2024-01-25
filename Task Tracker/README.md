Task Tracker and Windows Service
Task Tracker (Task_edit.py)

Overview

The Task_edit.py script serves as a Task Tracker application allowing users to manage their tasks through a command-line interface. It utilizes the pandas library for handling CSV data, ensuring task uniqueness, and providing functionality such as adding, viewing, marking as complete, and deleting tasks.

Task Class
The Task class represents a task, incorporating methods for writing tasks into a CSV file, adding serial numbers, adding new tasks, viewing tasks, marking tasks as complete, deleting tasks, and exiting the application. The class ensures that tasks with the same name are not duplicated.

Main Function
The main function acts as the entry point for the application, providing a user-friendly menu for interacting with the task tracker. Users can choose options to add tasks, view tasks, mark tasks as complete, delete tasks, or exit the application.

Usage
Run the script (Task_edit.py).
Choose options from the menu:
Add Task (1): Add a new task.
View Tasks (2): Display all tasks.
Mark Task as Complete (3): Update the status of a task to "Complete."
Delete Task (4): Remove a task from the list.
Exit (5): Terminate the application.
Configuration
The script creates a CSV file named "Task_info.csv" to store task information.
Users can customize the CSV file name by modifying the name variable in the main function.
Dependencies
pandas: Used for CSV file operations.
datetime: Used for validating due dates.
Considerations
The script ensures unique tasks by checking for existing tasks with the same name.
User input is validated to handle invalid choices and date formats.
MyService Windows Service
Overview
The MyService Windows service is implemented using the win32serviceutil module, allowing it to run in the background. The service periodically checks a CSV file for tasks with the current date and "Incomplete" status, sending email notifications for matching tasks. It is designed to run indefinitely.

Dependencies
pandas: Used for reading and manipulating the CSV file.
time.sleep: Provides a pause to control the frequency of task checks.
datetime.date: Retrieves the current date for comparison.
smtplib: Enables sending emails using the Simple Mail Transfer Protocol (SMTP).
email.mime.text and email.mime.multipart: Used to construct and format email messages.
win32service, win32serviceutil, win32event: Windows-specific modules for creating and managing Windows services.
servicemanager: Provides access to the Windows service manager for logging and event handling.
socket: Sets the default timeout for network-related operations.
Service Implementation
The MyService class inherits from win32serviceutil.ServiceFramework and defines methods for service start, stop, and the main functionality. The service reads a CSV file containing task information, filters tasks with the current date and "Incomplete" status, and sends an email notification if any matching tasks are found.

Email Functionality
The service utilizes the smtplib library to send email notifications through a Gmail SMTP server. Ensure that the sender's email and password are correctly provided for authentication. The email contains a message listing tasks with a due date on the current day.

Configuration
Update the file_path, sender_email, sender_password, and recever_email variables in the MyService class with appropriate values for file path and email configuration.

Running the Service
To run the service, execute the script in command prompt as administrator locate the file then install using “python Task_Tracker.py install” and start the service using “python Task_Tracker.py start”. You can start with “python Task_Tracker.py stop” and remove the service using “python Task_Tracker.py remove”
