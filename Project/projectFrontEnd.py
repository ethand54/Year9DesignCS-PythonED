import tkinter as tk 



root = tk.Tk()

titleLabel = tk.Label(root, text = "Class Organizer", font=("Helvetica", 20))

titleLabel.pack()


titleLabel.grid(row = 0, column = 0, columnspan = 2)

output = tk.Text(root, height = 5, width = 50)
output.config(state = "disable")
output.grid(row = 1, column = 0, columnspan = 4)

word1Label = tk.Label(root, text = "Class-Topic", foreground = "blue")
word1Label.pack

ent1 = tk.Entry(root)
ent1.pack()

btnGO = tk.Button(root, text = "ENTER")
btnGO.grid(row = 30,column = 0)\



root.mainloop()