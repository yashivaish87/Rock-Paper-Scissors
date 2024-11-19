import random
import tkinter as tk
from tkinter import messagebox

# ASCII art for rock, paper, and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]

def play(user_choice):
    if user_choice not in [0, 1, 2]:
        messagebox.showerror("Error", "Invalid choice! Please choose 0 for Rock, 1 for Paper, or 2 for Scissors.")
        return
    
    computer_choice = random.randint(0, 2)
    
    # clearing text widget
    result_text_widget.delete("1.0", tk.END)
    
    # color user choice
    result_text_widget.insert(tk.END, "Your choice:\n", "header")
    color_ascii_art(user_choice)
    result_text_widget.insert(tk.END, "\nComputer's choice:\n", "header")
    color_ascii_art(computer_choice)
    
    #display result
    if user_choice == 0 and computer_choice == 2:
        result = "You Won!"
    elif user_choice == 2 and computer_choice == 0:
        result = "You Lose!"
    elif computer_choice > user_choice:
        result = "You Lose!"
    elif computer_choice < user_choice:
        result = "You Won!"
    else:
        result = "It's a draw!"
    
    result_text_widget.insert(tk.END, "\n" + result, "result")

def color_ascii_art(choice):
    ascii_art = game_image[choice]
    tag = ""
    if choice == 0:
        tag = "rock"
    elif choice == 1:
        tag = "paper"
    elif choice == 2:
        tag = "scissors"
    result_text_widget.insert(tk.END, ascii_art, tag)

# main application window
root = tk.Tk()
root.title("Rock Paper Scissors")

# window size and background color
root.geometry("1000x700")
root.configure(bg="#282c34")

# frame for buttons
button_frame = tk.Frame(root, bg="#282c34")
button_frame.pack(side=tk.TOP, pady=20)

# buttons for user choices with colors
rock_button = tk.Button(button_frame, text="Rock", command=lambda: play(0), bg="#ff5733", fg="white", font=("Helvetica", 16, "bold"))
paper_button = tk.Button(button_frame, text="Paper", command=lambda: play(1), bg="#33c9ff", fg="white", font=("Helvetica", 16, "bold"))
scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play(2), bg="#33ff57", fg="white", font=("Helvetica", 16, "bold"))

rock_button.pack(side=tk.LEFT, padx=20, pady=10)
paper_button.pack(side=tk.LEFT, padx=20, pady=10)
scissors_button.pack(side=tk.LEFT, padx=20, pady=10)

# frame for result
result_frame = tk.Frame(root, bg="#282c34")
result_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# text widget to display the result with colors
result_text_widget = tk.Text(result_frame, bg="white", fg="#000000", font=("Courier", 18), wrap="word", height=20, width=50)
result_text_widget.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

#tags for coloring ASCII art
result_text_widget.tag_config("header", foreground="blue", font=("Helvetica", 20, "bold"))
result_text_widget.tag_config("result", foreground="red", font=("Helvetica", 20, "bold"))
result_text_widget.tag_config("rock", foreground="#ff5733")
result_text_widget.tag_config("paper", foreground="#33c9ff")
result_text_widget.tag_config("scissors", foreground="#33ff57")

# set minimum size of the window 
root.minsize(1000, 700)

# start the application
root.mainloop()
