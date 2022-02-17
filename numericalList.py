#perform introductory operations on list
#Includes append(), min(), max(), sum()


#looping through number in ascending order
for num in range(1,21):
    print(num)
print("*******************************************************")


#add number to end of list
numbers=[]
for num in range(1,10):
    numbers.append(num)

#min(), max(), sum()
print("Min:",min(numbers))
print("Max",max(numbers))
print("Sum",sum(numbers))
print("*******************************************************")

#even numbers from 1 to 20 (exclusive)
print("Even numbers from 1 to 20 (exclusive)")
for num in range(1,20,2):
    print(num)
print("*******************************************************")


#numbers divisible by 3 from 3 to 30 (exclusive)
print("Numbers divisible by 3 from 3 to 30 (exclusive)")
for num in range(3,30):
    if (num%3==0):
        print(num)
print("*******************************************************")


#cube of number from 1 to 11 (exclusive)
print("Cube of number from 1 to 11 (exclusive)")
cube=[]
for num in range(1,11):
    cube.append(num**3)
    print(num)
for element in cube:
    print(element)




