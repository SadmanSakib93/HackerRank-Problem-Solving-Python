#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    left=[]
    right=[]
    pivot=arr[0]
    result=[]
    for i in range(1, len(arr)):
        if(pivot>arr[i]):
            left.append(arr[i])
        else:
            right.append(arr[i])
    for each in left:
        result.append(each)
    result.append(pivot)
    for each in right:
        result.append(each)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
