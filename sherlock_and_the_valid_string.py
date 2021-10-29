#!/bin/python3

import math
import os
import random
import re
import sys
from typing import Tuple

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    sValid = 'YES'
    count = [0] * 26
    char_offset = ord('a')
    max_freq = 1
    max_count = 1
    for c in s:
        idx = ord(c) - char_offset
        count[idx] += 1
        if count[idx] > max_freq:
            max_freq = count[idx]
            max_count = 1
        elif count[idx] == max_freq:
            max_count += 1
    freq_freq = set(count)
    freq_freq.discard(0)
    freq_freq_sz = len(freq_freq)
    if freq_freq_sz > 2:
        sValid = 'NO'
    elif freq_freq_sz > 1: # freq_freq == 2
        freq_freq.discard(max_freq)
        min_freq = freq_freq.pop()
        min_count = 0
        for freq in count:
            if freq == min_freq:
                min_count += 1
        if max_count > 1 and min_count > 1:
            sValid = 'NO'
        if max_count == 1 and max_freq - min_freq > 1:
            sValid = 'NO'
        if min_count == 1 and min_freq != 1:
            sValid = 'NO'
    return sValid

if __name__ == '__main__':
    infile = open(sys.argv[1])

    s = infile.readline()

    infile.close()

    result = isValid(s)

    print(result)