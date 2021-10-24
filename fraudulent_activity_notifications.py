#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):    
    counter = 0
    d_odd =  d % 2 > 0
    mid_idx_a = d -(d//2) -1
    mid_idx_b = mid_idx_a +1
    trail = [0] * 201
    for i in expenditure[:d]:
        trail[i] += 1
    for i in range(d, len(expenditure)):
        idx_count = -1
        mid_val_a = -1
        mid_val_b = -1
        for exp, freq in enumerate(trail):
            idx_count += freq
            if mid_val_a < 0 and idx_count >= mid_idx_a:
                mid_val_a = exp
            if mid_val_b < 0 and idx_count >= mid_idx_b:
                mid_val_b = exp
                break
        median = mid_val_a if d_odd else (mid_val_a + mid_val_b) / 2
        if expenditure[i] >= median * 2:
            counter += 1
        trail[expenditure[i -d]] -= 1
        trail[expenditure[i]] += 1
    return counter

if __name__ == '__main__':
    infile = open(sys.argv[1], 'r')
    first_multiple_input = infile.readline().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    expenditure = list(map(int, infile.readline().rstrip().split()))
    infile.close()
    result = activityNotifications(expenditure, d)
    print(result)
