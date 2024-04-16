# import m_movement
# import k_typing
# import where_to_click


import tkinter as tk
from tkinter import filedialog

# Function to open a file dialog and return the selected file's path
def browse_files():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Image files", "*.jpg *.png"), ("all files", "*.*")))
    return filename

# Function to execute the script
def execute_script():
    # Here you can add the code to execute your script
    pass

# Create the main window
window = tk.Tk()

# Create a button to browse for files
browse_button = tk.Button(window, text ="Browse", command = browse_files)
browse_button.pack()

# Create an entry field for the variable
variable_entry = tk.Entry(window)
variable_entry.pack()

# Create a button to execute the script
run_button = tk.Button(window, text ="Run", command = execute_script)
run_button.pack()

# Run the main loop
window.mainloop()