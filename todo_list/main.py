

tasks = []

def show_list():
    print("Your tasks:")
    for task in tasks:
        print(task)

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)

def delete_task():
    task_number = int(input("Enter the number of the task you want to delete: "))
    del tasks[task_number - 1]

def main():
    while True:
        print("1. Show list")
        print("2. Add task")
        print("3. Delete task")
        print("4. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            show_list()
        elif choice == 2:
            add_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            break
        else:
            print("Invalid choice.")

main()
    