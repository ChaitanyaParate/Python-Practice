import pandas as pd
from time import sleep
from datetime import date
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import win32service
import win32serviceutil
import win32event
import servicemanager
import socket
import sys

class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'MyService'
    _svc_display_name_ = 'My Service'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
        self.is_alive = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.is_alive = False

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()
    
    def email(self , task_due):
        sender_email = "example1@gmail.com"
        sender_password = "password"
        #Use app password
        
        recever_email = "example2@gmail.com"

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recever_email
        message["Subject"] = "Task Email"

        body = (f"These are the list of task whose due date is today\n\n{task_due}")
        
        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()

            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recever_email, message.as_string())

    def main(self):
        while self.is_alive:
            
            current_date = str(date.today())
            file_path = r"C:\Users\acer\OneDrive\Desktop\Python\Task Traker\Task_info.csv"
            df = pd.read_csv(file_path, index_col=0)
            filtered_rows = df[df['Due Date'] == current_date]
            filtered_rows = filtered_rows[filtered_rows['Status'] == "Incomplete"]
            
            Incomplete_task = filtered_rows.to_string(index=False)
            if filtered_rows.empty:
                ...
            else:
                self.email(Incomplete_task)
                
            sleep(86400)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(MyService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(MyService)