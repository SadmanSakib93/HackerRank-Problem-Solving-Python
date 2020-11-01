#!/bin/python3

import math
import os
import random
import re
import sys
def checkAllEven(arr):
    for each in arr:
        if(each%2!=0):
            return False
    return True
# Complete the fairRations function below.
def fairRations(B):
    count=0
    iterCount=0
    flag=False
    while(flag!=True and iterCount<=100):
        for i in range(len(B)-1):
            if(B[i]%2!=0):
                B[i]+=1
                B[i+1]+=1
                count+=2
        flag=checkAllEven(B)
        iterCount+=1

    if(iterCount<=100):
        return count
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
