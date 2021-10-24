#!/bin/python3

from functools import lru_cache
import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countInversions(arr):
    # Write your code here
    def merge_sort(arr, start_idx, end_idx):
        inv_count = 0
        if end_idx > start_idx:
            mid_idx = start_idx + math.ceil((end_idx -start_idx)/2)
            inv_count += merge_sort(arr, start_idx, mid_idx -1)
            inv_count += merge_sort(arr, mid_idx, end_idx)
            left_idx = start_idx
            right_idx = mid_idx
            tmp_arr = []
            while left_idx < mid_idx and right_idx <= end_idx:
                if arr[left_idx] > arr[right_idx]:
                    inv_count += mid_idx - left_idx
                    tmp_arr.append(arr[right_idx])
                    right_idx += 1
                else:
                    tmp_arr.append(arr[left_idx])
                    left_idx += 1
            tmp_arr.extend(arr[left_idx:mid_idx])
            tmp_arr.extend(arr[right_idx:end_idx +1])
            arr[start_idx: end_idx +1] = tmp_arr
        return inv_count
    return merge_sort(arr, 0, len(arr) -1);

if __name__ == '__main__':
    infile = open(sys.argv[1], 'r')
    t = int(infile.readline().strip())
    for t_itr in range(t):
        n = int(infile.readline().strip())
        arr = list(map(int, infile.readline().rstrip().split()))
        result = countInversions(arr)
        print(result)
