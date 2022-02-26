#Python tkinter
#create entry field and print output based on name entered
from tkinter import *

root=Tk()

def myClick():
    myLabel=Label(root,text="Welcome, "+e.get()).pack()

myButton=Button(root,text="Enter",padx=20,pady=10,command=myClick,bg="#f8f0c6")

e=Entry(root,width=50,bg="white",borderwidth=5)

e.pack()
e.get()

e.insert(0,"Your Name")

myButton.pack()

root.mainloop()