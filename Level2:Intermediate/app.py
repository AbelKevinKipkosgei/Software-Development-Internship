# Console application for basic CRUD operations
class Task:
    def __init__(self, task_name, task_description):
        self.task_name = task_name
        self.task_description = task_description
    
    def __str__(self):
        return f"Task: '{self.task_name}'\n Description: {self.task_description}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, task_description):
        new_task = Task(task_name, task_description)
        self.tasks.append(new_task)
        print(f"Task '{task_name}' added successfully.")

    def delete_task(self, task_index):
        try:
            deleted_task = self.tasks.pop(task_index)
            print(f"Task '{deleted_task.task_name}' deleted successfully.")
        except IndexError:
            print("Invalid task index.")

    def update_task(self, task_index, new_name=None, new_description=None):
        try:
            task = self.tasks[task_index]
            if new_name:
                task.task_name = new_name
            if new_description:
                task.task_description = new_description
            print(f"Task {task_index + 1} updated successfully.")
        except IndexError:
            print("Invalid task index.")
    
    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"Task: {index}")
                print(task)

def display_menu():
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Update Task")
    print("4. Display Tasks")
    print("5. Exit")

def main():
    task_manager = TaskManager()
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            task_name = input("Enter task name: ")
            task_description = input("Enter task description: ")
            task_manager.add_task(task_name, task_description)
        elif choice == "2":
            task_manager.display_tasks()
            try:
                task_index = int(input("Enter task index to delete: ")) - 1
                task_manager.delete_task(task_index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "3":
            task_manager.display_tasks()
            try:
                task_index = int(input("Enter task index to update: ")) - 1
                new_name = input("Enter new task name (press enter to skip): ")
                new_description = input("Enter new task description (press enter to skip): ")
                task_manager.update_task(task_index, new_name or None, new_description or None)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "4":
            task_manager.display_tasks()
        elif choice == "5":
            print("Exiting the Task Manager...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()