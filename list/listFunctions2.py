#perform introductory operations on list part 2
#updating and modifying values of list
#involves len(), insert(), append(), pop(), del

guest=["Li","Min","Zeke","Rev"]


i=0
while i<len(guest):
    print("Dear "+guest[i]+" , you are invited to the dinner.")
    i+=1

#updating guest[2]
print("\n"+guest[2]+" can't come to the dinner.\n")
guest[2]="Wen"

#check updated list
i=0
while i<len(guest):
    print("Dear "+guest[i]+" , you are invited to the dinner.")
    i+=1


print("*******************************************************")

print("\nA bigger table was found!\n")

#insert at index 0
guest.insert(0,"Ivan")
middle=int(len(guest)/2)

#insert at middle of list
guest.insert(middle,"Qing")

#insert at end of list
guest.append("Ponny")

#check updated list
i=0
while i<len(guest):
    print("Dear "+guest[i]+" , you are invited to the dinner.")
    i+=1
print("\n\nSo sorry, we could only invite 2 guest for the dinner.\n")

#pop the list until only 2 guest left
while len(guest)>2:
    popped=guest.pop()
    print(popped+", so sorry to let you know that we can't invite you to the dinner.")

print(guest[0]+", you are invited.")
print(guest[1]+", you are invited.")


#Delete guests
del guest[0]
del guest[0]

print("\n\nRemanding guest: ")
print(guest)