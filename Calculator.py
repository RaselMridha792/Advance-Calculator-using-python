import tkinter as tk
import math

# Variable to track if the mode is degree or radian
is_degrees = True

# Function to handle button clicks
def on_click(text):
    global is_degrees
    current_text = entry_var.get()

    if text == "=":
        if not current_text:  # If the input is empty, return 0.
            entry_var.set("0.")
        else:
            try:
                # Replace 'x' with '*' for multiplication and eval the expression
                result = eval(current_text.replace("x", "*"))
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
            if is_degrees:
                # Convert to radians if degrees mode is selected
                current_text = current_text.replace("°", "")
                result = math.sin(math.radians(float(current_text)))
            else:
                result = math.sin(float(current_text))
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif text == "cos":
        try:
            if is_degrees:
                current_text = current_text.replace("°", "")
                result = math.cos(math.radians(float(current_text)))
            else:
                result = math.cos(float(current_text))
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif text == "tan":
        try:
            if is_degrees:
                current_text = current_text.replace("°", "")
                result = math.tan(math.radians(float(current_text)))
            else:
                result = math.tan(float(current_text))
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif text == "^":
        entry_var.set(current_text + "**")
    elif text == "deg":  # Toggle degree/radian mode and insert the degree symbol (°)
        is_degrees = not is_degrees
        entry_var.set(f"Mode: {'Degrees' if is_degrees else 'Radians'}")
    else:
        entry_var.set(current_text + text)

# Creating main window
root = tk.Tk()
root.title("@Rasel Mridha - Scientific Calculator, Satkhira Polytechnic Institute")
root.configure(bg="#00A2AE")
root.geometry("630x700")

# 🔹 Adding "Rasel Mridha" Label at the Top
title_label = tk.Label(root, text="Rasel Mridha", font="Arial 18 bold", fg="black", bg="#00A2AE")
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
    ("e", "%", "×", "deg")  # Added the degree button here
]

# Button Styling
btn_color = "#333"
text_color = "white"

# Create main buttons using a loop
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        if btn_text:  # Avoid empty button space
            btn = tk.Button(root, text=btn_text, font="Arial 14 bold", bg=btn_color, fg=text_color,
                            padx=15, pady=15, relief="raised", bd=3,
                            command=lambda text=btn_text: on_click(text))
            btn.grid(row=i + 2, column=j, sticky="nsew", padx=5, pady=5)

# 🔹 Adding the Cross Button for Backspace
cross_btn = tk.Button(root, text="×", font="Arial 14 bold", bg="#FF8C00", fg="white", padx=15, pady=15, relief="raised", bd=3,
                      command=lambda: on_click("×"))
cross_btn.grid(row=7, column=2, sticky="nsew", padx=5, pady=5)

# 🔹 Make "=" and "+" Buttons the Same Size (Place them in the same row)
equal_btn = tk.Button(root, text="=", font="Arial 12 bold", bg="#FF8C00", fg="white",
                      padx=15, pady=15, relief="raised", bd=3, command=lambda: on_click("="))
equal_btn.grid(row=7, column=3, columnspan=2, sticky="nsew", padx=5, pady=5)

plus_btn = tk.Button(root, text="+", font="Arial 14 bold", bg=btn_color, fg=text_color,
                     padx=15, pady=15, relief="raised", bd=3, command=lambda: on_click("+"))
plus_btn.grid(row=7, column=1, columnspan=2, sticky="nsew", padx=5, pady=5)

# 🔹 Bind Enter Key to "=" Button
root.bind('<Return>', lambda event: on_click("="))

# Start the main event loop
root.mainloop()
