#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the stones function below.
def stones(n, a, b):
    return sorted(set([a*i+b*(n-1-i) for i in range(n)]))
    # lst = list(itertools.product([a, b], repeat=n-1))
    # resultSet=set()
    # for each in lst:
    #     resultSet.add(sum(each))
    # return (sorted(resultSet))

    return [0]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
