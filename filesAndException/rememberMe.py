# For the first time loading the programme, asking for user's username. Else, confirm that the current user is the user the programme recorded

import json

filename = "username.json"

def update_username(username=None):
    if username == None:
         username = input("Enter username: ")

    with open(filename, 'w') as file_obj:
        json.dump(username, file_obj)
    print("Successfully updated!")


def get_username():
    with open(filename) as file_obj:
        username = json.load(file_obj)
    print("Welcome to",username,"'s home.")

def return_username():
    with open(filename) as file_obj:
        username = json.load(file_obj)
    return username

def get_current_user():
    return input("Your username: ")

def cont_current(name):
    prompt = "Continue with "+name+" ? (True/False) "
    decision = input(prompt)
    if decision == "True":
        return True
    else:
        return False


try:
    get_username()
    current_user = get_current_user()
    if current_user == return_username():
        pass
    else:
        if cont_current(current_user):
            update_username(current_user)
        else:
            update_username()

except FileNotFoundError:
    update_username()





