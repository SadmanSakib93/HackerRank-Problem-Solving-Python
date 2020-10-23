#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    counter=0
    iTemp=i
    jTemp=j
    while(iTemp<=jTemp):
        num=str(iTemp)
        numRev=num[::-1]
        result=abs(int(num)-int(numRev))/k
        if result.is_integer():
            counter+=1
        iTemp+=1
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
