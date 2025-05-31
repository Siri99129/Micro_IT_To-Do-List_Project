def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. View tasks")
    print("2. Add a new task")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Exit")
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{index}. {task['title']} [{status}]")
def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    print(f"Task '{title}' added successfully.")
def mark_complete(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    task_num = int(input("Enter task number to mark as complete: "))
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = True
        print(f"Task '{tasks[task_num - 1]['title']}' marked as complete.")
    else:
        print("Invalid task number.")
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    task_num = int(input("Enter task number to delete: "))
    if 0 < task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        print(f"Task '{removed['title']}' deleted.")
    else:
        print("Invalid task number.")
def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exit")
            break
        else:
            print("Invalid option. Please choose again.")
if __name__ == "__main__":
    main()
