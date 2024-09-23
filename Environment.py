import tkinter as tk

# Check if Tkinter is working
root = tk.Tk()
root.title("Tkinter Test Window")
root.geometry("300x200")
label = tk.Label(root, text="Tkinter is installed and working!")
label.pack()

root.mainloop()