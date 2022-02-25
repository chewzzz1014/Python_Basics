#introductory operation on files part 3
#different argument of open()

#write only
#since text.txt doesn't not exist on my directory, new file will be created
print("\t1. Write only\n")
with open("text.txt","w") as file_obj:
    file_obj.write("Wowwwwwwww!\nI created this file using Python code\nIt's so fun isn't?")


print("\n*******************************")


#read only
print("\t2. Read only\n")
with open("text.txt","r") as file_obj:
    print(file_obj.read())

print("\n*******************************")

print("\t3. Append only\n")

#appending to the end of file
with open("text.txt","a") as file_obj:
    file_obj.write("\nAppended :)")

with open("text.txt","r") as file_obj:
    print(file_obj.read())

print("\n*******************************")

print("\t4. Write and read\n")
#read and write
with open("text.txt","r+") as file_obj:
    file_obj.write("hmmmm something different here :(\n") #overwrite
    print(file_obj.read())