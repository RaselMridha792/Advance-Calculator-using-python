import tkinter as tk
import math

# Function to handle button clicks
def on_click(text):
    current_text = entry_var.get()

    if text == "=":
        try:
            result = eval(current_text.replace("x", "*"))  # Replace 'x' with '*'
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    elif text == "×":  # Backspace Functionality
        entry_var.set(current_text[:-1])
    elif text == "√":
        try:
            result = math.sqrt(float(current_text))
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif text == "π":  # Insert Pi Value
        entry_var.set(current_text + str(math.pi))
    elif text == "e":  # Insert Euler's Number
        entry_var.set(current_text + str(math.e))
    elif text == "ln":  # Natural Logarithm
        try:
            result = math.log(float(current_text))
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif text == "log":  # Log Base 10
        try:
            result = math.log10(float(current_text))
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif text == "10^x":  # 10 Power x
        try:
            result = 10 ** float(current_text)
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif text == "1/x":  # Reciprocal
        try:
            result = 1 / float(current_text)
            entry_var.set(result)
        except ZeroDivisionError:
            entry_var.set("Error")
    elif text == "x!":  # Factorial
        try:
            result = math.factorial(int(current_text))
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif text == "%":  # Percentage Functionality
        try:
            result = float(current_text) / 100
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
root.geometry("620x700")

# 🔹 Adding "Rasel Mridha" Label at the Top
title_label = tk.Label(root, text="Rasel Mridha", font="Arial 18 bold", fg="white", bg="#1e1e1e")
title_label.grid(row=0, column=0, columnspan=6, pady=10)

# 🔹 Input Box with Awesome Gradient Color
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font="Arial 40", bg="#444", fg="white", bd=5, relief="ridge", justify="right")
entry.grid(row=1, column=0, columnspan=6, ipadx=8, ipady=8, pady=10, padx=10)

# Button Layout (Grouped)
buttons = [
    ("7", "8", "9", "/", "C", "x!"),
    ("4", "5", "6", "x", "√", "1/x"),
    ("1", "2", "3", "-", "^", "10^x"),  
    ("0", "00", ".", "+", "log", "ln"), 
    ("(", ")", "sin", "cos", "tan", "π"), 
    ("e", "%", "×", "=", "")  
]

# 🔹 Scientific Buttons in Two Aligned Columns (Right Side)
scientific_buttons = [
    ("sin", "cos"),
    ("tan", "√"),
    ("π", "e"),
    ("log", "ln"),
    ("10^x", "1/x"),
    ("x!", "%"),
]

# Button Styling
btn_color = "#333"
text_color = "orange"

# Create main buttons using a loop
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        if btn_text:  # Avoid empty button space
            btn = tk.Button(root, text=btn_text, font="Arial 14 bold", bg=btn_color, fg=text_color,
                            padx=15, pady=15, relief="raised", bd=3,
                            command=lambda text=btn_text: on_click(text))
            btn.grid(row=i + 2, column=j, sticky="nsew", padx=5, pady=5)

# Create scientific buttons (aligned in two columns)
for i, (btn1, btn2) in enumerate(scientific_buttons):
    btn1_widget = tk.Button(root, text=btn1, font="Arial 14 bold", bg="#555", fg=text_color,
                            padx=15, pady=15, relief="raised", bd=3,
                            command=lambda text=btn1: on_click(text))
    btn1_widget.grid(row=i + 2, column=5, sticky="nsew", padx=5, pady=5)

    btn2_widget = tk.Button(root, text=btn2, font="Arial 14 bold", bg="#555", fg=text_color,
                            padx=15, pady=15, relief="raised", bd=3,
                            command=lambda text=btn2: on_click(text))
    btn2_widget.grid(row=i + 2, column=6, sticky="nsew", padx=5, pady=5)

# 🔹 Make "=" Button Bigger (2 Columns Wide)
equal_btn = tk.Button(root, text="=", font="Arial 14 bold", bg="#FF8C00", fg="white",
                      padx=15, pady=15, relief="raised", bd=3, command=lambda: on_click("="))
equal_btn.grid(row=7, column=4, columnspan=2, sticky="nsew", padx=5, pady=5)

# Start the main event loop
root.mainloop()
