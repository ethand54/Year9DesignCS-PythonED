import tkinter as tk

def change(*args):
	print("running change")
	print(var.get())

root = tk.Tk() #Constructs our main window

#List of strings 
#My list is called options there are 3 elements with index 0 to 2
#print(OPTIONS[2])
OPTIONS = [
	"Understand",
	"OK",
	"Help"
]

var = tk.StringVar(root)
var.set(OPTIONS[0])
var.trace("w",change)

dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1],OPTIONS[2])
dropDownMenu.pack()

word1Label = tk.Label(root, text = "Class-Topic", foreground = "blue")
word1Label.pack()


ent1 = tk.Entry(root)
ent1.pack()


btnGO = tk.Button(root, text = "ENTER")
btnGO.pack()



root = tk.Tk()





root.mainloop()
print("End program")