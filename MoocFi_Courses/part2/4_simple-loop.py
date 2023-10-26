import math

respond = ''
while respond != 'no':
    print('hi')
    respond = input('Shall we continue?')
print('okay then')

n = int(input('Please type in a number:'))
while n != 0:
    if n<0:
        print('Invalid number')
    else:
        print(math.sqrt(n))
    n = int(input('Please type in a number:'))
print('Exiting...')

p1 = input('Password:')
p2 = input('Repeat password:')
while p1 != p2:
    print('They do not match!')
    p2 = input('Repeat password:')
print('User account created!')

attempts = 1
pin = input('PIN:')
while pin != '4321':
    print('Wrong')
    pin = input('PIN:')
    attempts += 1
if attempts == 1:
    print('Correct! It only took you one single attempt!')
else:
    print(f'Correct! It took you {attempts} attempts')

year = int(input('Year:'))
leap = year
found = leap%100 == 0 and leap%400==0 or leap%4==0
while not found:
    leap += 1
    if leap%100 == 0 and leap%400==0 or leap%4==0:
        found = True
print(f'The next leap year after {year} is {leap}')

result = ''
prevWord = input('Please type in a word:')
while prevWord != 'end':
    result += prevWord + ' '
    word = input('Please type in a word:')
    if word == 'end' or word == prevWord:
        break
    else:
        result += word + ' '
    prevWord = input('Please type in a word:')
print(result)