#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    n = len(grid)
    sorted_grid = [sorted(x) for x in grid]
    cols = []

    for col in range(len(grid[0])):
        cols.append([sorted_grid[row][col] for row in range(n)])

    sorted_rows = [1 if "".join(sorted_grid[x][:]) == "".join(sorted(sorted_grid[x][:])) else 0 for x in range(n)]
    sorted_cols = [1 if "".join(col) == "".join(sorted(col)) else 0 for col in cols]
    return 'YES' if (sum(sorted_cols) == len(grid[0]) and sum(sorted_rows) == n) else 'NO'


if __name__ == '__main__':
    t = int(input('# Test Cases: ').strip())

    for t_itr in range(t):
        n = int(input('# Rows: ').strip())

        grid = []

        for _ in range(n):
            grid_item = input('Grid Items: ')
            grid.append(grid_item)

        result = gridChallenge(grid)
        print(result)
