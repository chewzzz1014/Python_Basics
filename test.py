import os

path = "../Downloads/hyperskill-dataset-67978314.txt"


with open(path) as f:
    lines = f.readlines()

count = 0
for l in lines:
    if l =="summer\n":
        count+=1

print(count)