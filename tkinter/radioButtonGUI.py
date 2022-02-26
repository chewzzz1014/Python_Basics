#tkinter
#create radio button that gives appropriate output when prompted (choose option 1/option 2)

from tkinter import *
from PIL import ImageTk, Image

root=Tk()
r= IntVar()
r.set("0")
MODES=[("Pepperoni","Pepperoni"),("Cheese","Cheese"),("Mushroom","Mushroom"),("Onion","Onion")]
pizza=StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def click(value):
    myLabel=Label(root, text=value)
    myLabel.pack()

Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda:click(1)).pack()
Radiobutton(root, text="Option 2", variable=r, value=2,command=lambda:click(2)).pack()
myLabel=Label(root, text=pizza.get())
myLabel.pack()

root.mainloop()