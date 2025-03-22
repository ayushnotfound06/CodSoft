import tkinter as tk
from tkinter import messagebox

def addTask():
    task = entry.get()
    if task:
        todo_list.insert(tk.END ,task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def deleteTask():
    try:
        selecttask = todo_list.curselection()[0]
        todo_list.delete(selecttask)

    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clearTask():
    todo_list.delete(0, tk.END)
    done_list.delete(0, tk.END)
    entry.delete(0, tk.END)

def doneTask():
    try:
        taskDone = todo_list.curselection()[0]
        task = todo_list.get(taskDone)
        done_list.insert(tk.END, task)
        todo_list.delete(taskDone)
    except:
        messagebox.showwarning("Warning", "Please select a task that you have done!")


root = tk.Tk()
root.title("To-Do List")
root.config(bg="grey18")
root.geometry("650x450")

# Row 0
lable_title = tk.Label(root, text="To-Do List", bg="grey18", fg="mediumpurple", font=("Lobster", 20, "bold"))
lable_title.grid(row=0, column=1, pady=10)


# Row 1
entry = tk.Entry(root, width=30, borderwidth=1, fg='cyan', bg='grey30', font=("Lucida Sans Typewriter", 15))
entry.grid(row=1, column=0, padx=10, columnspan=2)

btn_add = tk.Button(root, text="Add Task", bg="dodger blue", activeforeground="dodger blue", width=10, font=("Arial", 10, "bold" ), command=addTask)
btn_add.grid(row=1, column=2)

#Row 2
btn_delete = tk.Button(root, text="Delete", bg="dodger blue", activeforeground="dodger blue", width=10,font=("Arial", 10, "bold" ), command=deleteTask)
btn_delete.grid(row=2, column=2, pady=0)

#Row 3
btn_clear = tk.Button(root, text="Clear All", bg="dodger blue", activeforeground="dodger blue", width=10, font=("Arial", 10, "bold" ), command=clearTask)
btn_clear.grid(row=3, column=2, pady = 0)

# Row 4
label_todo = tk.Label(root, text="To-Do", font=("Lucida Sans Typewriter", 15, "bold"), fg="RoyalBlue2", bg= 'grey18')
label_todo.grid(row=4, column=0, pady= 5)

label_done = tk.Label(root, text="Done", font=("Lucida Sans Typewriter", 15, "bold"), fg="RoyalBlue2", bg= 'grey18')
label_done.grid(row=4, column=2, pady=5)

#Row5
todo_list = tk.Listbox(root, width=20, height=10, borderwidth=1, fg='cyan', bg='grey30', font=("Lucida Sans Typewriter", 15))
todo_list.grid(row=5, column=0, padx=10, pady=5)

btn_done = tk.Button(root, text="Done ->", bg="mediumpurple3", activeforeground="purple" , activebackground="grey10", width=10,font=("Arial", 10, "bold" ), command=doneTask)
btn_done.grid(row=5, column=1)

done_list = tk.Listbox(root, width=20, height=10, borderwidth=1,fg='cyan', bg='grey30', font=("Lucida Sans Typewriter", 15))
done_list.grid(row=5, column=2, padx=10, pady=5)

root.mainloop()