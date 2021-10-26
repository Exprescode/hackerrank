#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # Write your code here
    prices.sort()
    price_count = 0
    toy_count = 0
    for price in prices:
        price_count += price
        if price_count <= k:
            toy_count += 1
        else:
            break
    return toy_count

if __name__ == '__main__':
    infile = open(sys.argv[1])

    first_multiple_input = infile.readline().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, infile.readline().rstrip().split()))

    result = maximumToys(prices, k)

    print(result)
