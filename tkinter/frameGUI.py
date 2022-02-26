from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Learning Tkinter")
#icon of the windows. Should be .ico format
root.iconbitmap("C:/Users/USER/OneDrive/Pictures/Layer 1.png")

#create frame
frame=LabelFrame(root, text="This is a frame.", padx=10, pady=10 )
frame.pack(padx=100, pady=100 )

#put 2 buttons inside the frame created
b=Button(frame, text="Click Here",padx=10, pady=10)
b.grid(row=0,column=0)
b1=Button(frame, text="Hello!",padx=10, pady=10)
b1.grid(row=1, column=1)

root.mainloop()