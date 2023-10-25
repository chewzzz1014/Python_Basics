import math

year = int(input('Please type in a number:'))
if year == 1984:
    print('Orwell')

n = int(input('Please type in a number'))
result = n
if n < 0:
    result = n * -1
print(f'The absolute value of this number is {result}')

customer_name = input('Please tell me your name:')
if customer_name != 'Jerry':
    portion = int(input('How many portions of soup?'))
    print(f'The total cost is {portion * 5.9}')
print('Next please!')

n = int(input('Please type in a number'))
if n < 1000:
    print('This number is smaller than 1000')
if n < 100:
    print('This number is smaller than 100')
if n < 10:
    print('This number is smaller than 10')
print('Thank you!')

n1 = int(input('Number 1:'))
n2 = int(input('Number 2:'))
op = input('Operation:')
if op == 'add':
    print(f'{n1} + {n2} = {n1 + n2}')
if op == 'multiply':
    print(f'{n1} * {n2} = {n1 * n2}')
if op == 'subtract':
    print(f'{n1} - {n2} = {n1 - n2}')

temp_f = int(input('Please type in a temperature (F):'))
temp_c = (temp_f-32) * (5/9)
print(f'{temp_f} degrees Fahrenheit equals {temp_c} degrees Celsius')
if temp_c < 0:
    print('Brr! It\'s cold in here!')

hr_wage = float(input('Hourly wage:'))
hr_worked = int(input('Hourly worked:'))
day = input('Day of the week')
if day == 'Sunday':
    print(f'Daily wages: {hr_wage * hr_worked * 2} euros')
else:
    print(f'Daily wages: {hr_wage * hr_worked } euros')

bonus_points = int(input('How many points are on your card?'))
if bonus_points < 100:
    print(f'Your bonus is 10 %')
    print(f'You now have {bonus_points * 1.1} points')
else:
    print(f'Your bonus is 15 %')
    print(f'You now have {bonus_points * 1.5} points')

# quadratic equation
a = int(input('Value of a:'))
b = int(input('Value of b:'))
c = int(input('Value of c:'))
print(f'The roots are {(-b + sqrt(b**2 - 4*a*c))/(2*a)} and {(-b - sqrt(b**2 - 4*a*c))/(2*a)}')