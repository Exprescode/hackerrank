#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    counter = 0
    for i in range(len(a) -1):
        for j in range(len(a) -1 -i):
            if a[j] > a[j +1]:
                a[j], a[j +1] = a[j +1], a[j]
                counter += 1
    print('Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}'.format(counter,a[0], a[-1]))


if __name__ == '__main__':
    infile = open(sys.argv[1], 'r')
    n = int(infile.readline().strip())
    a = list(map(int, infile.readline().rstrip().split()))
    infile.close()
    countSwaps(a)
