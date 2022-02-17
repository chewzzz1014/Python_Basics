#introductory operations of functions part 3
#contain 2 simple tasks


#Task 1: Updating the progress of items. Involves functions, repetition statements and list
def printing(unprinted_designs, printed):
    while unprinted_designs:
        in_progress=unprinted_designs.pop()
        print("We're making "+in_progress+"!")
        printed.append(in_progress)

def result (printed):
    for item in printed:
        print("We have "+item+"!")

unprinted_designs=["iphone case","robot pendant","dodecahedron"]
printed=[]
printing(unprinted_designs,printed)
print("*********************WAITING...************************")
result(printed)
print("*******************************************************")



#Task 1: Modifying and updating the magician list. Involves functions, repetition statements and list
#Adding "Great" in front of the names of every magicians and update the list
#Purpose: To show that magicians[:] as argument to functions that modifying list will never change the contents of original list
def print_magicians (magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians,updated_magicians):
    for idx in range(len(magicians)):
        new_name="Great "+magicians.pop()
        updated_magicians.append(new_name)

magicians=["a","b","c"]
updated_magicians=[]

print("Initial List")
print_magicians(magicians)
#noting the argument magicians[:]
make_great(magicians[:],updated_magicians)
print("\nOriginal List after Modifying")
print_magicians(magicians)
print("\nNew List after Modifying")
print_magicians(updated_magicians)
print("*******************************************************")