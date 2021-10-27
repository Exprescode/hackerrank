#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Write your code here
    stack = []
    del_count = 0
    for c in s:
        while len(stack) > 0:
            if stack[-1] == c:
                del_count += 1
                stack.pop()
            else:
                break
        stack.append(c)
    return del_count

if __name__ == '__main__':
    infile = open(sys.argv[1])

    q = int(infile.readline().strip())

    for q_itr in range(q):
        s = infile.readline()

        result = alternatingCharacters(s)

        print(result)
