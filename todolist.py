import json
import os

DATA_FILE = 'todo_list.json'

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return {"tasks": [], "completed": []}
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_tasks(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_task(data):
    task = input("Enter task description: ")
    category = input("Enter category (e.g., Work, Personal): ")
    data["tasks"].append({"task": task, "category": category})
    print("✅ Task added!")

def view_tasks(data, completed=False):
    tasks = data["completed"] if completed else data["tasks"]
    if not tasks:
        print("No tasks found.")
        return
    
    filter_cat = input("Enter category to filter (or press Enter to show all): ")
    print("\n📋 Completed Tasks:" if completed else "\n📋 Current Tasks:")
    for idx, t in enumerate(tasks):
        if not filter_cat or t["category"].lower() == filter_cat.lower():
            print(f"{idx + 1}. {t['task']} [{t['category']}]")

def mark_task_completed(data):
    if not data["tasks"]:
        print("No tasks to mark as completed.")
        return
    
    view_tasks(data)
    try:
        index = int(input("Enter the number of the task to mark as completed: ")) - 1
        if 0 <= index < len(data["tasks"]):
            task = data["tasks"].pop(index)
            data["completed"].append(task)
            print("✅ Task marked as completed!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def remove_completed_task(data):
    if not data["completed"]:
        print("No completed tasks to remove.")
        return

    view_tasks(data, completed=True)
    try:
        index = int(input("Enter the number of the completed task to remove: ")) - 1
        if 0 <= index < len(data["completed"]):
            removed = data["completed"].pop(index)
            print(f"🗑️ Removed: {removed['task']}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    print("📌 Welcome to the To-Do List Manager!")
    data = load_tasks()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. View Completed Tasks")
        print("5. Remove Completed Task")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_task(data)
        elif choice == '2':
            view_tasks(data)
        elif choice == '3':
            mark_task_completed(data)
        elif choice == '4':
            view_tasks(data, completed=True)
        elif choice == '5':
            remove_completed_task(data)
        elif choice == '6':
            save_tasks(data)
            print("📁 Tasks saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
