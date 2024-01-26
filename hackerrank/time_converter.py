#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    times = s.split(':')
    hours = int(times[0])
    if 'AM' in s:
        if hours == 12:
            hours = '00'
    elif 'PM' in s:
        if hours != 12:
            hours += 12
    return f'{hours:{0}{2}}:{times[1]}:{times[2][:-2]}'

if __name__ == '__main__':
    s = input('Enter time: ')

    result = timeConversion(s)

    print(result)
