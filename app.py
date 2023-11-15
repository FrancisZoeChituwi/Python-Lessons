import tkinter as tk

def on_click(button_text):
    current_text = entry_var.get()

    if button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_text == "C":
        clear_entry()
    else:
        entry_var.set(current_text + button_text)

def clear_entry():
    entry_var.set("")

def create_button(window, text, row, col, command):
    return tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14), command=command).grid(row=row, column=col)

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry widget to display and edit the current expression
entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, font=('Arial', 18), justify="right")
entry.grid(row=0, column=0, columnspan=6)  # Adjusted columnspan to 6

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    '(', ')', 'sqrt', '**2', '**0.5'  # Added more buttons
]

# Add buttons to the grid
row_val = 1
col_val = 0

for button_text in buttons:
    create_button(window, button_text, row_val, col_val, lambda btn=button_text: on_click(btn))
    col_val += 1
    if col_val > 5:  # Adjusted the condition for a new row
        col_val = 0
        row_val += 1

# Create a Clear button
create_button(window, "C", row_val, col_val, clear_entry)

# Run the Tkinter event loop
window.mainloop()
