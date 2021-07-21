#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    magazine_dict = {}
    for word in magazine:
        magazine_dict[word] = magazine_dict[word] + 1 if word in magazine_dict else 1
    for word in note:
        if word in magazine_dict and magazine_dict[word] > 0:
            magazine_dict[word] -= 1
        else:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    in_file = open(sys.argv[1])

    first_multiple_input = in_file.readline().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = in_file.readline().rstrip().split()

    note = in_file.readline().rstrip().split()

    in_file.close()

    checkMagazine(magazine, note)
