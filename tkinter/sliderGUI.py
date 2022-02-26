#Tkinter
#create simple slider (that doesn't look that good)


from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.geometry("400x400")

myImg= ImageTk.PhotoImage(Image.open("C:/Users/USER/OneDrive/Pictures/cat3.jpg"))
myLabel= Label(root, image=myImg )

vertical=Scale(root, from_=0, to=200)
horizontal=Scale(root, from_=0, to=200, orient=HORIZONTAL)

vertical.pack()
horizontal.pack()

my_label=Label(root, text=horizontal.get()).pack()

root.mainloop()