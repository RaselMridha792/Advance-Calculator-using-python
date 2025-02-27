import tkinter as tk
import math

# Variable to track if the mode is degree or radian
is_degrees = True
calculated = False  # Flag to track whether the calculation is done
last_result = None  # Variable to store the last result

# Function to handle button clicks
def on_click(text):
    global is_degrees, calculated, last_result
    current_text = entry_var.get()

    if text == "=":
        if not current_text:  # If the input is empty, return 0.
            entry_var.set("0.")
        else:
            try:
                # Replace '^' with '**' for exponentiation and eval the expression
                result = eval(current_text.replace("^", "**"))
                entry_var.set(result)
                last_result = result  # Save the result
                calculated = True  # Mark that calculation is done
            except Exception:
                entry_var.set("Error")
                last_result = None
                calculated = True  # Mark that calculation is done
    elif text == "C":
        entry_var.set("")
        calculated = False  # Reset the flag
    elif text == "×":  # Backspace Functionality
        entry_var.set(current_text[:-1])
        calculated = False  # Reset the flag
    elif text == "√":
        try:
            result = math.sqrt(float(current_text))
            entry_var.set(result)
            last_result = result  # Save the result
            calculated = True
        except ValueError:
            entry_var.set("Error")
            last_result = None
            calculated = True
    elif text == "π":  # Insert Pi Value
        entry_var.set(current_text + str(math.pi))
        calculated = False  # Reset the flag
    elif text == "e":  # Insert Euler's Number
        entry_var.set(current_text + str(math.e))
        calculated = False  # Reset the flag
    elif text == "ln":  # Natural Logarithm
        try:
            result = math.log(float(current_text))
            entry_var.set(result)
            last_result = result  # Save the result
            calculated = True
        except ValueError:
            entry_var.set("Error")
            last_result = None
            calculated = True
    elif text == "log":  # Log Base 10
        try:
            result = math.log10(float(current_text))
            entry_var.set(result)
            last_result = result  # Save the result
            calculated = True
        except ValueError:
            entry_var.set("Error")
            last_result = None
            calculated = True
    elif text == "10^x":  # 10 Power x
        try:
            result = 10 ** float(current_text)
            entry_var.set(result)
            last_result = result  # Save the result
            calculated = True
        except ValueError:
            entry_var.set("Error")
            last_result = None
            calculated = True
    elif text == "1/x":  # Reciprocal
        try:
            result = 1 / float(current_text)
            entry_var.set(result)
            last_result = result  # Save the result
            calculated = True
        except ZeroDivisionError:
            entry_var.set("Error")
            last_result = None
            calculated = True
    elif text == "x!":  # Factorial
        try:
            result = math.factorial(int(current_text))
            entry_var.set(result)
            last_result = result  # Save the result
            calculated = True
        except ValueError:
            entry_var.set("Error")
            last_result = None
            calculated = True
    elif text == "%":  # Percentage Functionality
        try:
            if current_text and current_text[-1].isdigit():  
                entry_var.set(current_text + "%")  # Allow % to be used in expressions
            else:
                result = float(current_text) / 100  # If used alone, calculate percentage
                entry_var.set(result)
                last_result = result  # Save the result
                calculated = True
        except ValueError:
            entry_var.set("Error")
            last_result = None
            calculated = True
    elif text == "sin":
        try:
            if is_degrees:
                # Convert to radians if degrees mode is selected
                current_text = current_text.replace("°", "")
                result = math.sin(math.radians(float(current_text)))
            else:
                result = math.sin(float(current_text))
            entry_var.set(result)
            last_result = result  # Save the result
            calculated = True
        except ValueError:
            entry_var.set("Error")
            last_result = None
            calculated = True
    elif text == "cos":
        try:
            if is_degrees:
                current_text = current_text.replace("°", "")
                result = math.cos(math.radians(float(current_text)))
            else:
                result = math.cos(float(current_text))
            entry_var.set(result)
            last_result = result  # Save the result
            calculated = True
        except ValueError:
            entry_var.set("Error")
            last_result = None
            calculated = True
    elif text == "tan":
        try:
            if is_degrees:
                current_text = current_text.replace("°", "")
                result = math.tan(math.radians(float(current_text)))
            else:
                result = math.tan(float(current_text))
            entry_var.set(result)
            last_result = result  # Save the result
            calculated = True
        except ValueError:
            entry_var.set("Error")
            last_result = None
            calculated = True
    elif text == "^":
        entry_var.set(current_text + "^")
        calculated = False  # Reset the flag
    elif text == "deg":  # Toggle degree/radian mode and insert the degree symbol (°)
        is_degrees = not is_degrees
        entry_var.set(f"Mode: {'Degrees' if is_degrees else 'Radians'}")
        calculated = False  # Reset the flag
    elif text == "Ans":  # Show the last result
        if last_result is not None:
            entry_var.set(last_result)
        calculated = False  # Reset the flag
    else:
        if calculated:  # Reset the entry when a new button is pressed after calculation
            entry_var.set(text)
            calculated = False  # Reset the flag
        else:
            entry_var.set(current_text + text)

