#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sorted_arr_asc = sorted(arr)
    sorted_arr_desc = sorted(arr, reverse=True)
    print(f'{sum(sorted_arr_asc[:-1])} {sum(sorted_arr_desc[:-1])}')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
