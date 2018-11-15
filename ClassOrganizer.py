import tkinter as tk

root = tk.Tk()
root.title("Class Organizer")
entry1 = tk.Entry(root)
entry1.pack()
canvas1 = tk.Canvas(root, width =1024, height =576, background = "grey")

canvas1.pack();
root.mainloop()