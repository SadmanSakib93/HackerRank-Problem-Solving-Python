#!/bin/python3

import math
import os
import random
import re
import sys

# def checkZero(list1, val): 
#     return(all(x <= val for x in list1)) 

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    result=[]
    statusAllZero=False
    while(len(arr)>0):
        minElem=min(arr)
        result.append(len(arr))
        arr = [x - minElem for x in arr]
        arr = [i for i in arr if i != 0]
        # print("minElem",minElem)
        # print(arr)
    return (result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
