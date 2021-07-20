#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    n_array = [0] * n
    for [a, b, k] in queries:
        n_array[a - 1] += k
        if b < n:
            n_array[b] -= k
    max_val = -math.inf
    cur_val = 0
    for val in n_array:
        cur_val += val
        if cur_val > max_val:
            max_val = cur_val
    return max_val

if __name__ == '__main__':
    in_file = open(sys.argv[1])

    first_multiple_input = in_file.readline().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, in_file.readline().rstrip().split())))

    in_file.close()

    result = arrayManipulation(n, queries)

    print(result)
