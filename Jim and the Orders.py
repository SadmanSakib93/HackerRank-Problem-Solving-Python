#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders):
    results=[]
    for i in range(len(orders)):
        results.append(orders[i][0]+orders[i][1])
    resultsIndex = sorted(range(len(results)), key=lambda k: results[k])
    resultsIndex[:]=[i+1 for i in resultsIndex]
    results.sort()
    return resultsIndex
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
