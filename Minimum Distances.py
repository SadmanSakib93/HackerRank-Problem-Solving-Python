#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    checkedValues=[]
    minVal=999999
    for each in a:
        if(each not in checkedValues):
            checkedValues.append(each)
            foundIndices = [n for n,x in enumerate(a) if x==each]
            print("each",each,"foundIndices",foundIndices)
            if(len(foundIndices)==2 and (abs(foundIndices[0]-foundIndices[1])<minVal)):
                minVal=abs(foundIndices[0]-foundIndices[1])
    if(minVal==999999):
        minVal=-1
    return (minVal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
