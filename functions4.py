#introductory operations of functions part 4
#contains 3 simple tasks

import sys

#Task 1: Explore arbitary arguments of function
def build_userProfile(first,last,**user_info):
    profile={}
    profile["first"]=first
    profile["last"]=last
    for item in user_info:
        profile[item]=user_info[item]
    return profile

user_profile=build_userProfile("zi qing","chew",location="kuala lumpur",university="UPM")
print(user_profile)
print("*******************************************************")

#Task 2: Explore arbitary arguments of function (1)
def making_sandwiches(orderNum,*sandwiches):
    print("\n\tMaking...")
    print("Order Number: "+str(orderNum))
    for sandwich in sandwiches:
        print(sandwich.title())

making_sandwiches(123456,"cheesy","bbq")
making_sandwiches(468534,"smoked bacon")
making_sandwiches(548948,"tuna","pork","beef","original")
print("*******************************************************")


#Task 3: Biodata of one user only with unspecified keys
#Involves function, disctionary, repetition statements and selection statements
def testIt(fromUser):
    if fromUser in "Qq":
        sys.exit()


def print_profile(profile):
    #print("First Name: "+first+"\nLast Name: "+last)
    print("")
    if len(profile)!=0:
        for item in profile:
            if profile[item].isdigit():
                print( item.title()+": "+ str(profile[item]) )
            else:
                print( item.title() + ": " + profile[item].title() )

def determine_addMore(fromUser):
    if fromUser.casefold()=="no".casefold() or fromUser.casefold()=="n".casefold() or fromUser.casefold()=="q".casefold() or fromUser=="-":
        return False
    else:
        return True

def ask_profile():
    toCont=True
    getExtra={}

    getUserName = input("Username: ").strip()
    testIt(getUserName)
    getExtra["username"] = getUserName

    getFirstName=input("First Name: ").strip()
    testIt(getFirstName)
    getExtra["first name"]=getFirstName

    getLastName=input("Last Name: ").strip()
    testIt(getLastName)
    getExtra["last name"] = getLastName

    getToAdd=input("\nAnything to add(Y/N)? ")
    testIt(getToAdd)
    addMore=determine_addMore(getToAdd)

    if addMore:
        while toCont:
            getKey=input("Enter Key: ").strip()
            testIt(getKey)

            getValue=input("Enter Value: ").strip()
            testIt(getValue)

            getExtra[getKey]=getValue

            getToCont=input("\nEnter more info (Y/N)? ")
            testIt(getToCont)
            toCont=determine_addMore(getToCont)

    return getExtra

print("Enter \"Q\" or \"q\" to terminate the program at anytime.")
profile=ask_profile()
print_profile(profile)
