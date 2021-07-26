#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    # Write your code here
    for alpha in s1:
        if alpha in s2:
            return "YES"
    return "NO"

if __name__ == '__main__':
    in_file = open(sys.argv[1])

    q = int(in_file.readline().strip())

    for q_itr in range(q):
        s1 = in_file.readline()

        s2 = in_file.readline()

        result = twoStrings(s1, s2)

        print(result)

    in_file.close()
