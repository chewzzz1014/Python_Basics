import math
from random import seed, shuffle, randint, choice
import string
from fractions import Fraction

def hypotenuse(leg1: float, leg2: float):
    return math.sqrt(leg1**2 + leg2**2)

###############################################################

def separate_characters(my_string: str):
    r1 = ''
    r2 = ''
    r3 = ''
    for char in my_string:
        if char in string.ascii_letters:
            r1 += char
        elif char in string.punctuation:
            r2 += char
        else:
            r3 += char
    return r1,r2,r3

#################################################################
def fractionate(amount: int):
    results = []
    for i in range(amount):
        results.append(Fraction(1,amount))
    return results

############################################################

# seed(42)

def generate_password(length: int):
    words = list(string.ascii_lowercase)
    shuffle(words)
    return "".join(words[:length])


###############################################################
# TODO
def generate_strong_password(length, has_numbers, has_special_char):
    alphabets = string.ascii_lowercase
    numbers = '0123456789'
    special_characters = '!?=+-()#'

    words_1 = ''
    words_2 = ''
    words_3 = ''
    if has_numbers and has_special_char:
        words_1 = alphabets[ : randint(2,len(alphabets)-1)]
        words_2 = numbers[ : randint(2,len(numbers)-1)]
        words_3 = special_characters[ : randint(2,len(special_characters)-1)]
        shuffle(list(words_1))
        shuffle(list(words_2))
        shuffle(list(words_3))
    elif has_numbers:
        words_1 = alphabets[ : randint(2,len(alphabets)-1)]
        words_2 = numbers[ : randint(2,len(numbers)-1)]
        shuffle(list(words_1))
        shuffle(list(words_2))
    elif has_special_char:
        words_1 = alphabets[ : randint(2,len(alphabets)-1)]
        words_2 = special_characters[ : randint(2,len(special_characters-1))]
        shuffle(list(words_1))
        shuffle(list(words_2))
    else:
        words_1 = alphabets[:]
        shuffle(words_1)

    words = words_1 + words_2 + words_3
    shuffle(words)
    return "".join(words[:length])

for i in range(10):
    print(generate_strong_password(8, True, True))


###################################################################

def roll(die: str):
    dices = {
        'A': [3, 3, 3, 3, 3, 6],
        'B': [2, 2, 2, 5, 5, 5],
        'C': [1, 4, 4, 4, 4, 4]
    }
    return choice(dices[die])

def play(die1: str, die2: str, times: int):
    wins_die1 = 0
    wins_die2 = 0
    wins_ties = 0
    for i in range(times):
        result_die1 = roll(die1)
        result_die2 = roll(die2)
        if result_die1 > result_die2:
            wins_die1 += 1
        elif result_die1 < result_die2:
            wins_die2 += 1
        else:
            wins_ties += 1
    return wins_die1, wins_die2, wins_ties

# result = play("A", "C", 1000)
# print(result)
# result = play("B", "B", 1000)
# print(result)

#######################################################################

def words(n: int, beginning: str):
    results = []
    with open('words.txt') as rf:
        for line in rf:
            word = line.replace('\n', '')
            if word.startswith(beginning) and word not in results:
                results.append(word)
    if len(results)>=n:
        shuffle(results)
        return results[:n]
    else:
        raise ValueError

#######################################################################

