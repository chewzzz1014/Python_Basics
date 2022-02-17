#introductory operations of selection statements part 3
#contains 2 simple task involving selection, repetition and list

#Task 1
usernames=[]
numUsers=int(input("How many users? "))
for i in range(numUsers):
    user=input("Enter user name: ")
    usernames.append(user.strip())

for user in usernames:
    if user=="admin":
      print("Hello admin, would you like to see a status report?")
    else:
      print("Hello "+user+", thank you for logging in again.")

print("*******************************************************")


newUsers=["Lynn","asd","dvgdf"]
print("We have 3 new users! Check their username.\n")
for newUser in newUsers:
    if newUser in usernames:
        print("Dear",newUser,", this username has been used.")
    else:
        print("Dear",newUser,", this username is available.")

print("*******************************************************")


#Task 2
num=[]
for i in range(1,10):
    num.append(i)
for th in num:
    if th==1:
        print(str(th)+"st")
    elif th==2:
        print(str(th)+"nd")
    else:
        print(str(th)+'th')

