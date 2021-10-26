#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    char_count = [0] * 26
    ascii_offset = ord('a')
    del_count = 0
    for c in a.strip():
        char_count[ord(c) - ascii_offset] += 1
    for c in b.strip():
        char_count[ord(c) - ascii_offset] -= 1
    for c in char_count:
        del_count += abs(c) 
    return del_count

if __name__ == '__main__':
    infile = open(sys.argv[1])

    a = infile.readline()

    b = infile.readline()

    infile.close()

    res = makeAnagram(a, b)

    print(res)