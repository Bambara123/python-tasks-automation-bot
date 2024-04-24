# import m_movement
# import k_typing
# import where_to_click


import tkinter as tk

# Create the main window
window = tk.Tk()

# Create entry fields for name, action, and year
name_entry = tk.Entry(window)
name_entry.pack()

action_entry = tk.Entry(window)
action_entry.pack()

year_entry = tk.Entry(window)
year_entry.pack()

# Define the functions for name, action, and year
def name_fun(name):
    print(f"Name function executed with {name}")

def action_fun(action):
    print(f"Action function executed with {action}")

def year_fun(year):
    print(f"Year function executed with {year}")

# Create a function to execute the script
def execute_script():
    # Get the values from the entry fields
    name = name_entry.get()
    action = action_entry.get()
    year = year_entry.get()

    # Call the relevant functions with these values
    name_fun(name)
    action_fun(action)
    year_fun(year)

# Create a button to execute the script
run_button = tk.Button(window, text ="Run", command = execute_script)
run_button.pack()

# Run the main loop
window.mainloop()