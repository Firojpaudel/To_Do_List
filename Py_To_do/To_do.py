class Task:
    # constructor
    def __init__(self, title, description, completed):
        self.title = title
        self.description = description
        self.completed = completed

    # methods
    def mark_as_completed(self):
        self.completed = True  # marked the task as completed

    def update_description(self, new_description):
        self.description = new_description  # updated the description of the task

    def __str__(self):
        return f"{self.title} - {self.description} - {self.completed}"
        # returned the string representation of the task


class ToDoList:
    # Attributes:
    def __init__(self):
        self.tasks = []  # created an empty list

    # methods:
    def add_task(self, task):
        self.tasks.append(task)  # added a task to the list

    def update_task_description(self, task_title, new_description):
        for task in self.tasks:
            if task.title == task_title:
                task.update_description(new_description)  # updated the description of the task

    def mark_task_as_completed(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.mark_as_completed()  # marked the task as completed

    def delete_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                self.tasks.remove(task)  # deleted the task from the list
                print(f"Task: {task_title} deleted successfully")
                return
        print(f"No task found with the title: {task_title}")

    def save_to_file(self, file_name):
        with open(file_name, "w") as file:  # opening in write mode
            for task in self.tasks:
                file.write(f"{task.title},{task.description},{task.completed}\n")  # saved the tasks to a file

    def load_from_file(self, file_name):
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
                if not lines:
                    print(f"File '{file_name}' is empty.")
                    return
                for line in lines:
                    title, description, completed = line.strip().split(",")
                    task = Task(title, description, completed == "True")
                    self.tasks.append(task)
            print(f"Tasks loaded from {file_name} successfully")
        except FileNotFoundError:
            print(f"File '{file_name}' not found. Creating a new file.")
            with open(file_name, "w") as new_file:
                print("New file created.")
        except Exception as e:
            print(f"Error: An unexpected error occurred - {e}")


# UI part
# Giving a different twist: Since python does not have a switch case, I will define a switch making a dict ✅
def add_task(todo_list):
    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    completed = input("Enter the status of the task (True/False): ")
    task = Task(title, description, completed == "True")
    todo_list.add_task(task)
    print(f"Task: {task.title} added successfully")


def update_task_description(todo_list):
    title = input("Enter the title of the task: ")
    new_description = input("Enter the new description of the task: ")
    todo_list.update_task_description(title, new_description)
    print(f"Task_description of {title} updated successfully")


def mark_task_as_completed(todo_list):
    title = input("Enter the title of the task: ")
    todo_list.mark_task_as_completed(title)
    print(f"Task: {title} marked as completed successfully")


def delete_task(todo_list):
    title = input("Enter the title of the task: ")
    todo_list.delete_task(title)


def display_tasks(todo_list):
    for task in todo_list.tasks:
        print(task)


def save_to_file(todo_list):
    file_name = "tasks.txt"
    with open(file_name, "w") as file:
        for task in todo_list.tasks:
            file.write(f"{task.title},{task.description},{task.completed}\n")
    print(f"Tasks saved to {file_name} successfully")


def load_from_file(todo_list):
    file_name = input("Enter the name of the file to load tasks from: ")
    todo_list.load_from_file(file_name)


# For Exiting the program:
def exit_program(todo_list):
    print("Exiting the program")
    todo_list.save_to_file("tasks.txt")  # saving before exiting the program
    exit()


# Main function
def main():
    todo_list = ToDoList()
    todo_list.load_from_file("tasks.txt")  # loading the tasks from the file
    while True:  # loop goes on and on ♾️
        print("1. Add a task")
        print("2. Update the description of a task")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Display tasks")
        print("6. Save tasks to a file")
        print("7. Load tasks from a file")
        print("8. Exit")
        choice = int(input("Enter your choice (1 to 8): "))  # Type casting since input returns a string by default
        # Switch dictionary
        switch = {
            1: add_task,
            2: update_task_description,
            3: mark_task_as_completed,
            4: delete_task,
            5: display_tasks,
            6: save_to_file,
            7: load_from_file,
            8: exit_program
        }
        selected_case = switch.get(choice)
        if selected_case:
            selected_case(todo_list)
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
