#store data into json file


import json

userName = input("Enter username: ")
preference = input("Enter you preference:")

abtUser = [userName, preference]

with open("user.json","w") as file_obj:
    json.dump(abtUser, file_obj)

print("See you next time!")