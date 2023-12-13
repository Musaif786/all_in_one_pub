import os

try:
    import tkinter as tk

except ModuleNotFoundError:
    os.system("pip install tkinter")

# Create the main application window
root = tk.Tk()
root.title("Tkinter Example")

# Create a label to display text
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Function to change the label text
def change_text():
    label.config(text="Button clicked!")

# Create a button
button = tk.Button(root, text="Click Me", command=change_text)
button.pack()

# Start the Tkinter event loop
root.mainloop()
