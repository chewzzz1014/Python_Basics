# get user's favourite number and store it in json file

import json

filename = "favNum.json"

def store_data():
    with open(filename, 'w') as file_obj:
        num = int(input("Enter your favourite number: "))
        json.dump(num, file_obj)


def get_data():
    with open(filename) as file_obj:
        print("We know your favorite number! It's", json.load(file_obj))


try:
     get_data()
except FileNotFoundError:
    store_data()



