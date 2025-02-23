import tkinter as tk
from tkinter import messagebox
import math

# Function to handle button click
def on_click(event):
    text = event.widget.cget("text")
    current_text = entry_var.get()

    if text == "=":
        try:
            # Try to evaluate the expression
            result = eval(current_text)
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")
            messagebox.showerror("Error", "Invalid Input!")
    elif text == "C":
        entry_var.set("")
    elif text == "M+":
        try:
            memory = float(entry_var.get())
            memory_var.set(memory_var.get() + memory)
            entry_var.set("")
        except ValueError:
            entry_var.set("Error")
    elif text == "M-":
        try:
            memory = float(entry_var.get())
            memory_var.set(memory_var.get() - memory)
            entry_var.set("")
        except ValueError:
            entry_var.set("Error")
    elif text == "MR":
        entry_var.set(memory_var.get())
    elif text == "MC":
        memory_var.set(0)
        entry_var.set("")
    elif text == "√":  # Handle sqrt
        try:
            result = math.sqrt(float(current_text))
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif text == "log":
        try:
            result = math.log(float(current_text))
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif text == "sin":
        try:
            result = math.sin(math.radians(float(current_text)))  # sin in radians
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif text == "cos":
        try:
            result = math.cos(math.radians(float(current_text)))  # cos in radians
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif text == "tan":
        try:
            result = math.tan(math.radians(float(current_text)))  # tan in radians
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif text == "^":
        entry_var.set(current_text + "**")  # Use Python exponentiation
    else:
        entry_var.set(current_text + text)

# GUI Window setup
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x600")
root.configure(bg="black")

entry_var = tk.StringVar()

title_label = tk.Label(root, text="Rasel Mridha", font="Arial 16 bold", bg="black", fg="white")
title_label.pack(fill="both", pady=10)


# Entry widget for displaying input and output
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", justify="right", bd=10)
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

memory_var = tk.DoubleVar(value=0)
# Buttons layout for calculator
buttons = [
("7", "8", "9", "/", "M+"),
    ("4", "5", "6", "*", "M-"),
    ("1", "2", "3", "-", "MR"),
    ("0", ".", "C", "+", "MC"),
    ("(", ")", "=", "√", "^"),  
    ("log", "sin", "cos", "tan")
]

frame = tk.Frame(root)
frame.pack()

# Create and pack buttons in the grid
for row in buttons:
    btn_row = tk.Frame(frame)
    btn_row.pack(side="top", fill="both", expand=True)
    for btn_text in row:
        btn = tk.Button(btn_row, text=btn_text, font="Arial 16 bold", padx=20, pady=20)
        btn.pack(side="left", fill="both", expand=True)
        btn.bind("<Button-1>", on_click)

root.mainloop()
