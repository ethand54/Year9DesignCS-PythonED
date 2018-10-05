#When making radio buttons the dimesions are recorded by rows and columns
#tkinter is a module (tool box) that holds code that you can use
#by using as tk we just are shortening the name
import tkinter as tk
#root is variable that hold the information
#about the main window. That is the window
#with the close, min, man buttons in the top
#left
root = tk.Tk() # tk.TK() go in to the tk tool box and use the function Tk()
#Tk with the capital is different the just tk

#if we want to better position the elements we use 
#the grid geometry manager, not the pack
ent = tk.Entry(root)
ent.grid(row = 0, column = 0)

btn = tk.Button(root, text = "Press Me")
btn.grid(row = 0, column = 1)

label = tk.Label(root, text = "...")
label.grid(row = 1, column = 0, columnspan = 2)

root.mainloop()
#sets up your program in an infinit loop waiting for 
#the user to do something. This is an EVEN DRIVE PROGRAM
#This means a function is called when we "do something"
#For example in Fortnite when you dont touch the controller
#the player doesnt move but once you "do something "
#it does