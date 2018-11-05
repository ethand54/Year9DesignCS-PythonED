import tkinter as tk

root = tk.Tk()
root.title("GuiPracticeCanvas.py")
root.maxsize(10000,10000)
root.minsize(1,1)
canvas1 = tk.Canvas(root, width = 1920, height = 1080, background = "rainbow")

canvas1.pack();



root.mainloop()