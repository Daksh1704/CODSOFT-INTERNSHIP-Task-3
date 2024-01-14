import tkinter as tk
from tkinter import Label, Entry, Button, StringVar
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_clicked():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_var.set("Please enter a positive integer for the password length.")
            return
        password = generate_password(length)
        result_var.set(f"Your generated password is: {password}")
    except ValueError:
        result_var.set("Invalid input. Please enter a valid number.")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create and pack widgets
Label(window, text="Enter the desired length of the password:").pack(pady=10)
length_entry = Entry(window, width=20)
length_entry.pack(pady=5)

generate_button = Button(window, text="Generate Password", command=generate_button_clicked)
generate_button.pack(pady=10)

result_var = StringVar()
result_label = Label(window, textvariable=result_var)
result_label.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
