import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def deletebtn():
    seleteditem = treeview.selection()
    if seleteditem:
        for item in seleteditem:
            treeview.delete(item)
        messagebox.showinfo("Sucess", "Contact Sucessfully Deleted.")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")
        return


def editbtn():
    selectedItem = treeview.selection()
    if not selectedItem:
        messagebox.showwarning("Selection Error", "Please select a contact to edit.")
        return

    selectedValues = treeview.item(selectedItem)["values"]

    def editContact():
        updated_values = (editnameEntry.get(), editphoneEntry.get(), editemailEntry.get(), editaddressEntry.get())
        if all(updated_values):
            treeview.item(selectedItem, values=updated_values)
            editroot.destroy()
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    editroot = tk.Tk()
    editroot.geometry("400x250")
    editroot.config(bg="grey18")
    editroot.title("Edit Contact")

    label1 = tk.Label(editroot, text="Modify Contact Details", font=("Arial", 15, "bold"), bg="grey18", fg="mediumpurple")
    label1.grid(row=0, column=0, columnspan=2, pady=10, padx=40)

    label2 = tk.Label(editroot, text="Name:", font=("Arial", 10), bg="grey18", fg="dodger blue")
    label2.grid(row=1, column=0, pady=5)
    label3 = tk.Label(editroot, text="Phone No.:", font=("Arial", 10), bg="grey18", fg="dodger blue")
    label3.grid(row=2, column=0, pady=5)
    label4 = tk.Label(editroot, text="Email:", font=("Arial", 10), bg="grey18", fg="dodger blue")
    label4.grid(row=3, column=0, pady=5)
    label5 = tk.Label(editroot, text="Address:", font=("Arial", 10), bg="grey18", fg="dodger blue")
    label5.grid(row=4, column=0, pady=5)

    editnameEntry = tk.Entry(editroot, font=("Lucida Sans Typewriter", 10), fg="cyan", borderwidth=1, width=25, bg="grey25")
    editnameEntry.grid(row=1, column=1, columnspan=2, pady=5)
    editnameEntry.insert(0, selectedValues[0])

    editphoneEntry = tk.Entry(editroot, font=("Lucida Sans Typewriter", 10), fg="cyan", borderwidth=1, width=25, bg="grey25")
    editphoneEntry.grid(row=2, column=1, columnspan=2, pady=5)
    editphoneEntry.insert(0, selectedValues[1])

    editemailEntry = tk.Entry(editroot, font=("Lucida Sans Typewriter", 10), fg="cyan", borderwidth=1, width=25, bg="grey25")
    editemailEntry.grid(row=3, column=1, columnspan=2, pady=5)
    editemailEntry.insert(0, selectedValues[2])

    editaddressEntry = tk.Entry(editroot, font=("Lucida Sans Typewriter", 10), fg="cyan", borderwidth=1, width=25, bg="grey25")
    editaddressEntry.grid(row=4, column=1, columnspan=2, pady=5)
    editaddressEntry.insert(0, selectedValues[3])

    editBtn = tk.Button(editroot, text="Modify", command=editContact, bg="dodger blue", fg="black", width=8, activeforeground="dodger blue3", font=("Arial", 10, "bold"))
    editBtn.grid(row=5, column=2, pady=10)


