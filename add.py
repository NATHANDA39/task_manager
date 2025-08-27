# def add_tasks(task):
#      #save task to database 
#      # Return resonse 
#      return True

from db import tasks

def add_tasks(task):
    #save task to database 
    tasks.insert_one(task)
    #Return response
    return True