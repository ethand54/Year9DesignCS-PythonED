import tkinter as tk

root = tk.Tk()
root.title("Class Organizer")
entry1 = tk.Entry(root)
entry1.pack()
canvas1 = tk.Canvas(root, width = 1920, height = 1080)

canvas1.pack();
root.mainloop()