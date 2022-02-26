#nested dictionary



varsAlien={"name": {"zaid","qin","avatar"},"color": {"Red", "BLUE", "ivory" },"points":{34,12,0} }

print("Beware of aliens!\n")

for alien in range(len(varsAlien["name"])):
    print(varsAlien[0].title()+": "+varsAlien[0][alien].title()+"\n"+
          varsAlien[1].title()+": "+varsAlien[1][alien].title()+"\n"+
          varsAlien[2].title()+": "+str(varsAlien[2][alien])+"\n")

print("Are there any more aliens you found? Enter 0 if not relevant.")
confirm=input("")
getAliensProperties=[]

if confirm!="0":
    num=int(input("Enter number of monsters: "))
    for newAliens in range(num):
        getName=input("Enter name:")
        getAliensProperties[0]=getName.title()
        getColor=input("Enter color: ")
        getAliensProperties[1]=getColor.title()
        getPoints=int(input("Enter points: "))
        getAliensProperties[2]=getPoints
        print("")
        varsAlien.extend(getAliensProperties)

print("Updated aliens list.\n")

for alien in sorted(varsAlien[0]):
    print(varsAlien[0].title() + ": " + varsAlien[0].title() + "\n" +
          varsAlien[1].title() + ": " + varsAlien[1].title() + "\n" +
          varsAlien[2].title() + ": " + str(varsAlien[2]) + "\n")


