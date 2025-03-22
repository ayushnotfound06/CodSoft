import random
import tkinter as tk
from tkinter.constants import HORIZONTAL

uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercaseLetters = uppercaseLetters.lower()
digits = "0123456789"
specialChars = "~`!@#$%^&*()_-+={[}]|:;'<,>.?/"


def gen():
    allChars = ""
    halfPassword = ""
    length = lenScale.get()

    if checkUpper.get():
        allChars += uppercaseLetters
        halfPassword += random.choice(uppercaseLetters)
    if checkLower.get():
        allChars += lowercaseLetters
        halfPassword += random.choice(lowercaseLetters)
    if checkDigit.get():
        allChars += digits
        halfPassword += random.choice(digits)
    if checkSymbols.get():
        allChars += specialChars
        halfPassword += random.choice(specialChars)

    if not allChars:
        passEntry.delete(0, tk.END)
        passEntry.insert(0, "Select at least one!")
        return

    newLen = length - len(halfPassword)
    password = halfPassword + "".join(random.sample(allChars, newLen))

    passEntry.delete(0, tk.END)
    passEntry.insert(0, password)


def copyClipboard():
    root.clipboard_clear()
    root.clipboard_append(passEntry.get())
    root.update()


# Tkinter part -----------------------------------------------------------------------------------------------------
root = tk.Tk()
root.title("Password Generator")
root.config(bg="grey18")
root.geometry("440x400")

# Row 0
lableTitle = tk.Label(root, text="Password Generator", fg="mediumpurple", bg="grey18", font=("lobster", 20, "bold"))
lableTitle.grid(row=0, column=0, padx=100, pady=10, columnspan=2)

# Row 1
labelFrame1 = tk.LabelFrame(root, text="Password Settings", fg="white", bg="grey18", font=("Arial", 12))
labelFrame1.grid(row=1, column=0, columnspan=2)

checkUpper = tk.BooleanVar(value=True)
upperCheck = tk.Checkbutton(labelFrame1, text="Uppercase (A-Z)", variable=checkUpper, selectcolor="grey18",activebackground="Grey18", activeforeground="SeaGreen3", fg="SeaGreen3", bg="grey18",font=("Arial", 12))
upperCheck.grid(row=0, column=0, sticky=tk.W)

checkLower = tk.BooleanVar(value=True)
lowerCheck = tk.Checkbutton(labelFrame1, text="Lowercase (a-z)", variable=checkLower, selectcolor="grey18",activebackground="Grey18", activeforeground="SeaGreen3", fg="SeaGreen3", bg="grey18", font=("Arial", 12))
lowerCheck.grid(row=0, column=1, sticky=tk.W)

checkDigit = tk.BooleanVar(value=True)
numCheck = tk.Checkbutton(labelFrame1, text="Numbers (0-9)", variable=checkDigit, selectcolor="grey18",activebackground="Grey18", activeforeground="SeaGreen3", fg="SeaGreen3", bg="grey18", font=("Arial", 12))
numCheck.grid(row=1, column=0, sticky=tk.W)

checkSymbols = tk.BooleanVar(value=True)
symbolsCheck = tk.Checkbutton(labelFrame1, text="Symbols (!-$^+)", variable=checkSymbols, selectcolor="grey18",activebackground="Grey18", activeforeground="SeaGreen3",fg="SeaGreen3", bg="grey18",font=("Arial", 12))
symbolsCheck.grid(row=1, column=1, sticky=tk.W)

# Row 2
labelFrame2 = tk.LabelFrame(root, text="Password Length", fg="white", bg="grey18", font=("Arial", 12))
labelFrame2.grid(row=2, column=0, columnspan=2)

sliderLable = tk.Label(labelFrame2, text="Password Length", fg="SeaGreen3", bg="grey18", font=("Arial", 15))
sliderLable.grid(row=0, column=0, columnspan=2)

lenScale = tk.Scale(labelFrame2, from_=4, to=20, orient=HORIZONTAL, borderwidth=0, length=260, bg="grey18",fg="SeaGreen3", font=("Arial", 10))
lenScale.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
lenScale.set(10)

# Row 3
passEntry = tk.Entry(root, width=25, fg="cyan", bg="grey25", borderwidth=1, font=("Lucida Sans Typewriter", 15))
passEntry.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

# Row 4
genButton = tk.Button(root, width=15, text="Generate", command=gen, fg="Black", bg="dodger blue", activeforeground="dodger blue3", font=("Arial", 15, "bold"))
genButton.grid(row=4, column=0, padx=15, pady=10)

copyButton = tk.Button(root, width=15, text="Copy To Clipboard", command=copyClipboard, fg="Black",bg="dodger blue", activeforeground="dodger blue3" ,font=("Arial", 15, "bold"))
copyButton.grid(row=4, column=1, padx=15, pady=10)

root.mainloop()
