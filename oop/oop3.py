#introductory practices of OOP in Python part 2

class Restaurant():

    def __init__(self,name,day,month,year):
        self.name = name
        self.day = day
        self.month = month
        self.year = year
        self.num_served = 0

    def getDate(self):
        self.established_date = str(self.day)+"-"+str(self.month)+"-"+str(self.year)

    def set_number_served(self, num):
        self.num_served = num

    def increment_number_served(self,plus):
        self.num_served += plus

    def about (self):
        self.getDate()
        print("***************************************************************")
        print("\t\t\t\t\t\t_________")
        print("\t\t\t\t\t\tAbout Us")
        print("\t\t\t\t\t\t_________")
        print("Restaurant:",self.name,"\nYear Established:",self.established_date,
              "\nTotal Number Customer Served:",self.num_served)
        print("\n***************************************************************")

    def printWelcome(self):
        print("Welcome to Restaurant",self.name)
        numCustomer = int(input("How many customers? "))
        self.set_number_served(numCustomer)





my_Res = Restaurant("Confirm Sedap",14,10,2021)
my_Res.printWelcome()
my_Res.about()