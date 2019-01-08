import tkinter as tk




def change(*args):
	print("running change")
	print(var.get())

def AddToList():
	#label2 = tk.Label(root, text = ent1.get() + "-" + var.get(), foreground="blue")
	#label2.pack()
	f = open("file.txt", "a+")
	f.write(ent1.get() + " - " + ent2.get() + " : " + var.get() + "\n")
	f.close()
	print("file written")

def ClearFile(): 
	f = open("file.txt", "w+")
	f.write("")
	f.close()

root = tk.Tk() #Constructs our main window


OPTIONS = [
	"Strong Understanding",
	"Basic Understanding",
	"Weak Understanding"
]

var = tk.StringVar(root)
var.set(OPTIONS[2])
var.trace("w",change)

dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1],OPTIONS[2])
dropDownMenu.pack()

word1Label = tk.Label(root, text = "Class", foreground = "red")
word1Label.pack()

ent1 = tk.Entry(root)
ent1.pack()

word2Label = tk.Label(root, text = "Topic", foreground = "black")
word2Label.pack()

ent2 = tk.Entry(root)
ent2.pack()




btnGO = tk.Button(root, text = "ENTER", command=AddToList)
btnGO.pack()

clearButton = tk.Button(root, text = "CLEAR FILE", command=ClearFile)
clearButton.pack()


root.mainloop()
