#introductory practices of inputting
#contains 3 tasks that perform different operations based on inputted value
car=input("What kind of rental car you would like? ")
print("Let me see if I can find you a ",car)
print("*******************************************************")


numPpl=int(input("How many people in your dinner group? "))
if numPpl>8:
    print("You would have to wait.")
else:
    print("Your table is ready!")
print("*******************************************************")


num=int(input("Enter a number: "))
if num%10==0:
    print(num," is multiples of 10.")
else:
    print(num," is not  multiple of 10.")
print("*******************************************************")