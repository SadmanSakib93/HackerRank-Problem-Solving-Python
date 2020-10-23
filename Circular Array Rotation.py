#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    result=[]
    a = collections.deque(a)
    a.rotate(k)
    print(a)
    for eachQ in queries:
        result.append(a[eachQ])
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
