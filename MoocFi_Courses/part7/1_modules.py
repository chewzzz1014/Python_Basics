import math

def hypotenuse(leg1: float, leg2: float):
    return math.sqrt(leg1**2 + leg2**2)

import string

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

from fractions import Fraction

def fractionate(amount: int):
    results = []
    for i in range(amount):
        results.append(Fraction(1,amount))
    return results

