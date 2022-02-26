#nested dictionary
#extended version of nestedDictionaries2
#will calculate age based on birth year

from nestedDictionaries2 import determineIsAsian

users={"chewzzz1014":{"user_info":{"first":"zi qing","last":"chew","birthYear":2002}},
       "wen_1212":{"user_info":{"first":"wen jing","last":"lim","birthYear":1999}}}

def askMoreUsers(users):
    numUsers=int(input("How many users are there? "))
    for count in range(numUsers):
        getUserName=input("Enter user name: ")
        getFirstName=input("Enter first name: ")
        getLastName=input("Enter last name: ")
        getBirthYear=int(input("Enter birth year: "))
        getIsAsian=input("Asian? (yes/no): ")
        getFullName=knowFullName(determineIsAsian(getIsAsian),getFirstName,getLastName)
        users[getUserName]={"user_info":{"first":getFirstName,"last":getLastName,"birthYear":getBirthYear,"full name":getFullName.title()}}
        print("")

def calcAge(users,currYear):
    for people in users:
        age=currYear-users[people]["user_info"]["birthYear"]
        users[people]["user_info"]["age"]=age

def askCurrYear():
    currYear=int(input("Enter current year: "))
    return currYear

def wantToCont ():
    respond=input("Do you wish to continue? ")
    if (respond.casefold().find("no".casefold()[:])!=-1) or (respond.casefold().find("don't".casefold()[:])!=-1) or (respond.casefold().find("false".casefold()[:])!=-1) or (respond.casefold().find("not".casefold()[:])!=-1):
        return False
    else:
        return True

def printUsersWithAgeandFullname(users):
    for user in sorted(users):
        print("Username: ",user)
        print("First Name: ",users[user]["user_info"]["first"].title())
        print("Last Name: ", users[user]["user_info"]["last"].title())
        print("Birth Year: ", users[user]["user_info"]["birthYear"])
        print("Age: ", users[user]["user_info"]["age"])
        print("Full Name: ",users[user]["user_info"]["full name"])
        print("")

def printUsers(users):
     for user in sorted(users):
        print("Username: ", user)
        print("First Name: ", users[user]["user_info"]["first"].title())
        print("Last Name: ", users[user]["user_info"]["last"].title())
        print("Birth Year: ", users[user]["user_info"]["birthYear"])
        print("")

def knowFullName(isAsian,getFirstName,getLastName):
    if isAsian:
        fullName= getLastName+" "+getFirstName
    else:
        fullName=getFirstName+" "+getLastName
    return fullName

keepLoop=False
printUsers(users)
askMoreUsers(users)
calcAge(users,askCurrYear())
print("")
printUsersWithAgeandFullname(users)
keepLoop=wantToCont()

while keepLoop==True:
    askMoreUsers(users)
    calcAge(users, askCurrYear())
    printUsersWithAgeandFullname(users)
    print("")
    keepLoop = wantToCont()


