import tkinter as tk
import random
from tkinter import messagebox

urPlay = 0  # default value 0 hai (0 is rock, 1 is paper, 2 is scissor).
myScore = 0
computerScore = 0


def rockPlay():
    global urPlay
    urPlay = 0
    result()

def paperPlay():
    global urPlay
    urPlay = 1
    result()

def scissorPlay():
    global urPlay
    urPlay = 2
    result()

def result():
    global myScore, computerScore
    computer = random.randint(0, 2)
    choice = ["Rock", "Paper", "Scissor"]
    computerPlay = choice[computer]
    myPlay = choice[urPlay]

    if myPlay == computerPlay:
        result_text = f"Tie!"
    elif (urPlay == 0 and computer == 2) or (urPlay == 1 and computer == 0) or (urPlay == 2 and computer == 1):
        myScore += 1
        result_text = f"You Win!"
    else:
        computerScore += 1
        result_text = f"You Lose!"

    editbox.insert(tk.END, f"Your Choice: {myPlay}\nComputer's Choice: {computerPlay}\n{result_text}\n\n")
    scoreLabel.config(text=f"Your Score: {myScore}  |  Computer's Score: {computerScore}")

    playAgain()


def playAgain():
    answer = messagebox.askyesno("Play Again?", "Do you want to play another round?")
    if answer:
        resetGame()
    else:
        root.quit()


def resetGame():
    global urPlay
    urPlay = 0
    editbox.delete(1.0, tk.END)


root = tk.Tk()
root.title("Rock-Paper-Scissor Game")
root.geometry("600x350")
root.config(bg="grey18")

# Row 0-------------------------------
lableTitle = tk.Label(root, text="Rock-Paper-Scissor Game", fg="mediumpurple", bg="grey18", font=("lobster", 20, "bold"))
lableTitle.grid(row=0, column=0, pady=10, columnspan=2)

# Row 1-----------------------------------
frame = tk.LabelFrame(root, text="Your Play", fg="White", bg="grey18", font=("Arial", 10))
frame.grid(row=1, column=0, padx=20)

rockBtn = tk.Button(frame, text="Rock", command=rockPlay, fg="Black", bg="dodger blue", width=8,activeforeground="dodger blue3", font=("Arial", 15, "bold"))
rockBtn.grid(row=0, column=0, padx=12, pady=8)

paperBtn = tk.Button(frame, text="Paper", command=paperPlay, fg="Black", bg="dodger blue", width=8,activeforeground="dodger blue3", font=("Arial", 15, "bold"))
paperBtn.grid(row=1, column=0, padx=12, pady=8)

scissorBtn = tk.Button(frame, text="Scissor", command=scissorPlay, fg="Black", bg="dodger blue", width=8,activeforeground="dodger blue3", font=("Arial", 15, "bold"))
scissorBtn.grid(row=2, column=0, padx=12, pady=8)

editbox = tk.Text(root, fg="Cyan", bg="grey25", width=40, height=10, font=("Lucida Sans Typewriter", 12))
editbox.grid(row=1, column=1, padx=10)

# Row 2---------------------------------
scoreLabel = tk.Label(root, text=f"Your Score: {myScore}  |  Computer's Score: {computerScore}", fg="cyan",bg="grey18", font=("Arial", 12))
scoreLabel.grid(row=2, column=0, pady=20, columnspan=2)



root.mainloop()
