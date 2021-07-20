#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    x_val = 0
    y_val = 0
    max_sum = -math.inf
    while x_val < 4:
        while y_val < 4:
            sum_val = sum(arr[x_val][y_val : y_val + 3]) + arr[x_val + 1][y_val + 1] + sum(arr[x_val + 2][y_val : y_val + 3])
            if sum_val > max_sum:
                max_sum = sum_val
            y_val += 1
        y_val = 0
        x_val += 1
    return max_sum

if __name__ == '__main__':
    in_file = open(sys.argv[1])

    arr = []

    for _ in range(6):
        arr.append(list(map(int, in_file.readline().rstrip().split())))

    in_file.close()

    result = hourglassSum(arr)

    print(result)
