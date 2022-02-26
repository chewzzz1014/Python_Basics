#exception handling



def askNum():
    num = int(input("Enter a number: "))
    return num

def division(num1, num2):
    try:
        div = num1/num2

    except ZeroDivisionError:
         print("Do not divide by 0.")
    except TypeError:
            print("Invalid Type")
    else:
        print("Result:", div) #execute this when no exception

num1 = askNum()
num2 = askNum()
division(num1,num2)