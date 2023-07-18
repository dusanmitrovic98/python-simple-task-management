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
    else:
        print("Task not found.")

def update_status(tasks, task_id):
    task = find_task_by_id(tasks, task_id)
    if task:
        new_status = input("Enter new task status (True/False): ").lower()
        if new_status == 'true':
            task['status'] = True
        elif new_status == 'false':
            task['status'] = False
        else:
            print("Invalid status value. Status not updated.")
            return
        print("Task status updated successfully.")
    else:
        print("Task not found.")

def display_tasks(tasks, level=0):
    for task in tasks:
        print('\t' * level, end='')
        print(f"ID: {task['id']}, Title: {task['title']}, Status: {'Completed' if task['status'] else 'Not Completed'}, Description: {task['description']}")
        display_tasks(task['children'], level + 1)

def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
        child_task = find_task_by_id(task['children'], task_id)
        if child_task:
            return child_task
    return None

def find_parent_task(tasks, task_id):
    for task in tasks:
        for child_task in task['children']:
            if child_task['id'] == task_id:
                return task
            parent_task = find_parent_task(child_task['children'], task_id)
            if parent_task:
                return parent_task
    return None

def save_tasks(tasks):
    filename = input("Enter file name to save tasks: ")
    try:
        with open(filename, 'w') as file:
            json.dump(tasks, file)
        print("Tasks saved successfully.")