def addbtn():

    def addContact():
        name = nameEntry.get()
        phone = phoneEntry.get()
        email = emailEntry.get()
        address = addressEntry.get()

        if name and phone and email and address:
            treeview.insert("", tk.END, values=(name, phone, email, address))
            addroot.destroy()
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    addroot = tk.Tk()
    addroot.geometry("400x250")
    addroot.config(bg="grey18")
    addroot.title("Add Contact")

    label1 = tk.Label(addroot, text="Add Contact Details", font=("Arial", 15, "bold"), bg="grey18", fg="mediumpurple")
    label1.grid(row=0, column=0, columnspan=2, pady=10, padx=50)

    label2 = tk.Label(addroot, text="Name:", font=("Arial", 10), bg="grey18", fg="dodger blue")
    label2.grid(row=1, column=0, pady=5)
    label3 = tk.Label(addroot, text="Phone No.:", font=("Arial", 10), bg="grey18", fg="dodger blue")
    label3.grid(row=2, column=0, pady=5)
    label4 = tk.Label(addroot, text="Email:", font=("Arial", 10), bg="grey18", fg="dodger blue")
    label4.grid(row=3, column=0, pady=5)
    label5 = tk.Label(addroot, text="Address:", font=("Arial", 10), bg="grey18", fg="dodger blue")
    label5.grid(row=4, column=0, pady=5)

    nameEntry = tk.Entry(addroot, font=("Lucida Sans Typewriter", 10), fg="cyan", borderwidth=1, width=25, bg="grey25")
    nameEntry.grid(row=1, column=1, columnspan=2, pady=5)
    phoneEntry = tk.Entry(addroot, font=("Lucida Sans Typewriter", 10), fg="cyan", borderwidth=1, width=25, bg="grey25")
    phoneEntry.grid(row=2, column=1, columnspan=2, pady=5)
    emailEntry = tk.Entry(addroot, font=("Lucida Sans Typewriter", 10), fg="cyan", borderwidth=1, width=25, bg="grey25")
    emailEntry.grid(row=3, column=1, columnspan=2, pady=5)
    addressEntry = tk.Entry(addroot, font=("Lucida Sans Typewriter", 10), fg="cyan", borderwidth=1, width=25, bg="grey25")
    addressEntry.grid(row=4, column=1, columnspan=2, pady=5)

    doneBtn = tk.Button(addroot, text="Add", command=addContact, bg="dodger blue", fg="black", width=8, activeforeground="dodger blue3", font=("Arial", 10, "bold"))
    doneBtn.grid(row=5, column=2, pady=10)


root = tk.Tk()
root.title("Contact Book")
root.configure(bg="grey18")
root.geometry("890x350")

# Row 0
titleLable= tk.Label(root, text = "Contact Book", bg="grey18", fg= "mediumpurple", font=("lobster", 30, "bold"))
titleLable.grid(row=0, column=0, columnspan=2, pady=5)

# Row 1
# Treeview part--------------------------------------------------------------------
style = ttk.Style()
style.configure("Treeview.Heading", font=("Lucida Sans Typewriter", 10, "bold"), fg="black")

treeview = ttk.Treeview(root, columns=("name", "phone", "email", "address"), show="headings")

treeview.heading("name", text="Name")
treeview.heading("phone", text="Phone Number")
treeview.heading("email", text="Email")
treeview.heading("address", text="Address")

treeview.column("name", width=100)
treeview.column("phone", width=150)
treeview.column("email", width=200)
treeview.column("address", width=200)
treeview.grid(row=1, column=0, padx=20, pady=20)

# frame and buttons part --------------------------------------------------------------------
frame1 = tk.LabelFrame(root, text="Options", fg="white", bg="grey18", font=("Arial", 12))
frame1.grid(row=1, column=1)

addButton = tk.Button(frame1, text="Add", command=addbtn, bg="dodger blue", fg="black", width=10, activeforeground="dodger blue3", font=("Arial", 15, "bold"))
addButton.grid(row=0, column=0, pady=10, padx=20)

editButton = tk.Button(frame1, text="Edit", command=editbtn, bg="dodger blue", fg="black", width=10, activeforeground="dodger blue3", font=("Arial", 15, "bold"))
editButton.grid(row=1, column=0,pady=14, padx=20)

deleteButton = tk.Button(frame1, text="Delete", command=deletebtn, bg="dodger blue", fg="black", width=10, activeforeground="dodger blue3", font=("Arial", 15, "bold"))
deleteButton.grid(row=2, column=0,pady=14, padx=20)

root.mainloop()