# Creating main window
root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg="#34495E")
root.geometry("630x720")

# Adding a header label with a stylish font
title_label = tk.Label(root, text="Scientific Calculator", font="Arial 18 bold", fg="white", bg="#34495E")
title_label.grid(row=0, column=0, columnspan=6, pady=10, padx=(10, 0))  # Added padding to the left of the title

# Input Box with sleek modern style
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font="Arial 30", bg="#2C3E50", fg="white", bd=5, relief="ridge", justify="right")
entry.grid(row=1, column=0, columnspan=6, ipadx=60, ipady=8, pady=20, padx=(10, 0))  # Added left padding to input box

buttons = [
    ("x!", "%", "(", ")", "/", "C"),
    ("10^x", "7", "8", "9", "X", "√"),
    ("1/x", "4", "5","6", "-", "cos" ),  
    ("^", "1", "2", "3", ",", "sin", ), 
    ("ln","0", "00", ".", "π", "tan"), 
    ("e",  "mod", "×", "Ans"),  
]
# Button Styling (Sleek, modern style)
btn_color = "#2C3E50"
btn_hover_color = "#34495E"
text_color = "white"

# Function Buttons Color
func_btn_color = "#06407a"  # Color for functions like sin, cos, log, etc.
operator_btn_color = "#03ab9d"  # Color for operators (+, -, x, /, etc.)
number_btn_color = "#2980B9"  # Color for numbers (0-9)
close_btn_color = "#c20404"

# Create buttons using a loop
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        if btn_text:
            if btn_text in "0123456789":
                color = number_btn_color
            elif btn_text in "+-*/()X":
                color = operator_btn_color
            elif btn_text in "x":
                color = close_btn_color
            else:
                color = func_btn_color

            btn = tk.Button(root, text=btn_text, font="Arial 14 bold", bg=color, fg=text_color,
                            padx=20, pady=20, relief="raised", bd=3,
                            command=lambda text=btn_text: on_click(text))
            btn.grid(row=i + 2, column=j, sticky="nsew", padx=5, pady=5)

# Making "=" and "+" buttons larger
equal_btn = tk.Button(root, text="=", font="Arial 14 bold", bg="#FF8C00", fg="white", padx=20, pady=20, relief="raised", bd=3,
                      command=lambda: on_click("="))
equal_btn.grid(row=7, column=4, columnspan=2, sticky="nsew", padx=5, pady=5)

plus_btn = tk.Button(root, text="+", font="Arial 14 bold", bg=operator_btn_color, fg=text_color, padx=20, pady=20, relief="raised", bd=3,
                     command=lambda: on_click("+"))
plus_btn.grid(row=5, column=4, columnspan=1, sticky="nsew", padx=5, pady=5)

# Bind the Enter key to the "=" button
root.bind('<Return>', lambda event: on_click("="))

# Start the main event loop
root.mainloop()
