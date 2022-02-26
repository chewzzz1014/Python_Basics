#count the number of words in a file (from same directory)


try:
    with open("randomText.txt","r") as file_obj:
        contents = file_obj.read()
except FileNotFoundError:
    print("File unavailable. Try to check again?")
else:
    contentsInList = contents.split()
    print("This file has",len(contentsInList),"words.")

