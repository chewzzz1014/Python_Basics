n = int(input('Please type in a number:'))
print(f'{n} times 5 is {n*5}')

name = input('What is your name?')
year = int(input('Which year were you born?'))
print(f'Hi {name}, you will be {2023-year} years old at the end of year 2023')

days = int(input('How many days?'))
print(f'Seconds in that many days:{days * 24 * 3600}')

product = 1
number = int(input("Please type in the first number: "))
product *= number
number = int(input("Please type in the second number: "))
product *= number
number = int(input("Please type in the third number: "))
product *= number
print("The product is", product)

n1 = int(input('Number 1:'))
n2 = int(input('Number 2:'))
print(f'The sum of the numbers: {n1 + n2}')
print(f'The product of the numbers: {n1 * n2}')

product = 0
number = int(input("Number 1:"))
product += number
number = int(input("Number 2:"))
product += number
number = int(input("Number 3:"))
product += number
number = int(input("Number 4:"))
product += number
print(f'The sum of the numbers is {product} and the mean is {product / 4}')

lunch_times = int(input('How many times a week do you eat at the student cafeteria?'))
lunch_price = float(input('The price of a typical student lunch?'))
groceries_spent = float(input('How much money do you spend on groceries in a week?'))
print(f'\nAverage food expenditure:\n')
print(f'Daily: {(lunch_price * lunch_times + groceries_spent)} euros')
print(f'Weekly: {(lunch_price * lunch_times + groceries_spent)} euros')

num_std = int(input('How many students on the course?'))
grp_size = int(input('Desired group size?'))
print(f'Number of groups formed:{num_std//grp_size}')