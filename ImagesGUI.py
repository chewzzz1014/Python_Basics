#create a photo displayer contains back, forward, exit buttons and index of photo


from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Cat Viewer")

#root.iconbitmap("C:/Users/USER/Downloads/images.png")
'''
button_quit=Button(root,text="Exit",command=root.quit)
button_quit.pack()
'''
my_img1=ImageTk.PhotoImage(Image.open("C:/Users/USER/OneDrive/Pictures/cat.jpg"))
my_img2=ImageTk.PhotoImage(Image.open("C:/Users/USER/OneDrive/Pictures/cat2.jpg"))
my_img3=  ImageTk.PhotoImage(Image.open("C:/Users/USER/OneDrive/Pictures/cat3 (2).jpg"))
image_list = [my_img1, my_img2, my_img3]
image_number=1

status = Label(root,text="Image "+str(image_number)+" of  "+str(len(image_list)), bd=1, relief=SUNKEN,anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)


my_label=Label(image=my_img1)
my_label.grid(row=0, column=0,columnspan=3)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forward=Button(root,text=">>",padx=20,pady=10,borderwidth=5,command=lambda:forward(image_number+1))
    button_back=Button(root,text="<<",padx=20,pady=10,borderwidth=5,command=lambda:back(image_number-1))

    if image_number==1:
        button_back=Button(root,text="<<",padx=20,pady=10,borderwidth=5,state=DISABLED)
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1, column=2)
    status = Label(root, text="Image " + str(image_number) + " of  " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forward=Button(root,text=">>",padx=20,pady=10,borderwidth=5,command=lambda:forward(image_number+1))
    button_back=Button(root,text="<<",padx=20,pady=10,borderwidth=5,command=lambda:back(image_number-1))

    if image_number==3:
        button_forward=Button(root,text=">>",padx=20,pady=10,borderwidth=5,state=DISABLED)
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1, column=2)
    status = Label(root,text="Image "+str(image_number)+" of  "+str(len(image_list)), bd=1, relief=SUNKEN,anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

button_back=Button(root,text="<<",padx=20,pady=10,borderwidth=5,state=DISABLED)
button_exit=Button(root,text="EXIT",command=root.quit,padx=80,pady=10,borderwidth=5)
button_forward=Button(root,text=">>",padx=20,pady=10,borderwidth=5,command=lambda:forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)
#status.grid(row=2,column=0,columnspan=3, sticky=W+E)

root.mainloop()