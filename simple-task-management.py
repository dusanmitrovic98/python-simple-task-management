import json

task_id_counter = 0

def get_next_task_id():
    global task_id_counter
    task_id_counter += 1
    return task_id_counter

def add_task(tasks, parent=None):
    title = input("Enter task title: ")
    description = input("Enter task description (optional): ")
    new_task = {'id': get_next_task_id(), 'title': title, 'status': False, 'description': description, 'children': []}

    if parent:
        parent['children'].append(new_task)
    else:
