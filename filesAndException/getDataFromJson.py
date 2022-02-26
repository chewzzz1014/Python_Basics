#get back data from json file

import json

print("Hi nice to meet you!")

try:
    with open("user.json") as file_obj:
        data = json.load(file_obj)

except FileNotFoundError:
    print("We lost the data :(")
    userName = input("Enter username: ")
    preference = input("Enter you preference:")

    data = [userName, preference]

    with open("user.json", "w") as file_obj:
        json.dump(abtUser, file_obj)

else:
    print("Hi",data[0],"we are finding movies that met you preference as stated below:\n",data[1])
    print("Thank you!")