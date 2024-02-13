import tkinter as tk
from tkinter import messagebox

def msgBoxFun():
    messagebox.showinfo("OK", text)

def popupFun(data=None):

    # text1 = "Hello world"
    text1 = data if data is not None else "Hello world"
    def show_ok_popup():
        messagebox.showinfo("OK", text1)
        root.after(1000,close_popup)

        #disable the button also
        # button.config(state=tk.DISABLED)


    def close_popup():
        #close the popup
        root.update_idletasks()
        root.destroy()


    # Create the main window
    root = tk.Tk()

    # button to click
    button = tk.Button(root, text="Alert", command=show_ok_popup)
    button.pack(pady=20)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ =="__main__":

    text = "Good Morning!"
    # popupFun(text)