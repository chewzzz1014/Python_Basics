#nested dictionary
#dictionary in dictionary. Determine full name based on asian (last+first) or non-asian (first+last)
# this doesn't apply to all asian countries

users={"aeinstein":{"first":"albert" ,"last":"einstein", "location":"princeton","isAsian":"no"},
      "mcurie": {"first":"marie", "last":"curie", "location":"paris","isAsian":"no"}}

def printUser(users):
    for user in sorted(users):
      print("Username: "+user)
      print("First Name: "+(users[user]["first"]).title())
      print("Last Name: "+(users[user]["last"]).title())
      print("Location: "+(users[user]["location"]).title())
      print("")

def printUserWithFullName(users):
        for user in sorted(users):
            print("Username: " + user)
            print("First Name: " + (users[user]["first"]).title())
            print("Last Name: " + (users[user]["last"]).title())
            print("Location: " + (users[user]["location"]).title())
            print("Full Name: " + getFullName(user, users))
            print("")

def determineIsAsian(getIsAsian):
    if getIsAsian in "no".casefold():
        return False
    else:
        return True


def getUser(users,numUsers):
    for count in range(0,numUsers):
        getUsername=input("Username: ")
        getFirstName=input("First Name: ")
        getLastName=input("Last Name: ")
        getLocation=input("Location: ")
        getIsAsian=input("Are you Asian (Yes/No)?")
        isAsian=determineIsAsian(getIsAsian)
        users[getUsername]={"first":getFirstName.strip(),"last":getLastName.strip(),"location":getLocation.strip(),"isAsian":isAsian}
        print("")


def getFullName(user,users):
    if users[user]["isAsian"]==True :
        users[user]["full name"]=users[user]["last"].title()+" "+users[user]["first"].title()
    else:
        users[user]["full name"]=users[user]["first"].title()+" "+users[user]["last"].title()
    return users[user]["full name"]


print("Current User List: ")
print("")

printUser(users)

getRespond=input("Press 1 to add user.")

if getRespond=="1":
        numUsers=int(input("Enter number of user: "))
        print("\n")
        getUser(users,numUsers)


print("List Updating...\n")
printUserWithFullName(users)
