#!/bin/python3

import math
import os
import random
import re
import sys
import string


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    lower_char = string.ascii_lowercase
    upper_char = string.ascii_uppercase
    list_s = list(s)
    for i in range(len(s)):
        if list_s[i] not in string.ascii_letters:
            continue
        elif list_s[i].islower():
            list_s[i] = lower_char[(lower_char.find(list_s[i]) + k) % 26]
        elif list_s[i].isupper:
            list_s[i] = upper_char[(upper_char.find(list_s[i]) + k) % 26]
    return "".join(list_s)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
