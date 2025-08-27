import db

def save_task(task):
    db.tasks.insert_one(task)
    #save task to database
    #Return response
    return True

def delete_task(id):
    #Delete task from database
    db.tasks.delete_one({"_id": id})
    #Return response
    return True

def update_task(task, update):
    #update task in database
    #Return response
    return True

def get_tasks():
    # Get all task from database
    all_tasks = db.tasks.find()
    # Return response
    return all_tasks