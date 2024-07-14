import tkinter as tk
from tkinter import messagebox

# Function to reverse the input text
def reverse_text():
    input_text = entry.get()
    reversed_text = input_text[::-1]
    result_label.config(text=reversed_text)

# Function to clear the input and result
def clear_text():
    entry.delete(0, tk.END)
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Text Reverser")
root.geometry("300x200")

# Create and place the widgets
entry_label = tk.Label(root, text="Enter text:")
entry_label.pack(pady=5)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

reverse_button = tk.Button(root, text="Reverse Text", command=reverse_text)
reverse_button.pack(pady=5)

result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_text)
clear_button.pack(pady=5)

# Start the application
root.mainloop()
