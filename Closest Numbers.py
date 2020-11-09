#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    minDis=99999
    minList=[]
    print(arr)
    for i in range(0, len(arr)-1):
        tempMinDis=abs(arr[i]-arr[i+1])
        if(minDis>tempMinDis):
            minList.clear()
            minDis=tempMinDis
            minList.append(arr[i])
            minList.append(arr[i+1])
        elif(minDis==tempMinDis):
            minDis=tempMinDis
            minList.append(arr[i])
            minList.append(arr[i+1])
    return (minList)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
