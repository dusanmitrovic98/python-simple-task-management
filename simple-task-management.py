import json

task_id_counter = 0

def get_next_task_id():
    global task_id_counter
    task_id_counter += 1
    return task_id_counter

def add_task(tasks, parent=None):
