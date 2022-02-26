#introductory practices of OOP in Python part 3
#modified based on nestedDictionaries2

import sys

class User():

    '''
    self.username
    self.first_name
    self.last_name
    self.location
    self.isAsian
    self.birthYear
    self.birthMonth
    self.birthDay
    self.age
    self.birthday
    self.full_name
    self.matricNum
    '''

    def askInput(self,question):
        str = input("Enter "+question+": ")
        if str == "q" or str == "Q":
            sys.exit()
        return str.strip()

    def checkEmailValidity (self, email):
        if "@"  in email and "."  in email:
            return email
        else:
            self.incorrectEmail()

    def incorrectEmail(self):
        print("Invalid email. Kindly reenter all your data :(")
        sys.exit()

    def calcAge(self):
        if self.birthYear<=2022:
            return 2022-self.birthYear
        else:
            return "NULL"

    def determineIsAsian(self, isAsian):
        if isAsian in "no".casefold():
            return False
        else:
            return True

    def getFullName(self):
        if self.isAsian:
            self.full_name = self.last_name + " " + self.first_name
        else:
            self.full_name = self.first_name + " " + self.last_name

    def updateBirthMonth(self):
        month = ["January", "February", "March", "April", "May", "June"
                 "July", "August", "September", "October", "November","December"]
        if self.birthMonth<=12 and self.birthMonth>=1:
            return month[self.birthMonth - 1].upper()
        else:
            return "NULL"


    def formattingBirthday(self):
        return str(self.birthYear) + "-" + self.updateBirthMonth() + "-"+ str(self.birthDay)


    def determineInMsia(self):
        states = ["kl", "kuala lumpur", "terangganu", "selangor", "melaka", "pp", "penang", "pulau pinang",
                  "kedah", "perak", "johor", "pahang","kelantan", "sabah", "sarawak","putrajaya", "labuan"]

        if  self.location.lower() not in states:
            print("\nOpps this service is currently unavailabe as you are not in Malaysia :(")

        else:
            print("\nYess we got you :). Kindly take note on your email inbox yaa")

    def printBioData (self):
        print("\nFull Name:",self.full_name)
        print("Age (valid on 2022):",str(self.age))
        print("Birthday:", self.birthday)
        print("Matric Number:",self.matricNum)
        print("Email:",self.email)
        print()


    def __init__(self):

        self.username = self.askInput("Username")
        self.first_name = self.askInput("First Name").title()
        self.last_name = self.askInput("Last Name").title()
        self.matricNum = int(self.askInput("Matric Number"))
        self.email = self.checkEmailValidity ( self.askInput("Email") )
        self.location = self.askInput("Location (State)").title()
        self.isAsian = self.determineIsAsian( self.askInput("Is Asian (y/n)?") )
        self.birthYear = int(self.askInput("Birth Year"))
        self.birthMonth = int(self.askInput("Birth Month (1-12 inclusively)"))
        self.birthDay = int(self.askInput("Birth Day (1-31 inclusively)"))
        self.age = self.calcAge()
        self.birthday = self.formattingBirthday()
        self.getFullName()
        self.determineInMsia()




print("************************************************")
print("Enter 'q' or 'Q' at any time to quit.")

while (True):
    print("************************************************")
    person = User()
    person.printBioData()











