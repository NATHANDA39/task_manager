from db import tasks

def show_tasks():
     #Get all task from database
     all_tasks = tasks.find()

     #Return response 
     return all_tasks


