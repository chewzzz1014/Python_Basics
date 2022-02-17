#Repetition using while statements
#contains 2 simple Tasks

#Task 1
print("Enter quit at any time to terminate.")
print("Toppings?")
topping=input("")
while not (topping in "quit".casefold()) :
    print(topping," added!\n")
    topping=input("")
print("*******************************************************")



#Task 2

print("Enter negative integer at any time to terminate.")
age=int(input("Enter age: "))
while age>0:
    if age<3:
        fee=0
    elif age<=3 and age<=12:
        fee=10
    else:
        fee=15
    print("Fee is RM ",str(fee),"\n")
    age=int(input("Enter age: "))