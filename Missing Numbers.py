#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    result=[]
    arrDict=dict(collections.Counter(arr))
    brrDict=dict(collections.Counter(brr))
    if(len(arr)>len(brr)):
        for key, value in arrDict.items():
            if(value!=brrDict.get(key)):
                result.append(key)
    else:
        for key, value in brrDict.items():  
            if(value!=arrDict.get(key)):
                result.append(key)  
    result.sort() 
    return (result)          
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
