#tkinter
#create a message box

from tkinter import *
from tkinter import messagebox

root=Tk()
def popup():
    response= messagebox.askyesno("Warning","Do you wish to continue?")
    #Label(root,text=response).pack()
    if response==1:
        Label(root, text="You clicked yes!").pack()
    else:
        Label(root, text="You clicked no :(").pack()

Button(root,text="Press Me",command=popup).pack()

root.mainloop()