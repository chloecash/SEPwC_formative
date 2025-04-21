"""A simple command line to-do list application"""

import argparse
import os

TASK_FILE = ".tasks.txt"

def add_task(task):
    """Adds a new task to the to-do list file
    
    Args:
        task (str): The task to be added.
    """
    with open(TASK_FILE, "a", encoding="utf-8") as file:
        file.write(task + "\n")

def list_tasks():
    """Lists all tasks from the to-do list file.
    
    Returns:
        str: A formatted string containing all tasks with their index,
        or an empty string if the file doesn't exist or is empty.
    """
    with open(TASK_FILE, 'r', encoding="utf-8") as file:
        tasks = file.readlines()
        counter = 1
        output_string =""
        for task in tasks:
            output_string = output_string + str(counter) + ". "+task
            counter = counter + 1
        return output_string.rstrip()

def remove_task(index):
    """Removes a task from the to-do list file based on its index.
    
    Args:
        index (str): The index of the task to remove.
    """
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r', encoding="utf-8") as file:
            tasks = file.readlines()
        with open(TASK_FILE, 'w', encoding="utf-8") as file:
            for i, task in enumerate(tasks, start=1):
                if i != index:
                    file.write(task)
        print("Task Successfully Removed")
    else:
        print("Task not found")

def main():
    """Parses command-line arguments and executes the corresponding to-do list action."""
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
            "-a",
            "--add",
            help="Add a new task"
            )
    parser.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="List all tasks")
    parser.add_argument(
            "-r",
            "--remove",
            help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
