from tkinter import *
from tkinter import filedialog

root = Tk()

root.filename=filedialog.askopenfile(initialdir="C:/Users/USER/OneDrive/Pictures", title="Select A File", filetypes=(("png files","*.png")))
myLabel = Label(root, text=root.filename )

root.mainloop()