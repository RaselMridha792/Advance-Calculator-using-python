import tkinter as tk
import math

# Function to handle button clicks
def on_click(text):
    current_text = entry_var.get()

    if text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    elif text == "√":
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
            result = math.sin(math.radians(float(current_text)))
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif text == "cos":
        try:
            result = math.cos(math.radians(float(current_text)))
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif text == "tan":
        try:
            result = math.tan(math.radians(float(current_text)))
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif text == "^":
        entry_var.set(current_text + "**")
    else:
        entry_var.set(current_text + text)

# Creating main window
root = tk.Tk()
root.title("Rasel Mridha - Scientific Calculator")
root.configure(bg="#1e1e1e")
root.geometry("400x600")

# Entry widget for input/output
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font="Arial 20", bg="#222", fg="white", bd=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=8, pady=15, padx=10)

# Button Layout (Grouped)
buttons = [
    ("7", "8", "9", "/", "C"),
    ("4", "5", "6", "*", "√"),
    ("1", "2", "3", "-", "^"),
    ("0", ".", "+", "log"),
    ("(", ")", "sin", "cos", "tan")
]

# Button Styling
btn_color = "#333"
text_color = "white"

# Create buttons using a loop
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        btn = tk.Button(root, text=btn_text, font="Arial 14 bold", bg=btn_color, fg=text_color,
                        padx=15, pady=15, relief="raised", bd=3,
                        command=lambda text=btn_text: on_click(text))
        btn.grid(row=i + 1, column=j, sticky="nsew", padx=5, pady=5)

# Add Bigger "=" Button (Spans 2 Columns)
equal_btn = tk.Button(root, text="=", font="Arial 14 bold", bg="#ff9800", fg="black",
                      padx=15, pady=15, relief="raised", bd=3,
                      command=lambda: on_click("="))
equal_btn.grid(row=4, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)  # Spanning 2 columns

# Adjusting row and column weights for responsiveness
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(5):
    root.grid_columnconfigure(j, weight=1)

# Run the application
root.mainloop()
