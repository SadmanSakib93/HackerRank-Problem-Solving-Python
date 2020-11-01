#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    surf = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            currVal = A[i][j]
            tempVal = (currVal*4)+2            
            if i > 0:
                tempVal -= min(currVal, A[i-1][j])*2
            if j > 0:
                tempVal -= min(currVal, A[i][j-1])*2                
            surf += tempVal
            
    return surf
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
