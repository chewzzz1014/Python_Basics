#introductory operation on files

#open files and print the contents from randomText.txt in same directory

#replace "n" and "N" with "!" and "?" respectively

with open("randomText.txt") as file_object:
    contents = file_object.read()

contents = contents.replace("n","!")
contents = contents.replace("N","?")

print("Modified Text....\n\n\n")
print(contents)