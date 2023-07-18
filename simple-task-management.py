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
        tasks.append(new_task)

    print("Task added successfully.")

def remove_task(tasks, task_id):
    task = find_task_by_id(tasks, task_id)
    if task:
        parent = find_parent_task(tasks, task_id)
        if parent:
            parent['children'].remove(task)
        else:
            tasks.remove(task)
        print("Task removed successfully.")
    else:
        print("Task not found.")

def edit_task(tasks, task_id):
    task = find_task_by_id(tasks, task_id)
    if task:
        new_title = input("Enter new task title: ")
        new_description = input("Enter new task description (optional): ")
        task['title'] = new_title
        task['description'] = new_description
        print("Task edited successfully.")
