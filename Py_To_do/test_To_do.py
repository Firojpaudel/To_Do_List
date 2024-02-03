# In CLI first install pytest using pip install pytest
# Then run the test using pytest test_To_do.py
from To_do import ToDoList, Task

def test_add_task():
    # Arrange
    to_do_list = ToDoList()
    task = Task("Task 1", "This is the first task", False)
    
    # Act
    to_do_list.add_task(task)
    
    # Assert
    assert len(to_do_list.tasks) == 1
    assert to_do_list.tasks[0].title == "Task 1"
    assert to_do_list.tasks[0].description == "This is the first task"
    assert to_do_list.tasks[0].completed == False

def test_update_task_description():
    # Arrange
    to_do_list = ToDoList()
    task = Task("Task 1", "This is the first task", False)
    to_do_list.add_task(task)
    
    # Act
    to_do_list.update_task_description("Task 1", "This is the updated task")
    
    # Assert
    assert to_do_list.tasks[0].description == "This is the updated task"

def test_mark_task_as_completed():
    # Arrange
    to_do_list = ToDoList()
    task = Task("Task 1", "This is the first task", False)
    to_do_list.add_task(task)
    
    # Act
    to_do_list.mark_task_as_completed("Task 1")
    
    # Assert
    assert to_do_list.tasks[0].completed == True

def test_save_to_file():
    # Arrange
    to_do_list = ToDoList()
    task = Task("Task 1", "This is the first task", False)
    to_do_list.add_task(task)
    
    # Act
    to_do_list.save_to_file("test_file.txt")
    
    # Assert
    with open("test_file.txt", "r") as file:
        data = file.read()
        assert data == "Task 1,This is the first task,False\n"

def test_load_from_file():
    # Arrange
    to_do_list = ToDoList()
    with open("test_file.txt", "w") as file:
        file.write("Task 1,This is the first task,False\n")
    
    # Act
    to_do_list.load_from_file("test_file.txt")
    
    # Assert
    assert len(to_do_list.tasks) == 1
    assert to_do_list.tasks[0].title == "Task 1"
    assert to_do_list.tasks[0].description == "This is the first task"
    assert to_do_list.tasks[0].completed == False

def test_delete_task():
    # Arrange
    to_do_list = ToDoList()
    task = Task("Task 1", "This is the first task", False)
    to_do_list.add_task(task)
    
    # Act
    to_do_list.delete_task("Task 1")
    
    # Assert
    assert len(to_do_list.tasks) == 0
