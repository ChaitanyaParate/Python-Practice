import csv
import pandas as pd
import datetime
import sys
class Task:
    def __init__(self , info_list , Status="Incomplete"):
        self.info_list = info_list
        self.Status = Status
        self.info_list.append(self.Status)

    def __str__(self):
        return "You already have this task"

    def write_into_csv(self , info_list):
        with open("Task_info.csv" , mode="a" , newline='' ) as csv_file:
            writer = csv.writer(csv_file)
            
            if csv_file.tell() == 0:
                writer.writerow(["Sr.no." , "Task" , "Discruption" , "Due Date" , "Status"])
            
            writer.writerow(self.info_list)
    @classmethod
    def Sr_no(cls , file_name):
        num = []
        df = pd.read_csv(file_name)
        df.drop('Sr.no.', axis=1, inplace=True)
        df.to_csv('Task_info.csv')

        for i in range(len(pd.read_csv(file_name))):
            num.append(i + 1)

        df.insert(0, 'Sr.no.', num)

        df.to_csv('Task_info.csv', index=False)
        df = pd.read_csv(file_name, index_col=0)
        print(df)

    @classmethod
    def add_task(cls , file_name):
        record = []
        try:
            record.append(len(pd.read_csv(file_name)) + 1)
        except pd.errors.EmptyDataError:
            record.append("1")
        record.append(input("What is the task ? "))
        record.append(input("Discruption: "))
        
        while True:
            try:
                date = input("Due Date(YYYY-MM-DD): ")
                datetime.datetime.strptime(date , "%Y-%m-%d")
            except ValueError:
                print("Please enter in valid format!")
                continue
            break
        record.append(date)
        df = pd.read_csv(file_name , index_col=0)

        if not (df[df['Task'] == record[1]]).empty:
            print ("You already have this task")
            
        task = Task(record)
        task.write_into_csv(task)
    @classmethod
    def view_task(cls , file_name):
        try:
            df = pd.read_csv(file_name , index_col=0)
            
            if df.empty:
                raise ValueError
            print (df)
        except (pd.errors.EmptyDataError , ValueError):
            print ("You don't have any task!")
    @classmethod
    def done_task(cls , file_name):
        df = pd.read_csv(file_name , index_col=0)
        print(df)
        
        while True:
            done_task = input("What task have you done?\n").strip()

            filtered_rows = df[df['Task'] == done_task]

            if not filtered_rows.empty:
            
                df.loc[df['Task'] == done_task, "Status"] = "Complete"
                df.to_csv('Task_info.csv')
                print("Task status updated.")
                print(df)
                break
            else:
                print(f"No task found with the name: {done_task}")
    @classmethod
    def del_task(cls , file_name):
        df = pd.read_csv(file_name , index_col=0)
        print(df)
        
        while True:
            delete_task = input("What task do you want to remove?\n")
            filtered_rows = df[df['Task'] == delete_task]
            
            if not filtered_rows.empty:
                df.drop(df[df['Task'] == delete_task].index, inplace=True)
                df.to_csv('Task_info.csv')
                Task.Sr_no(file_name)
                break
            else:
                print(f"No task found with the name: {delete_task}")
    @classmethod
    def exit_code(cls , file_name):
        sys.exit()


def main():
    name = "Task_info.csv"
    with open(name, mode='a', newline='') as csv_file:
        ...
    while True:
        print("Task Tracker Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        while True:
            try:
                choise = int(input("Enter your choice (1-5): "))
            except ValueError:
                print("Invalid input")
                continue
            if choise not in range(1,6):
                print("Invalid input")
                continue
            break
            
        if choise == 1:
            Task.add_task(name)
        elif choise == 2:
            Task.view_task(name)
        elif choise == 3:
            Task.done_task(name)
        elif choise == 4:
            Task.del_task(name)
        elif choise == 5:
            Task.exit_code(name)

if __name__ == "__main__":
    main()

    