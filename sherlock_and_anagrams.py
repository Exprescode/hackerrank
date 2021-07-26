#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    substrs = {}
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substr = ''.join(sorted(s[i:j]))
            if substr in substrs:
                substrs[substr] += 1
            else: 
                substrs[substr] = 1
    count = 0
    for substr in substrs:
        n = substrs[substr]
        count +=  (n * (n - 1))/2
    return int(count)

if __name__ == '__main__':

    fptr = open(sys.argv[1])
    q = int(fptr.readline().strip())

    for q_itr in range(q):
        s = fptr.readline()
        result = sherlockAndAnagrams(s)
        print(result)

    fptr.close()
