import tkinter as tk 



root = tk.Tk()

titleLabel = tk.Label(root, text = "Class Organizer", font=("Helvetica", 20))

titleLabel.pack()


titleLabel.grid(row = 0, column = 0, columnspan = 2)

output = tk.Text(root, height = 15, width = 50)
output.config(state = "disable")
output.grid(row = 1, column = 0, columnspan = 2)

word1Label = tk.Label(root, text = "Class-Topic-Understading", background = "red", foreground = "blue")
word1Label.grid(row = 1, column = 0)

ent1 = tk.Entry(root)
ent1.grid(row = 1, column = 1)


btnGO = tk.Button(root, text = "ENTER")
btnGO.grid(row = 30,column = 0)\


root.mainloop()