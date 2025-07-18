import tkinter as tk
from tkinter import messagebox
import random

def check_winner():
    global winner
    for x in [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]:
        a, b, c = x
        if (
            buttons[a]["text"] == buttons[b]["text"]
            == buttons[c]["text"] != ""
        ):
            for i in x:
                buttons[i].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[a]['text']} wins!")
            winner = True
            return

    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        winner = True


def player_move(index):
    global winner
    if winner:
        return

    if buttons[index]["text"] == "":
        buttons[index]["text"] = "X"
        check_winner()

        if not winner:
            label.config(text="Computer's move (O)...")
            root.after(500, computer_move)


def computer_move():
    global winner
    if winner:
        return

    # First, try to block two Xs in a row
    for x in [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]:
        line = [buttons[i]["text"] for i in x]
        if line.count("X") == 2 and line.count("") == 1:
            empty_index = x[line.index("")]
            buttons[empty_index]["text"] = "O"
            check_winner()
            if not winner:
                label.config(text="Your move (X)")
            return

    # Else, pick a random empty cell
    empty_indices = [i for i, btn in enumerate(buttons) if btn["text"] == ""]
    if empty_indices:
        index = random.choice(empty_indices)
        buttons[index]["text"] = "O"
        check_winner()
        if not winner:
            label.config(text="Your move (X)")

# ---------------------------
# GUI Setup
# ---------------------------

root = tk.Tk()
root.title("Tic-Tac-Toe: You (X) vs Smart Computer (O)")

buttons = [
    tk.Button(root, text="", font=("normal", 25), width=6, height=2,
              command=lambda i=i: player_move(i))
    for i in range(9)
]

for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

label = tk.Label(root, text="Your move (X)", font=("normal", 14))
label.grid(row=3, column=0, columnspan=3, pady=10)

winner = False

root.mainloop()
