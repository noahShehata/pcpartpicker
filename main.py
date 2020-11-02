from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Noah's World")
root.geometry("500x500")

noahsList1 = ["Menu"]
noahsList2 = ["land", "water", "earth"]




dropBox = ttk.Spinbox(root, wrap = True)
dropBox.pack()

dropBox["values"] = noahsList2
root.mainloop()