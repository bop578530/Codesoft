import tkinter as tk

# Function to evaluate the expression and display the result
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error")

# Function to clear the input and result
def clear():
    entry.delete(0, tk.END)
    result_label.config(text="Result:")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create an entry widget for input
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for numbers and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, padx=20, pady=20, command=lambda b=button: entry.insert(tk.END, b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create a label to display the result
result_label = tk.Label(window, text="Result:")
result_label.grid(row=row_val, column=0, columnspan=4)

# Create a Clear button
clear_button = tk.Button(window, text="Clear", padx=20, pady=20, command=clear)
clear_button.grid(row=row_val + 1, column=0, columnspan=4)

window.mainloop()
