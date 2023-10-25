import math

word = input('Please type in a word:')
if len(word) > 1:
    print(f'There are {len(word)} letters in the word {word}')
print('Thank you!')

n = float(input('Please type in a number:'))
integer_n = math.floor(n)
print(f'Integer part:{integer_n}')
print(f'Decimal part:{n-integer_n}')

