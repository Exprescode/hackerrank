#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    val_freq_dict = {}
    freq_count_dict = {1:0}
    output = []
    for [opt, val] in queries:
        if opt < 2:
            if val in val_freq_dict:
                val_freq_dict[val] += 1
                freq = val_freq_dict[val]
                if freq in freq_count_dict:
                    freq_count_dict[freq] += 1
                else:
                    freq_count_dict[freq] = 1
                freq_count_dict[freq - 1] -= 1
            else:
                val_freq_dict[val] = 1
                freq_count_dict[1] += 1
        elif opt > 2:
            if val in freq_count_dict:
                output.append(int(freq_count_dict[val] > 0))
            else:
                output.append(0)
        else:
            if val in val_freq_dict:
                freq = val_freq_dict[val]
                freq_count_dict[freq] -= 1
                if freq > 1:
                    val_freq_dict[val] -= 1
                    freq_count_dict[freq - 1] += 1
                else:
                    val_freq_dict.pop(val)
                    
    return output

if __name__ == '__main__':
    fptr = open(sys.argv[1])

    q = int(fptr.readline().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, fptr.readline().rstrip().split())))

    fptr.close()

    ans = freqQuery(queries)

    print('\n'.join(map(str, ans)))
