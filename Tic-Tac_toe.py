
import tkinter as tk
from tkinter import messagebox

def check_Winner():
    global winner
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "" :
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            winner = True
            play_again = messagebox.askyesno("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins! 🎉\n\nDo you want to play again?")
            if play_again:
                reset_game()
            else:
                root.quit()
            return
    
    # Check for tie
    if all(button["text"] != "" for button in buttons) and not winner:
        play_again = messagebox.askyesno("Tic-Tac-Toe", "It's a Tie! 🤝\n\nDo you want to play again?")
        if play_again:
            reset_game()
        else:
            root.quit()

def reset_game():
    """Clear the board and reset state"""
    global winner, current_player
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")  # reset text & color
    winner = False
    current_player = "X"   # restart with X
    label.config(text=f"Player {current_player}'s turn")

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_Winner()
        if not winner:  # Only switch if game not over
            toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.resizable(False, False)


buttons = [tk.Button(root,text="",font=("normal",25),width=6, height=2,
                     command=lambda i=i:button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

current_player = "X"
winner = False

label = tk.Label(root,text=f"Player {current_player}'s turn",font=("normal",16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
