#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the gemstones function below.
def gemstones(arr):
    count=0
    for eachAlph in list(string.ascii_lowercase):
        foundAll=True
        for eachString in arr:
            if(eachAlph not in eachString):
                foundAll=False
                break
        if(foundAll):
            count+=1
    return ( count)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
