#introductory practices of OOP in Python part 1
#contians 3 classes


#Class 1

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title()+" is sitting.")
    def roll(self):
        print(self.name.title()+" rolled over!")

myDog=Dog("Jacky",3)
your_Dog= Dog("Woofy",4)

print("I have a dog named "+myDog.name.title()+". He is "+str(myDog.age)+" years old.")
myDog.sit()
myDog.roll()

print("\nYou have a dog named "+your_Dog.name.title()+". He is "+str(your_Dog.age)+" years old.")
myDog.sit()
myDog.roll()

print("*******************************************************")



#Class 2
class Restaurant():
    def __init__(self, name, cuisine):
        self.name=name
        self.cuisine=cuisine
    def describe_restaurant(self):
        print("Restaurant "+self.name.title()+" has "+self.cuisine.title()+" cuisines.")
    def open_restaurant(self):
        print("Restaurant "+self.name.title()+" has opened!")

getName=input("Enter name: ")
getType=input("Enter cuisine type: ")

res1=Restaurant("Mac Cik Bawang","malay")
res1.describe_restaurant()
res1.open_restaurant()

print("")
res2=Restaurant(getName,getType)
res2.describe_restaurant()
res2.open_restaurant()

print("*******************************************************")







#Class 3
class User():
    def __init__(self,userName,first,last,country,birthYear,birthMonth,birthDay):
        self.userName=userName
        self.first=first
        self.last=last
        self.country=country
        self.birthYear=birthYear
        self.birthMonth=birthMonth
        self.birthDay=birthDay


    def determineAge(self):
        age=2021-int(self.birthYear)
        return age

    def determineBornMonth(self):
        # update birthMonth (numerical-> literal
        monthsInYear={1:"January",2:"February",3:"March",4:"April",
                      5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
        if int(self.birthMonth<1) or int(self.birthMonth>12):
            self.birthMonth="Invalid"
        else:
            self.birthMonth=monthsInYear[self.birthMonth]

    def printBirthDay(self):
        #found out no need to get return value of determineBornMonth()
        #self.birthMonth=self.determineBornMonth()

        self.determineBornMonth()
        print("Birthday: "+str(self.birthDay) + "-" + self.birthMonth + "-" + str(self.birthYear))

    def describeYourself(self):
        print("Username: "+self.userName)
        print("First Name: "+self.first.title())
        print("Last Name: "+self.last.title())
        print("Country: "+self.country.title())
        self.printBirthDay()
        print("Age: "+str(self.determineAge()))


abtMe=User("chewzzz1014","zi qing","chew","malaysia",2002,10,14)
abtMe.describeYourself()




