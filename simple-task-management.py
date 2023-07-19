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
    except:
        print("Error saving tasks to file.")

def load_tasks():
    filename = input("Enter file name to load tasks: ")
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
        global task_id_counter
        task_id_counter = max(get_max_task_id(tasks), task_id_counter)
        print("Tasks loaded successfully.")
        return tasks
    except FileNotFoundError:
        print("File not found.")
    except:
        print("Error loading tasks from file.")
    return []

def get_max_task_id(tasks):
    max_id = 0
    for task in tasks:
        max_id = max(max_id, task['id'])
        max_id = max(max_id, get_max_task_id(task['children']))
    return max_id

def main():
    tasks = []

    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Edit Task")
        print("4. Update Task Status")
        print("5. Display Tasks")
        print("6. Save Tasks")
        print("7. Load Tasks")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            parent_id = input("Enter parent task ID (leave empty if no parent): ")
            parent = find_task_by_id(tasks, int(parent_id)) if parent_id else None
            add_task(tasks, parent)
        elif choice == '2':
            task_id = int(input("Enter task ID to remove: "))
            remove_task(tasks, task_id)
        elif choice == '3':
            task_id = int(input("Enter task ID to edit: "))
            edit_task(tasks, task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to update status: "))
            update_status(tasks, task_id)
        elif choice == '5':
            display_tasks(tasks)
        elif choice == '6':
            save_tasks(tasks)
        elif choice == '7':
            tasks = load_tasks()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

undefined
undefined
undefined
undefined
undefined
undefined
undefined
undefined
undefined
undefined
undefined
undefined
undefined
undefined
undefined
undefined
undefined
undefined
undefined
undefined
