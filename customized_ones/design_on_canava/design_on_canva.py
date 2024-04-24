import tkinter as tk

# Create the main window
window = tk.Tk()

# Create an entry field for the user input
input_entry = tk.Entry(window)
input_entry.pack()

# Create an entry field for the function name
function_entry = tk.Entry(window)
function_entry.pack()

# Create an entry field for the coordinates
coordinates_entry = tk.Entry(window)
coordinates_entry.pack()

# Create a checkbox for the click option
click_var = tk.BooleanVar()
click_checkbox = tk.Checkbutton(window, text="Click", variable=click_var)
click_checkbox.pack()

# Create a function to print the user input
def print_input():
    user_input = input_entry.get()
    function_name = function_entry.get()
    coordinates = coordinates_entry.get()
    click_option = click_var.get()
    print(user_input, function_name, coordinates, click_option)

# Create a button to print the user input
print_button = tk.Button(window, text="Print", command=print_input)
print_button.pack()

# Run the main loop
window.mainloop()