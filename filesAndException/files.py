#introductory operation on files part 1

#open files and print the contents from randomText.txt in same directory


#print whole contents
with open ("randomText.txt") as file_object:
    contents = file_object.read()
    print(contents)

print("*************************************")



#store line into a list and print selected number of lines only
#open again as it closed automtically right after last use

with open ("randomText.txt") as file_object:
    lines = file_object.readlines()
    print("Printing line 1 to line 32...")
    print(lines[:33])


#store line into a list and print selected number of lines only
#since list "lines" will contain line feed, this time we trim the string before store in string to print

with open ("randomText.txt") as file_object:
    clearLines=[]
    for line in lines:
      if "\n" in line and line!="\n":
            clearLines.append( line[:-2] )

    print("Printing line 1 to line 32...")
    print(clearLines[:33])
