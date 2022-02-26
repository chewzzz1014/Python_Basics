#introductory operations of functions part 6
#4 simple task related to functions were included
#Task 2,3,4 will involve default argument


#Task 1: Display skills learnt
print("*******************************************************")
lesson_provided={"language":{"Java","Kotlin"},"skill":{"photoshop","video editing"}}
lesson_went=[]

def display_msg (msg):
    print("I learnt ",msg.title()," today! ")
    print("")

for field in lesson_provided:
    for skill in lesson_provided[field]:
            lesson_went.append(skill)
            display_msg(skill)


#Task 2t
print("*******************************************************")
def print_pet(name,types="dog"): #must put default values at last since it's positional argument
    print("I have a",types," named ",name)

print_pet(name="Charles")



#Task 3:
print("*******************************************************")
def make_shirt(size,text="Moon"):
    print("The t-shirt of size",size,"printed \"",text,"\" is ready to ship!")
size=input("Enter size of t-shirt: ")
text=input("What would you like to print on the t-shirt? ")
make_shirt(size.upper(),text)
make_shirt("ss".upper())


#Task 4
print("*******************************************************")
def describe_city(city,country="Malaysia"):
    print(city+" is in "+country)
describe_city("Kuala Lumpur")
describe_city("Tokyo","Japan")
