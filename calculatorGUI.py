import tkinter as tk
from tkinter import StringVar

root = tk.Tk()
root.title("Calculator")
root.geometry("400x305")
root.config(bg="grey18")

def btnClick(item):
    global expression
    expression = expression + str(item)
    inputText.set(expression)

def btnClear():
    global expression
    expression = ""
    inputText.set("")

def btnEqual():
    global expression
    result = str(eval(expression))
    inputText.set(result)
    expression = ""
    expression += result

inputText = StringVar()
expression = ""

# Row 0
lable_title = tk.Label(root, text="Calculator", bg="grey18", fg="mediumpurple", font=("Lobster", 25, "bold"))
lable_title.grid(row=0, column=0, columnspan=4, pady=5)

#Row 1
entry = tk.Entry(root, borderwidth=0, textvariable=inputText, bg="grey30", fg="cyan", width=25, font=("Lucida Sans Typewriter", 20))
entry.grid(row=1, column=0, columnspan=4, sticky="nsew")

# Row 2
c = tk.Button(root, width=20, text="C", command=btnClear, fg="black",bg="mediumpurple3", activeforeground="black" , activebackground="mediumpurple4" ,font=("Arial", 15, "bold"))
c.grid(row=2, column=0, columnspan=3, sticky="nsew")

divide = tk.Button(root, width=5, text="/", command=lambda: btnClick("/"), fg="black",bg="mediumpurple3", activeforeground="black" , activebackground="mediumpurple4" ,font=("Arial", 15, "bold"))
divide.grid(row=2, column=3, sticky="nsew")

# Row 3
seven = tk.Button(root, width=5, text="7", command=lambda: btnClick("7"), fg="black",bg="mediumpurple", activeforeground="black" , activebackground="mediumpurple4" ,font=("Arial", 15, "bold"))
seven.grid(row=3, column=0, sticky="nsew")

eight = tk.Button(root, width=5, text="8", command=lambda: btnClick("8"), fg="black",bg="mediumpurple", activeforeground="black" , activebackground="mediumpurple4" ,font=("Arial", 15, "bold"))
eight.grid(row=3, column=1, sticky="nsew")

nine = tk.Button(root, width=5, text="9", command=lambda: btnClick("9"), fg="black",bg="mediumpurple", activeforeground="black" , activebackground="mediumpurple4" ,font=("Arial", 15, "bold"))
nine.grid(row=3, column=2, sticky="nsew")

multiply = tk.Button(root, width=5, text="*", command=lambda: btnClick("*"), fg="black",bg="mediumpurple3", activeforeground="black" , activebackground="mediumpurple4" ,font=("Arial", 15, "bold"))
multiply.grid(row=3, column=3, sticky="nsew")

# Row 4
four = tk.Button(root, width=5, text="4", command=lambda: btnClick("4"), fg="black",bg="mediumpurple", activeforeground="black" , activebackground="mediumpurple4" ,font=("Arial", 15, "bold"))
four.grid(row=4, column=0, sticky="nsew")

five = tk.Button(root, width=5, text="5", command=lambda: btnClick("5"), fg="black",bg="mediumpurple", activeforeground="black" , activebackground="mediumpurple4" ,font=("Arial", 15, "bold"))
five.grid(row=4, column=1, sticky="nsew")

six = tk.Button(root, width=5, text="6", command=lambda: btnClick("6"), fg="black",bg="mediumpurple", activeforeground="black" , activebackground="mediumpurple4" ,font=("Arial", 15, "bold"))
six.grid(row=4, column=2, sticky="nsew")

subtract = tk.Button(root, width=5, text="-", command=lambda: btnClick("-"), fg="black",bg="mediumpurple3", activeforeground="black" , activebackground="mediumpurple4" ,font=("Arial", 15, "bold"))
subtract.grid(row=4, column=3, sticky="nsew")


# Row 5
one = tk.Button(root, width=5, text="1", command=lambda: btnClick("1"), fg="black",bg="mediumpurple", activeforeground="black" , activebackground="mediumpurple4" ,font=("Arial", 15, "bold"))
one.grid(row=5, column=0, sticky="nsew")

two = tk.Button(root, width=5, text="2", command=lambda: btnClick("2"), fg="black",bg="mediumpurple", activeforeground="black" , activebackground="mediumpurple4" ,font=("Arial", 15, "bold"))
two.grid(row=5, column=1, sticky="nsew")

three = tk.Button(root, width=5, text="3", command=lambda: btnClick("3"), fg="black",bg="mediumpurple", activeforeground="black" , activebackground="mediumpurple4" ,font=("Arial", 15, "bold"))
three.grid(row=5, column=2, sticky="nsew")

add = tk.Button(root, width=5, text="+", command=lambda: btnClick("+"), fg="black",bg="mediumpurple3", activeforeground="black" , activebackground="mediumpurple4" ,font=("Arial", 15, "bold"))
add.grid(row=5, column=3, sticky="nsew")

# Row 6

zero = tk.Button(root, width=10, text="0", command=lambda: btnClick("0"), fg="black",bg="mediumpurple", activeforeground="black" , activebackground="mediumpurple4" ,font=("Arial", 15, "bold"))
zero.grid(row=6, column=0, columnspan=2,sticky="nsew")

decimal = tk.Button(root, width=5, text=".", command=lambda: btnClick("."), fg="black",bg="mediumpurple3", activeforeground="black" , activebackground="mediumpurple4" ,font=("Arial", 15, "bold"))
decimal.grid(row=6, column=2, sticky="nsew")

equalto = tk.Button(root, width=5, text="=", command=btnEqual, fg="black",bg="mediumpurple3", activeforeground="black" , activebackground="mediumpurple4" ,font=("Arial", 15, "bold"))
equalto.grid(row=6, column=3, sticky="nsew")

root.mainloop()
