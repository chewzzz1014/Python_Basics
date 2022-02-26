#introductory operations of functions part 2
#involve function, default argument of function, selection statements, repetition and usage of list


def determineAge (getAge):
    if not getAge.isdigit() or int(getAge)<0:
        getAge=""
    else:
        getAge=int(getAge)
    return getAge

def determineGender (getGender):
    if  getGender.casefold()=="M".casefold() or getGender.casefold()=="male".casefold():
        getGender="Male"
    elif getGender.casefold()=="F".casefold() or getGender.casefold()=="female".casefold():
        getGender="Female"
    else:
        getGender=""
    return getGender

def determineIsAsian(getIsAsian):
    if getIsAsian=="1":
        return True
    elif getIsAsian=="0":
        return False
    else:
        return ""

def determineFullName(isAsian,getLast,getFirst):
    if  isAsian:
        return getLast+" "+getFirst
    elif isAsian=="":
        return ""
    else:
        return getFirst+" "+getLast


def buildName(first,last,age="",gender="",getFullName=""):
    FIRST.append(first)
    LAST.append(last)
    AGE.append(age)
    GENDER.append(gender)
    FULLNAME.append(getFullName)

def printName(FIRST,LAST,AGE,GENDER,FULLNAME):
    for people in range(count):
        print("People "+str(people+1))
        print("First name: "+FIRST[people])
        print("Last name: "+LAST[people])
        if AGE[people]!="":
            print("Age: "+str(AGE[people]))
        if GENDER[people]!="":
            print("Gender: "+GENDER[people])
        if FULLNAME[people]!="":
            print("Full name: "+FULLNAME[people])
        print("")

def getInfo(count):
    for num in range(count):
         print("Person "+str(num+1))
         getLast=(input("Enter last name: ")).title()
         getFirst=(input("Enter first name: ")).title()
         getAge=input("Enter age (Press \"-\" if not relevant): ")
         age=determineAge(getAge)
         getGender=input("Enter gender (M\F) [Press \"-\" for others]: ")
         gender=determineGender(getGender)
         getIsAsian=input("Are you Asian? (1 for yes and 0 for no): ")
         isAsian=determineIsAsian(getIsAsian)
         getFullName=determineFullName(isAsian,getLast,getFirst)
         buildName(getFirst,getLast,age,gender,getFullName)
         print("")

FIRST=[]
LAST=[]
AGE=[]
GENDER=[]
FULLNAME=[]
count=int(input("Enter number of people: "))
print("")
getInfo(count)
printName(FIRST,LAST,AGE,GENDER,FULLNAME)