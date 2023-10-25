age = int(input('What is your age?'))
if age < 0:
    print(f'That must be a mistake')
elif age < 5:
    print('I suspect you can\'t write quite yet...')
else:
    print(f'Ok, you\'re {age} years old')

name = input('Please type in your name:')
if name in ['Huey', 'Dewey', 'Louie']:
    print('I think you might be one of Donald Duck\'s nephews.')
elif name in ['Morty', 'Ferdie']:
    print('I think you might be one of Mickey Mouse\'s nephews.')
else:
    print('You\'re not a nephew of any character I know of.')

points = int(input('How many points [0-100]:'))
grade = 'impossible!'
if 0 <= points <= 49:
    grade = 'fail'
elif 50 <= points <= 59:
    grade = '1'
elif 60 <= points <= 69:
    grade = '2'
elif 70 <= points <= 79:
    grade = '3'
elif 80 <= points <= 89:
    grade = '4'
elif 90 <= points <= 100:
    grade = '5'
print(f'Grade: {grade}')

n = int(input('Number:'))
if n%3 == 0 and n%5 == 0:
    print('FizzBuzz')
elif n%3 == 0:
    print('Fizz')
elif n%5 == 0:
    print('Buzz')

year = int(input('Please type in a year:'))
if year%100 == 0:
    if year%400 == 0:
        print('That year is a leap year.')
    else:
        print('That year is not a leap year.')
elif year%4 == 0:
    print('That year is a leap year.')
else:
    print('That year is not a leap year.')

letter1 = input('1st letter:')
letter2 = input('2nd letter:')
letter3 = input('3rd letter:')
if letter2<letter1<letter3 or letter3<letter1<letter2:
    print(f'The letter in the middle is {letter1}')
elif letter1<letter2<letter3 or letter3<letter2<letter1:
    print(f'The letter in the middle is {letter2}')
elif letter1<letter3<letter2 or letter2<letter3<letter1:
    print(f'The letter in the middle is {letter3}')


