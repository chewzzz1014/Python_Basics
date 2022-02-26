#tkinter
#open second window when prompted

from tkinter import *
from PIL import ImageTk,Image
root=Tk()


def open():
    global my_img
    top = Toplevel()
    top.title("Top")
    my_img = ImageTk.PhotoImage(Image.open("C:/Users/USER/OneDrive/Pictures/cat.jpg"))
    Label(top, image=my_img).pack()
    bt2=Button(top, text="Close", command=top.destroy).pack()


root.title("Root")
btn= Button(root, text="Click to open second window.",command=open).pack()


mainloop()