#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    count = 0
    left_dict = {}
    right_dict = {}
    for element in arr:
        if element in right_dict:
            right_dict[element] += 1
        else:
            right_dict[element] = 1
    for j_val in arr:
        right_dict[j_val] -= 1
        if j_val % r == 0:
            i_val = j_val / r
            k_val = j_val * r
            if i_val in left_dict and k_val in right_dict:
                count += left_dict[i_val] * right_dict[k_val]
        if j_val in left_dict:
            left_dict[j_val] += 1
        else:
            left_dict[j_val] = 1
    return count

if __name__ == '__main__':
    fptr = open(sys.argv[1])

    nr = fptr.readline().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, fptr.readline().rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)

    fptr.close()
