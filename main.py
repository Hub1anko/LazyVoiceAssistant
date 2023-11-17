'''
Author: Hubert Waleńczak

Using classes for shit and giggles. And for learning.

Limitations
Limited estimation to full hours
'''
from TaskDataExtractor import TaskDataExtractor as TDE
from SaveToExcel import SaveToExcel as STE
from microphone_recognition_gpu import recognize
from datetime import datetime

# Example usage:
#input_text = "Start some text here, task type task..., expected time 10 hours,"

# Find matches in text
Extarctor = TDE()
Recognizer = recognize()
#Extarctor.find_start_end(input_text)

# Variables to save in excel
#Task = Extarctor.Task
#TaskType = Extarctor.TaskType
#Time = Extarctor.Time
#Date = datetime.now().date()
#StartTime = datetime.now().time()

# ------------- #
# Save to Excel #
# ------------- #

excel_filename = 'test.xlsx'
#Saver = STE(Task, TaskType, Time, Date, StartTime, excel_filename)
#Saver.SaveToExcel()

# TO-DO: Add Stop command with optional 'Notes' or stop after new Start.
while 1:
    input_text = Recognizer.recognize()
    if input_text != None:
        Extarctor.init()
        Extarctor.find_start_end(input_text)

        # Variables to save in excel
        Task = Extarctor.Task
        TaskType = Extarctor.TaskType
        Time = Extarctor.Time
        Date = datetime.now().date()
        StartTime = datetime.now().time()

        Saver = STE(Task, TaskType, Time, Date, StartTime, excel_filename)
        Saver.SaveToExcel()