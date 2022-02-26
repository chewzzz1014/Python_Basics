#introductory practices of OOP in Python part 2

class Student:
    def __init__(self,name,major,gpa):
        self.name=name
        self.major=major
        self.gpa=gpa

    def on_honor_roll(self):
        if self.gpa>=3.50:
            return True
        else:
            return False

    def congrats (self,result):
        if result==True:
            print("Congrats",myself.name.title(),", you did it!")
        else:
            print("It's ok, try harder next time.")

myself  = Student("chew","CS",3.5)
print("On honor roll?\n",myself.congrats(myself.on_honor_roll))