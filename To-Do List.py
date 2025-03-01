def showTasks(tasks):
    if not tasks:
        print("No Task remaining.\n")
    else:
        print("Your Remaining Tasks:\n")

        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

def addTask(tasks):
    a_Task = input("Enter task to add: ")
    try:
        position = int(input(f"Enter position (1 to {len(tasks) + 1}): ")) - 1
        if position < 0 or position > len(tasks):
            print("Invalid Position.\n")
        else:
            tasks.insert(position, a_Task)
            print("Task Added!\n")
    except ValueError:
        print("Invalid input! Please enter a number.\n")

def removeTask(tasks):
    try:
        if not tasks:
            print("No tasks to remove.\n")
            return

        position = int(input(f"Enter the task position (1 to {len(tasks)}): ")) - 1
        if position < 0 or position >= len(tasks):
            print("Invalid Position.\n")
        else:
            removed = tasks.pop(position)
            print(f"Task '{removed}' removed!\n")
    except ValueError:
        print("Invalid input! Please enter a number.\n")             
        
def main():
    tasks = []
    while True:
        print("\nTO-DO LIST")
        print("1. Show Your Task")
        print("2. Add A New Task")
        print("3. Remove Task")
        print("4. Exit")
        
        option = input("Choose an option: ")

        if option.isdigit():
            option = int(option)
            if option == 1:
                showTasks(tasks)
            elif option == 2:
                addTask(tasks)
            elif option == 3:
                removeTask(tasks)
            elif option == 4:
                print("Goodbye!\n")
                break
            else:
                print("Invalid Number. Please choose between 1-4.\n")
        else:
            print("Invalid input! Please enter a number.\n")

if __name__ == "__main__":
    main()
