# CRUD application to store data persistently using file I/O
import os
class Task:
    def __init__(self, task_name, task_description):
        self.task_name = task_name
        self.task_description = task_description

    def __str__(self):
        return f"Task Name: '{self.task_name}'\nTask Description: {self.task_description}"
    
    def to_line(self):
        """Convert the task to a line for file storage"""
        return f"{self.task_name},{self.task_description}"
    
    @staticmethod
    def from_line(line):
        """Convert a line from file storage to a task"""
        task_name, task_description = line.strip().split(",", 1)
        return Task(task_name, task_description)

class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r") as file:
                    self.tasks = [Task.from_line(line) for line in file]
                print("Tasks loaded successfully.")
            else:
                print(f"No saved tasks found in '{self.filename}'.")
        except(IOError, ValueError) as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []
        
    def save_tasks(self):
        """Save tasks to the specified file."""
        try:
            with open(self.filename, "w") as file:
                for task in self.tasks:
                    file.write(task.to_line() + "\n")
            print(f"Tasks saved successfully to '{self.filename}'.")
        except IOError as e:
            print(f"Error saving tasks: {e}")

    def add_task(self, task_name, task_description):
        """Add a new task to the list."""
        new_task = Task(task_name, task_description)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task '{task_name}' added successfully.")

    def delete_task(self, task_index):
        """Delete a task from the list."""
        try:
            deleted_task = self.tasks.pop(task_index)
            self.save_tasks()
            print(f"Task '{deleted_task.task_name}' deleted successfully.")
        except IndexError:
            print("Invalid task index.")
    
    def update_task(self, task_index, new_name=None, new_description=None):
        """Update a task in the list."""
        try:
            task = self.tasks[task_index]
            if new_name:
                task.task_name = new_name
            if new_description:
                task.task_description = new_description
            self.save_tasks()
            print(f"Task '{task_index + 1}' updated successfully.")
        except IndexError:
            print("Invalid task index.")
    
    def display_tasks(self):
        """Display all tasks in the list."""
        if not self.tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"Task {index}: \n{task}")

def get_file_name():
    """Get the file name from the user."""
    while True:
        file_name = input("Enter the name of the file to save tasks (e.g., tasks.txt): ").strip()
        if file_name:
            return file_name
        print("File name cannot be empty. Please try again.")

def display_menu():
    """Display the main menu."""
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Update Task")
    print("4. Display Tasks")
    print("5. Exit")

def main():
    file_name = get_file_name()
    task_manager = TaskManager(file_name)

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            task_name = input("Enter task name: ").strip()
            task_description = input("Enter task description: ").strip()
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
                new_name = input("Enter new task name (press enter to skip): ").strip()
                new_description = input("Enter new task description (press enter to skip): ").strip()
                task_manager.update_task(task_index, new_name or None, new_description or None)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "4":
            task_manager.display_tasks()
        elif choice == "5":
            print("Exiting the program ...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()