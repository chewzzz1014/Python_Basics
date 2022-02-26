#introductory operations of selection statements part 1
#contains 3 simple tasks

#Task 1
alien_color=input("Enter the alien's color: ")
alien_color=alien_color.title()
if alien_color=="Green":
    print("Earned 5 points!")
elif alien_color=="Yellow":
    print("Earned 10 points!")
elif alien_color=="Red":
    print("Earned 15 points!")
print("*******************************************************")

#Task 2
age=int(input("\nEnter you age: "))
if age<2:
    print("You are baby.")
elif age<4:
    print("You are toddler.")
elif age<13:
    print("You are kid.")
elif age<20:
    print("You are teenager.")
elif age<65:
    print("You are adult.")
else:
    print("You are elder.")
print("*******************************************************")
print("\n")

#Task 3
fruits=["Mango","Banana","Strawberry"]
if "Mango" in fruits:
    print("You really like mango!")
if "Banana" in fruits:
    print("You really like banana!")
if "Strawberry" in  fruits:
    print("You really like strawberry!")
if "Apple" in fruits:
    print("You really like apple!")
if "Orange" in fruits:
    print("You really like orange!")
print("*******************************************************")