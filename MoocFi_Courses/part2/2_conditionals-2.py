age = int(input('How old are you?'))
if age >= 18:
    print('You are of age!')
else:
    print('You are not of age!')

n1 = int(input('Please type in the first number:'))
n2 = int(input('Please type in another number:'))
if n1 > n2:
    print(f'The greater number was: {n1}')
elif n1 < n2:
    print(f'The greater number was: {n2}')
else:
    print('The numbers are equal!')

print('Person 1:')
name1 = input('Name')
age1 = int(input('Age'))
print('Person 2:')
name2 = input('Name')
age2 = int(input('Age'))
if age1 > age2:
    print(f'The elder is {name1}')
elif age1 < age2:
    print(f'The elder is {name2}')
else:
    print(f'{name1} and ${name2} are the same age')

word1 = input('Please type in the 1st word:')
word2 = input('Please type in the 2nd word:')
if word1 > word2:
    print(f'{word1} comes alphabetically last.')
elif word1 < word2:
    print(f'{word2} comes alphabetically last.')
else:
    print('You gave the same word twice.')