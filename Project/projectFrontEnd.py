import tkinter as tk 



root = tk.Tk()

titleLabel = tk.Label(root, text = "Class Organizer", font=("Helvetica", 20))

titleLabel.pack()


titleLabel.grid(row = 0, column = 0, columnspan = 2)

output = tk.Text(root, height = 5, width = 50)
output.config(state = "disable")
output.grid(row = 1, column = 0, columnspan = 4)

word1Label = tk.Label(root, text = "Class-Topic-Understading", foreground = "blue")
word1Label.grid(row = 1, column = 0)

ent1 = tk.Entry(root)
ent1.grid(row = 1, column = 1)


btnGO = tk.Button(root, text = "ENTER")
btnGO.grid(row = 30,column = 0)\

master = tk.Tk()

w = tk.Canvas(master, width=200, height=100)
w.pack()


w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")

#	print("running change")
#	print(var.get())


#OPTIONS = [
#	"Sort",
#	"Alphebetical",
#	"Understanding",
#]

#var.set(OPTIONS[0])
#var.trace("w",change)

#dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1],OPTIONS[2])
#dropDownMenu.pack()
#dropDownMenu.grid(row = 3, column = 1)


root.mainloop()