#introductory operations of functions part 1


#Purpose: get name of 5 users and greet the user


#functions
def get_name(i):
    name=input("Enter name "+str(i+1)+": ")
    return name

def greet_user (name):
    print(name,", Welcome!")

def determineToCont(option):
    if option in "YES" or option in "yes":
        return True
    else:
        return False

#alternative 1: get name and greet the user straight away

def alternative1():
    for count in range(5):
        name=get_name(count).title()
        greet_user(name)
        print("")

#alternative 2: store all names and greet them one-off

def alternative2 ():
    names=[]
    for count in range(5):
        name=get_name(count).title()
        names.append(name)
    print()
    for user in names:
        greet_user(user)


#function call

toCont = True

while toCont:
    option = int(input("Alternative 1 or 2? "))

    if option==1:
        print("*******************************************************")
        print("Alternative 1:")
        alternative1()

    elif option==2:
        print("*******************************************************")
        print("Alternative 2:")
        alternative2()

    else:
        print("Invalid Input")

    toCont= determineToCont(input("Do you wish to continue? (y/n)"))

