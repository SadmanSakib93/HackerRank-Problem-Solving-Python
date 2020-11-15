#!/bin/python3

import math
import os
import random
import re
import sys

# Returns XOR of x and y 
def getXOR(x, y): 
    return ((x | y) & (~x | ~y)) 

# Complete the maximizingXor function below.
def maximizingXor(l, r):
    maxVal=0
    for i in range(l, r+1):
        for j in range(l, r+1):
            if(i!=j):
                xorVal=getXOR(i, j)
                if(maxVal<xorVal):
                    maxVal=xorVal
    return (maxVal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
