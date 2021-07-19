#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap_count = 0
    val_holder = 0
    for idx, val in enumerate(arr):
        idx += 1
        while idx != val:
            val_holder = arr[val - 1]
            arr[val - 1] = val
            val = val_holder
            swap_count += 1
    return swap_count

if __name__ == '__main__':

    in_file = open(sys.argv[1])

    n = int(in_file.readline())

    arr = list(map(int, in_file.readline().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)
